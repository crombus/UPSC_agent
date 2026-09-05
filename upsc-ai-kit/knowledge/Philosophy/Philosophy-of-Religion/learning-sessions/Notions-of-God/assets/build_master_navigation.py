from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
OUT = HERE / "Notions-of-God_Master-Teaching-Navigation_2026-08-22.png"

W, H, DPI = 3200, 1800, 300
BG = (8, 22, 37)
CARD = (17, 42, 64)
WHITE = (239, 247, 252)
DIM = (169, 192, 208)
CYAN = (70, 214, 255)
TEAL = (78, 228, 190)
AMBER = (255, 183, 92)
MAGENTA = (229, 145, 255)
RED = (255, 140, 130)

FONT_DIR = Path(r"C:\Windows\Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


F_TITLE = font("segoeuib.ttf", 92)
F_SUB = font("segoeui.ttf", 34)
F_STAGE = font("segoeuib.ttf", 37)
F_HEAD = font("segoeuib.ttf", 35)
F_BODY = font("segoeui.ttf", 29)
F_BOLD = font("segoeuib.ttf", 29)
F_SMALL = font("segoeui.ttf", 25)


def rr(draw: ImageDraw.ImageDraw, box, radius=22, fill=None, outline=None, width=3):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text_lines(draw: ImageDraw.ImageDraw, text: str, font_obj, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font_obj) <= max_width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(draw, xy, text, font_obj, fill, max_width, leading=8):
    x, y = xy
    for line in text_lines(draw, text, font_obj, max_width):
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += font_obj.getbbox("Ag")[3] + leading
    return y


def arrow(draw, x0, y0, x1, y1, colour=CYAN, width=9):
    draw.line((x0, y0, x1, y1), fill=colour, width=width)
    if x1 >= x0:
        draw.polygon([(x1, y1), (x1 - 28, y1 - 17), (x1 - 28, y1 + 17)], fill=colour)
    else:
        draw.polygon([(x1, y1), (x1 + 28, y1 - 17), (x1 + 28, y1 + 17)], fill=colour)


def card(draw, x, y, w, h, number, title, colour, bullets, footer):
    rr(draw, (x, y, x + w, y + h), fill=CARD, outline=colour, width=4)
    rr(draw, (x + 24, y + 22, x + 116, y + 84), radius=30, fill=colour)
    draw.text((x + 57, y + 28), str(number), font=F_STAGE, fill=BG, anchor="ma")
    draw.text((x + 138, y + 28), title, font=F_HEAD, fill=colour)
    cy = y + 105
    for bullet in bullets:
        draw.ellipse((x + 35, cy + 12, x + 47, cy + 24), fill=colour)
        cy = draw_wrapped(draw, (x + 64, cy), bullet, F_BODY, WHITE, w - 100, 7) + 10
    footer_h = 88
    rr(draw, (x + 24, y + h - footer_h - 22, x + w - 24, y + h - 22),
       radius=14, fill=(42, 37, 55), outline=MAGENTA, width=3)
    draw_wrapped(draw, (x + 42, y + h - footer_h - 9), footer, F_BOLD, WHITE, w - 84, 5)


def main() -> None:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)

    draw.text((120, 85), "NOTIONS OF GOD", font=F_TITLE, fill=WHITE)
    draw.text(
        (122, 205),
        "MASTER TEACHING NAVIGATION  |  BASIC / MUST KNOW FIRST  |  OPTIONAL ENRICHMENT LAST",
        font=F_SUB,
        fill=CYAN,
    )
    draw_wrapped(
        draw,
        (122, 268),
        "This diagram maps the learning architecture, not the separate continuous Carvaka revision rail. "
        "Read left to right: define the grammar, build the Western profile, learn Indian systems with parity, "
        "test relations and conflicts, then route the result into verified PYQs and mark-scaled answers.",
        F_SMALL,
        DIM,
        2940,
        5,
    )

    card_w, card_h, gap = 535, 1090, 55
    x0, y0 = 115, 430
    stages = [
        (
            "CONCEPTUAL GRAMMAR",
            CYAN,
            [
                "Personal / impersonal: agency and relation versus transpersonal ultimacy.",
                "Transcendent / immanent: independence without remoteness; presence without automatic identity.",
                "Cataphatic / apophatic: affirm perfections, then deny creaturely limitation.",
                "Classify before proving: a first cause is not yet the God of worship.",
            ],
            "Answer use: define the exact grammar before naming a school.",
        ),
        (
            "WESTERN CORE",
            AMBER,
            [
                "Classical theism, deism, pantheism and panentheism.",
                "Creation ex nihilo as total dependence, not manufacture from prior stuff.",
                "Omni-attributes plus eternity, immutability, impassibility, necessity, aseity and simplicity.",
                "Spinoza: substance, attributes, modes, Deus sive Natura and necessity.",
            ],
            "Answer use: connect each model to world relation and religious function.",
        ),
        (
            "INDIAN PARITY",
            TEAL,
            [
                "Advaita: Nirguna Brahman, Saguna Ishvara, maya, adhyasa, vivarta and levels of reality.",
                "Ramanuja: Ishvara-cit-acit, body-self relation, aprthak-siddhi, parinama, bhakti and prapatti.",
                "Nyaya: eternal omniscient self, efficient cause, atoms, karma and adrsta.",
                "Madhva, Saiva and Sakta: dependence, difference, divine power and liberation.",
            ],
            "Answer use: never flatten identity, appearance, embodiment and efficient causation.",
        ),
        (
            "COHERENCE TEST",
            RED,
            [
                "Power versus logic; foreknowledge versus freedom; goodness versus evil.",
                "Immutability / impassibility versus love; timelessness versus action.",
                "Simplicity versus many predicates and free creation.",
                "God-world-human comparison plus the physical-manifestation question.",
            ],
            "Answer use: objection -> best reply -> residual pressure.",
        ),
        (
            "EXAM ROUTING",
            MAGENTA,
            [
                "All 13 verified owner PYQs, 2018-2024; no primary owner question in 2025.",
                "Decode elucidate, discuss, evaluate and critically examine.",
                "10 / 15 / 20 marks require increasing doctrine, evidence, comparison and evaluation.",
                "Finish with a graded verdict and a final register-note recall spine.",
            ],
            "Answer use: thesis -> named doctrine -> analysis -> qualification -> verdict.",
        ),
    ]

    for i, (title, colour, bullets, footer) in enumerate(stages, 1):
        x = x0 + (i - 1) * (card_w + gap)
        card(draw, x, y0, card_w, card_h, i, title, colour, bullets, footer)
        if i < len(stages):
            arrow(draw, x + card_w + 5, y0 + card_h // 2, x + card_w + gap - 8, y0 + card_h // 2)

    rr(draw, (115, 1580, 3085, 1710), fill=(13, 35, 53), outline=TEAL, width=3)
    draw.text((145, 1600), "BASIC / MUST KNOW", font=F_HEAD, fill=TEAL)
    draw_wrapped(
        draw,
        (485, 1600),
        "Everything needed for direct PYQs and a complete core answer appears before enrichment. "
        "Advanced material deepens simplicity, free-will solutions, apophatic theology, Abrahamic comparison and extra critique; "
        "it never repairs a missing Basic doctrine.",
        F_BODY,
        WHITE,
        2550,
        6,
    )

    image.save(OUT, dpi=(DPI, DPI))
    print(OUT)


if __name__ == "__main__":
    main()
