from pathlib import Path
from html import escape


OUTPUT = Path("assets/philosophy.svg")

WIDTH = 1200
HEIGHT = 400

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

    ENGINEERING LOOP // HOW I BUILD

</text>


<text
    x="40"
    y="78"
    fill="{TEXT}"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    BUILD FIRST. UNDERSTAND EVERYTHING.

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
<!-- LOOP -->
<!-- ===================================================== -->

"""


steps = [
    ("01", "LEARN", "understand the idea"),
    ("02", "BUILD", "turn it into something real"),
    ("03", "BREAK", "find where it falls apart"),
    ("04", "DEBUG", "figure out why"),
    ("05", "REBUILD", "make it better"),
]


start_x = 40
card_width = 205
gap = 28
y = 145


for index, (number, title, subtitle) in enumerate(steps):

    x = start_x + index * (card_width + gap)

    accent = [
        PURPLE,
        BLUE,
        VIOLET,
        PURPLE,
        BLUE
    ][index]


    svg += f"""

    <g>

        <rect
            x="{x}"
            y="{y}"
            width="{card_width}"
            height="130"
            rx="16"
            fill="{PANEL}"
            stroke="{BORDER}"
        />


        <text
            x="{x + 20}"
            y="{y + 27}"
            fill="{accent}"
            font-family="monospace"
            font-size="10"
            font-weight="700">

            {number}

        </text>


        <text
            x="{x + 20}"
            y="{y + 61}"
            fill="{TEXT}"
            font-family="monospace"
            font-size="17"
            font-weight="700">

            {title}

        </text>


        <text
            x="{x + 20}"
            y="{y + 89}"
            fill="{MUTED}"
            font-family="Arial"
            font-size="10">

            {esc(subtitle)}

        </text>


        <circle
            cx="{x + 20}"
            cy="{y + 111}"
            r="3"
            fill="{accent}"
        />

    </g>

    """


    # connector

    if index < len(steps) - 1:

        line_x = (
            x +
            card_width +
            6
        )

        svg += f"""

        <line
            x1="{line_x}"
            y1="{y + 65}"
            x2="{line_x + 16}"
            y2="{y + 65}"
            stroke="{PURPLE}"
            stroke-width="2"
            opacity="0.7"
        />

        """


# ============================================================
# FOOTER
# ============================================================

svg += f"""

<line
    x1="40"
    y1="310"
    x2="1160"
    y2="310"
    stroke="{BORDER}"
/>


<text
    x="40"
    y="342"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    THEORY

</text>


<text
    x="105"
    y="342"
    fill="{TEXT}"
    font-family="monospace"
    font-size="10">

    → PRACTICE

</text>


<text
    x="220"
    y="342"
    fill="{TEXT}"
    font-family="monospace"
    font-size="10">

    → FAILURE

</text>


<text
    x="325"
    y="342"
    fill="{TEXT}"
    font-family="monospace"
    font-size="10">

    → DEBUGGING

</text>


<text
    x="450"
    y="342"
    fill="{TEXT}"
    font-family="monospace"
    font-size="10">

    → UNDERSTANDING

</text>


<text
    x="1160"
    y="342"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="10"
    text-anchor="end">

    REPEAT

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
print("       PHILOSOPHY SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()
print("Done.")