from pathlib import Path
from html import escape


OUTPUT = Path("assets/learning.svg")

WIDTH = 1200
HEIGHT = 470

BG = "#070914"
PANEL = "#0c0f20"
BORDER = "#24284a"

TEXT = "#f4f1ff"
MUTED = "#858aa8"

PURPLE = "#c084fc"
VIOLET = "#8b5cf6"
BLUE = "#38bdf8"


def esc(value):
    return escape(str(value))


def text(
    x,
    y,
    value,
    size=14,
    color=TEXT,
    weight="400",
    anchor="start",
    family="Arial"
):
    return f"""
    <text
        x="{x}"
        y="{y}"
        fill="{color}"
        font-family="{family}, sans-serif"
        font-size="{size}px"
        font-weight="{weight}"
        text-anchor="{anchor}">
        {esc(value)}
    </text>
    """


def learning_card(
    x,
    y,
    title,
    subtitle,
    progress,
    accent
):

    width = 350
    height = 115

    bar_width = int(270 * progress)

    return f"""
    <g>

        <rect
            x="{x}"
            y="{y}"
            width="{width}"
            height="{height}"
            rx="16"
            fill="{PANEL}"
            stroke="{BORDER}"
        />

        <text
            x="{x + 22}"
            y="{y + 29}"
            fill="{TEXT}"
            font-family="monospace"
            font-size="13"
            font-weight="700">

            {esc(title)}

        </text>

        <text
            x="{x + 22}"
            y="{y + 52}"
            fill="{MUTED}"
            font-family="Arial"
            font-size="11">

            {esc(subtitle)}

        </text>

        <rect
            x="{x + 22}"
            y="{y + 72}"
            width="270"
            height="7"
            rx="4"
            fill="#171a2d"
        />

        <rect
            x="{x + 22}"
            y="{y + 72}"
            width="{bar_width}"
            height="7"
            rx="4"
            fill="{accent}"
        />

        <text
            x="{x + 315}"
            y="{y + 79}"
            fill="{accent}"
            font-family="monospace"
            font-size="9"
            text-anchor="end">

            ACTIVE

        </text>

    </g>
    """


svg = f"""<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<defs>

    <linearGradient
        id="bg"
        x1="0"
        y1="0"
        x2="1"
        y2="1">

        <stop
            offset="0%"
            stop-color="#070914"/>

        <stop
            offset="55%"
            stop-color="#090b19"/>

        <stop
            offset="100%"
            stop-color="#12091d"/>

    </linearGradient>

    <linearGradient
        id="accent"
        x1="0"
        y1="0"
        x2="1"
        y2="0">

        <stop
            offset="0%"
            stop-color="{VIOLET}"/>

        <stop
            offset="50%"
            stop-color="{PURPLE}"/>

        <stop
            offset="100%"
            stop-color="{BLUE}"/>

    </linearGradient>

</defs>


<!-- BACKGROUND -->

<rect
    width="100%"
    height="100%"
    rx="28"
    fill="url(#bg)"
/>


<!-- GRID -->

<g opacity="0.10">
"""


for x in range(0, WIDTH + 1, 50):

    svg += f"""
    <line
        x1="{x}"
        y1="0"
        x2="{x}"
        y2="{HEIGHT}"
        stroke="#252846"
    />
    """


for y in range(0, HEIGHT + 1, 50):

    svg += f"""
    <line
        x1="0"
        y1="{y}"
        x2="{WIDTH}"
        y2="{y}"
        stroke="#252846"
    />
    """


svg += f"""
</g>


<!-- HEADER -->

<circle
    cx="40"
    cy="36"
    r="6"
    fill="#22c55e"
/>


<text
    x="57"
    y="41"
    fill="{MUTED}"
    font-family="monospace"
    font-size="13"
    font-weight="600">

    CURRENTLY LEARNING // 2026

</text>


<text
    x="40"
    y="78"
    fill="{TEXT}"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    STILL COOKING

</text>


<line
    x1="40"
    y1="100"
    x2="1160"
    y2="100"
    stroke="url(#accent)"
    stroke-width="2"
    opacity="0.7"
/>


<!-- LEARNING CARDS -->

"""


cards = [

    (
        40,
        125,
        "DSA",
        "Graphs • DP • Trees • Optimization",
        0.82,
        PURPLE
    ),

    (
        425,
        125,
        "BACKEND",
        "APIs • Databases • Caching • Architecture",
        0.68,
        BLUE
    ),

    (
        810,
        125,
        "SYSTEM DESIGN",
        "LLD • HLD • Scalability • Reliability",
        0.55,
        VIOLET
    ),

    (
        40,
        260,
        "AI ENGINEERING",
        "RAG • Agents • LLM Systems",
        0.72,
        PURPLE
    ),

    (
        425,
        260,
        "INFRASTRUCTURE",
        "Docker • Kubernetes • AWS • CI/CD",
        0.48,
        BLUE
    ),

]


for card in cards:

    svg += learning_card(*card)


# CURRENT MODE PANEL

svg += f"""

<g>

    <rect
        x="810"
        y="260"
        width="350"
        height="115"
        rx="16"
        fill="{PANEL}"
        stroke="{BORDER}"
    />

    <circle
        cx="840"
        cy="293"
        r="6"
        fill="#22c55e"
    />

    <text
        x="858"
        y="298"
        fill="{PURPLE}"
        font-family="monospace"
        font-size="12"
        font-weight="700">

        CURRENT MODE

    </text>

    <text
        x="832"
        y="330"
        fill="{TEXT}"
        font-family="monospace"
        font-size="12">

        LEARN → BUILD → BREAK

    </text>

    <text
        x="832"
        y="353"
        fill="{TEXT}"
        font-family="monospace"
        font-size="12">

        → FIX → UNDERSTAND → REPEAT

    </text>

</g>


<!-- FOOTER -->

<line
    x1="40"
    y1="405"
    x2="1160"
    y2="405"
    stroke="{BORDER}"
/>


<text
    x="40"
    y="435"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    NO FINISH LINE // JUST THE NEXT THING TO LEARN

</text>


<text
    x="1160"
    y="435"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="10"
    text-anchor="end">

    BUILDING

</text>


</svg>
"""


OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT.write_text(
    svg,
    encoding="utf-8"
)


print()
print("==============================================")
print("         LEARNING SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()
print("Done.")