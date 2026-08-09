"""
Generate study illustrations with an Azure OpenAI GPT Image deployment.

Configuration is loaded from environment variables (and an ignored .env file):
    AZURE_IMAGE_ENDPOINT
    AZURE_IMAGE_API_KEY
    AZURE_IMAGE_API_VERSION
    AZURE_IMAGE_SIZE
    AZURE_IMAGE_QUALITY

AZURE_IMAGE_ENDPOINT can be the complete /images/generations URL. The configured
API version replaces any api-version already present in that URL.

Usage:
    python tools/azure_image_generator.py ^
        --prompt "A conceptual illustration of the Constituent Assembly" ^
        --output notes/Polity/generated-images/constituent-assembly.png
"""

from __future__ import annotations

import argparse
import base64
import binascii
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_API_VERSION = "2025-04-01-preview"
DEFAULT_SIZE = "1536x1024"
DEFAULT_QUALITY = "medium"
SUPPORTED_FORMATS = {"png", "jpeg", "webp"}


class ImageGenerationError(RuntimeError):
    """Raised when Azure does not return a usable generated image."""


@dataclass(frozen=True)
class AzureImageConfig:
    endpoint: str
    api_key: str
    api_version: str = DEFAULT_API_VERSION
    size: str = DEFAULT_SIZE
    quality: str = DEFAULT_QUALITY

    @classmethod
    def from_env(cls) -> "AzureImageConfig":
        load_dotenv()
        endpoint = os.environ.get("AZURE_IMAGE_ENDPOINT", "").strip()
        api_key = os.environ.get("AZURE_IMAGE_API_KEY", "").strip()
        missing = [
            name
            for name, value in (
                ("AZURE_IMAGE_ENDPOINT", endpoint),
                ("AZURE_IMAGE_API_KEY", api_key),
            )
            if not value
        ]
        if missing:
            raise ImageGenerationError(
                f"Missing Azure image configuration: {', '.join(missing)}"
            )
        return cls(
            endpoint=endpoint,
            api_key=api_key,
            api_version=os.environ.get(
                "AZURE_IMAGE_API_VERSION", DEFAULT_API_VERSION
            ).strip(),
            size=os.environ.get("AZURE_IMAGE_SIZE", DEFAULT_SIZE).strip(),
            quality=os.environ.get(
                "AZURE_IMAGE_QUALITY", DEFAULT_QUALITY
            ).strip(),
        )

    @property
    def generation_url(self) -> str:
        parts = urlsplit(self.endpoint)
        if parts.scheme != "https" or not parts.netloc:
            raise ImageGenerationError(
                "AZURE_IMAGE_ENDPOINT must be a valid HTTPS URL."
            )
        if not parts.path.rstrip("/").endswith("/images/generations"):
            raise ImageGenerationError(
                "AZURE_IMAGE_ENDPOINT must end with /images/generations."
            )
        query = dict(parse_qsl(parts.query, keep_blank_values=True))
        query["api-version"] = self.api_version
        return urlunsplit(
            (parts.scheme, parts.netloc, parts.path, urlencode(query), "")
        )


def _retrying_session() -> requests.Session:
    retry = Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"POST"}),
        respect_retry_after_header=True,
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


def _api_error(response: requests.Response) -> ImageGenerationError:
    request_id = response.headers.get("x-request-id") or response.headers.get(
        "apim-request-id"
    )
    detail = ""
    try:
        body = response.json()
        error = body.get("error", body) if isinstance(body, dict) else body
        if isinstance(error, dict):
            code = error.get("code")
            message = error.get("message")
            detail = " - ".join(str(value) for value in (code, message) if value)
    except ValueError:
        detail = response.text.strip()[:500]

    suffix = f" Request ID: {request_id}." if request_id else ""
    return ImageGenerationError(
        f"Azure image generation failed with HTTP {response.status_code}"
        f"{f': {detail}' if detail else '.'}{suffix}"
    )


def _decode_image(item: dict[str, Any]) -> bytes:
    encoded = item.get("b64_json")
    if not encoded:
        raise ImageGenerationError(
            "Azure returned an image item without b64_json data."
        )
    try:
        image_bytes = base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise ImageGenerationError(
            "Azure returned invalid base64 image data."
        ) from exc
    if not image_bytes:
        raise ImageGenerationError("Azure returned an empty image.")
    return image_bytes


def _write_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=path.parent, prefix=f".{path.name}.", delete=False
        ) as handle:
            handle.write(content)
            temp_path = Path(handle.name)
        os.replace(temp_path, path)
    finally:
        if temp_path and temp_path.exists():
            temp_path.unlink()


def generate_image(
    prompt: str,
    output_path: str | Path,
    *,
    size: str | None = None,
    quality: str | None = None,
    output_format: str = "png",
    config: AzureImageConfig | None = None,
    session: requests.Session | None = None,
    timeout: tuple[int, int] = (15, 300),
) -> Path:
    """Generate one image and save it atomically to output_path."""
    prompt = prompt.strip()
    if not prompt:
        raise ValueError("Image prompt cannot be empty.")

    output_format = output_format.lower().strip()
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported output format '{output_format}'. "
            f"Choose from: {', '.join(sorted(SUPPORTED_FORMATS))}."
        )

    config = config or AzureImageConfig.from_env()
    payload = {
        "prompt": prompt,
        "n": 1,
        "size": size or config.size,
        "quality": quality or config.quality,
        "output_format": output_format,
    }
    client = session or _retrying_session()
    try:
        response = client.post(
            config.generation_url,
            headers={
                "api-key": config.api_key,
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=timeout,
        )
    except requests.RequestException as exc:
        raise ImageGenerationError(
            f"Azure image generation request failed: {exc}"
        ) from exc

    if not response.ok:
        raise _api_error(response)

    try:
        body = response.json()
    except ValueError as exc:
        raise ImageGenerationError(
            "Azure returned a non-JSON success response."
        ) from exc

    if isinstance(body, dict) and body.get("error"):
        error = body["error"]
        detail = error.get("message", str(error)) if isinstance(error, dict) else error
        raise ImageGenerationError(f"Azure image generation failed: {detail}")

    data = body.get("data") if isinstance(body, dict) else None
    if not isinstance(data, list) or not data or not isinstance(data[0], dict):
        raise ImageGenerationError(
            "Azure response did not contain a generated image."
        )

    destination = Path(output_path).expanduser()
    _write_atomic(destination, _decode_image(data[0]))
    return destination.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate one Azure GPT Image illustration."
    )
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--size")
    parser.add_argument("--quality", choices=("low", "medium", "high"))
    parser.add_argument(
        "--format", dest="output_format", choices=sorted(SUPPORTED_FORMATS),
        default="png",
    )
    args = parser.parse_args()

    try:
        output = generate_image(
            args.prompt,
            args.output,
            size=args.size,
            quality=args.quality,
            output_format=args.output_format,
        )
    except (ImageGenerationError, ValueError) as exc:
        parser.exit(1, f"Image generation failed: {exc}\n")

    print(f"Image saved: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
