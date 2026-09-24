from pathlib import Path
from html import escape


OUTPUT = Path("assets/building.svg")

WIDTH = 1200
HEIGHT = 520

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


def card(
    x,
    y,
    title,
    subtitle,
    lines,
    accent
):

    width = 530
    height = 135

    svg = f"""

    <g>

        <rect
            x="{x}"
            y="{y}"
            width="{width}"
            height="{height}"
            rx="18"
            fill="{PANEL}"
            stroke="{BORDER}"
        />

        <rect
            x="{x}"
            y="{y}"
            width="4"
            height="{height}"
            rx="2"
            fill="{accent}"
        />


        <text
            x="{x + 24}"
            y="{y + 31}"
            fill="{accent}"
            font-family="monospace"
            font-size="11"
            font-weight="700">

            {esc(title)}

        </text>


        <text
            x="{x + 24}"
            y="{y + 56}"
            fill="{TEXT}"
            font-family="Arial"
            font-size="15"
            font-weight="700">

            {esc(subtitle)}

        </text>

    """

    current_y = y + 82

    for line in lines:

        svg += f"""

        <text
            x="{x + 24}"
            y="{current_y}"
            fill="{MUTED}"
            font-family="monospace"
            font-size="10">

            {esc(line)}

        </text>

        """

        current_y += 18


    svg += """

    </g>

    """

    return svg


# ============================================================
# SVG
# ============================================================

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


<!-- ===================================================== -->
<!-- BACKGROUND -->
<!-- ===================================================== -->

<rect
    width="100%"
    height="100%"
    rx="28"
    fill="url(#bg)"
/>


<!-- ===================================================== -->
<!-- GRID -->
<!-- ===================================================== -->

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


<!-- ===================================================== -->
<!-- HEADER -->
<!-- ===================================================== -->

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

    BUILD PATTERNS // WHAT I LIKE MAKING

</text>


<text
    x="40"
    y="78"
    fill="{TEXT}"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    THINGS THAT ARE SLIGHTLY OVERENGINEERED

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


<!-- ===================================================== -->
<!-- BUILDING CATEGORIES -->
<!-- ===================================================== -->

"""


svg += card(
    40,
    125,
    "01 // SYSTEMS",
    "Things that actually have machinery underneath.",
    [
        "APIs  •  databases  •  caching  •  architecture",
        "logic that keeps working when the UI disappears"
    ],
    PURPLE
)


svg += card(
    630,
    125,
    "02 // EXPERIMENTS",
    "Ideas that probably did not need to exist.",
    [
        "games  •  interactive systems  •  visual experiments",
        "if it sounds unnecessarily ambitious → interesting"
    ],
    BLUE
)


svg += card(
    40,
    280,
    "03 // PROBLEM SOLVING",
    "Turning annoying problems into engineering problems.",
    [
        "DSA  •  optimization  •  algorithms  •  decision systems",
        "find the bottleneck → understand it → build around it"
    ],
    VIOLET
)


svg += card(
    630,
    280,
    "04 // PRODUCTS",
    "Tools that are meant to actually be used.",
    [
        "tracking  •  productivity  •  developer tools  •  data",
        "collect → process → visualize → make the thing useful"
    ],
    PURPLE
)


# ============================================================
# FOOTER
# ============================================================

svg += f"""

<line
    x1="40"
    y1="440"
    x2="1160"
    y2="440"
    stroke="{BORDER}"
/>


<text
    x="40"
    y="470"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    CURRENT RULE

</text>


<text
    x="160"
    y="470"
    fill="{TEXT}"
    font-family="monospace"
    font-size="10">

    IF IT CAN BE BUILT → BUILD IT

</text>


<text
    x="1160"
    y="470"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="10"
    text-anchor="end">

    OVERENGINEER // LEARN // REPEAT

</text>


</svg>
"""


# ============================================================
# WRITE
# ============================================================

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
print("         BUILDING SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()
print("Done.")