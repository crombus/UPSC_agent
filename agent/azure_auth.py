"""
Shared Azure auth helper.
Uses DefaultAzureCredential — works with Azure CLI login,
Managed Identity, VS Code login, or environment service principal.
No API keys needed when key-auth is disabled on the resource.
"""

import os
from functools import lru_cache
from typing import Any, Iterator, List, Optional
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage
from langchain_core.outputs import ChatResult, ChatGeneration, ChatGenerationChunk
from langchain_core.messages import AIMessageChunk
from dotenv import load_dotenv

load_dotenv()


@lru_cache(maxsize=1)
def _token_provider():
    credential = DefaultAzureCredential()
    return get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")


@lru_cache(maxsize=4)
def _get_azure_client(endpoint: str, deployment: str, api_version: str, use_entra: bool):
    """Cached AzureOpenAI client — created once per unique config."""
    from openai import AzureOpenAI
    if use_entra:
        return AzureOpenAI(
            azure_endpoint          = endpoint,
            azure_deployment        = deployment,
            api_version             = api_version,
            azure_ad_token_provider = _token_provider(),
        )
    return AzureOpenAI(
        azure_endpoint   = endpoint,
        azure_deployment = deployment,
        api_version      = api_version,
    )


# ── Custom wrapper for Azure Responses API (gpt-5.x models) ──────────────────

class AzureResponsesChatModel(BaseChatModel):
    """
    LangChain-compatible wrapper for Azure OpenAI Responses API.
    Required for gpt-5.x models which use /responses instead of /chat/completions.
    """
    azure_endpoint: str
    deployment: str
    api_version: str
    use_entra_id: bool = True
    api_key_val: str = ""

    def _get_client(self):
        return _get_azure_client(
            self.azure_endpoint, self.deployment,
            self.api_version, self.use_entra_id
        )

    def _convert_messages(self, messages: List[BaseMessage]) -> List[dict]:
        result = []
        for m in messages:
            if isinstance(m, SystemMessage):
                result.append({"role": "system", "content": m.content})
            elif isinstance(m, HumanMessage):
                result.append({"role": "user", "content": m.content})
            elif isinstance(m, AIMessage):
                result.append({"role": "assistant", "content": m.content})
            else:
                result.append({"role": "user", "content": str(m.content)})
        return result

    def _generate(self, messages: List[BaseMessage], stop=None, run_manager=None, **kwargs) -> ChatResult:
        client = self._get_client()
        input_msgs = self._convert_messages(messages)
        response = client.responses.create(
            model = self.deployment,
            input = input_msgs,
        )
        content = response.output_text
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=content))])

    def _stream(self, messages: List[BaseMessage], stop=None, run_manager=None, **kwargs) -> Iterator[ChatGenerationChunk]:
        """Stream tokens as they arrive — biggest latency fix."""
        client = self._get_client()
        input_msgs = self._convert_messages(messages)
        stream = client.responses.create(
            model  = self.deployment,
            input  = input_msgs,
            stream = True,
        )
        for event in stream:
            # Azure Responses API streaming event type for text deltas
            if getattr(event, "type", "") == "response.output_text.delta":
                delta = getattr(event, "delta", "")
                if delta:
                    yield ChatGenerationChunk(message=AIMessageChunk(content=delta))
            elif getattr(event, "type", "") == "response.text.delta":
                delta = getattr(event, "delta", "")
                if delta:
                    yield ChatGenerationChunk(message=AIMessageChunk(content=delta))

    @property
    def _llm_type(self) -> str:
        return "azure-responses-api"


# ── Public helpers ────────────────────────────────────────────────────────────

def get_embedding_model() -> AzureOpenAIEmbeddings:
    """
    Returns embedding model. Uses API key if AZURE_EMBEDDING_API_KEY is set,
    otherwise falls back to Entra ID (DefaultAzureCredential).
    """
    api_key = os.environ.get("AZURE_EMBEDDING_API_KEY", "")
    if api_key:
        return AzureOpenAIEmbeddings(
            azure_endpoint   = os.environ["AZURE_EMBEDDING_ENDPOINT"],
            azure_deployment = os.environ["AZURE_EMBEDDING_DEPLOYMENT"],
            api_version      = os.environ.get("AZURE_EMBEDDING_API_VERSION", "2023-05-15"),
            api_key          = api_key,
        )
    return AzureOpenAIEmbeddings(
        azure_endpoint          = os.environ["AZURE_EMBEDDING_ENDPOINT"],
        azure_deployment        = os.environ["AZURE_EMBEDDING_DEPLOYMENT"],
        api_version             = os.environ.get("AZURE_EMBEDDING_API_VERSION", "2023-05-15"),
        azure_ad_token_provider = _token_provider(),
    )


def get_chat_model(temperature: float = 0.2, max_tokens: int = 4096):
    """
    Returns chat model. Uses Azure Responses API for gpt-5.x models (Entra ID auth).
    Falls back to LiteLLM for non-Azure providers (openai/*, anthropic/*, ollama/*).
    """
    azure_endpoint = os.environ.get("AZURE_CHAT_ENDPOINT", "")
    deployment     = os.environ.get("AZURE_CHAT_DEPLOYMENT", "")
    api_version    = os.environ.get("AZURE_CHAT_API_VERSION", "2025-04-01-preview")
    api_key        = os.environ.get("AZURE_CHAT_API_KEY", "")
    litellm_model  = os.environ.get("LITELLM_MODEL", "")

    # Azure endpoint — use Responses API wrapper (supports gpt-5.x + Entra ID)
    if azure_endpoint and deployment:
        return AzureResponsesChatModel(
            azure_endpoint = azure_endpoint,
            deployment     = deployment,
            api_version    = api_version,
            use_entra_id   = not bool(api_key),
            api_key_val    = api_key,
        )

    # Non-Azure provider — route through LiteLLM
    if litellm_model:
        import litellm
        litellm.drop_params = True
        from langchain_litellm import ChatLiteLLM
        return ChatLiteLLM(
            model       = litellm_model,
            api_base    = os.environ.get("LITELLM_API_BASE"),
            api_key     = os.environ.get("LITELLM_API_KEY"),
            temperature = temperature,
            max_tokens  = max_tokens,
        )

    raise ValueError("No chat model configured. Set AZURE_CHAT_ENDPOINT + AZURE_CHAT_DEPLOYMENT in .env")

