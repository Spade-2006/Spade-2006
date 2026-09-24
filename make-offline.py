from pathlib import Path
from html import escape


OUTPUT = Path("assets/offline.svg")

WIDTH = 1200
HEIGHT = 420

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


def hobby_card(
    x,
    y,
    number,
    title,
    description,
    accent
):

    width = 250
    height = 115

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
            x="{x + 20}"
            y="{y + 25}"
            fill="{accent}"
            font-family="monospace"
            font-size="9"
            font-weight="700">

            {esc(number)}

        </text>


        <text
            x="{x + 20}"
            y="{y + 52}"
            fill="{TEXT}"
            font-family="monospace"
            font-size="15"
            font-weight="700">

            {esc(title)}

        </text>


        <text
            x="{x + 20}"
            y="{y + 78}"
            fill="{MUTED}"
            font-family="Arial"
            font-size="10">

            {esc(description)}

        </text>


        <circle
            cx="{x + 222}"
            cy="{y + 90}"
            r="3"
            fill="{accent}"
        />

    </g>
    """


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

    OFFLINE MODE // OUTSIDE THE CODE

</text>


<text
    x="40"
    y="78"
    fill="{TEXT}"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    WHEN THE TERMINAL IS CLOSED

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
<!-- HOBBIES -->
<!-- ===================================================== -->

"""


hobbies = [

    (
        40,
        125,
        "01",
        "SKETCH",
        "Anime, people & random ideas",
        PURPLE
    ),

    (
        320,
        125,
        "02",
        "EXPLORE",
        "Travel, places & visual memories",
        BLUE
    ),

    (
        600,
        125,
        "03",
        "PLAY",
        "Chess, strategy & competitive thinking",
        VIOLET
    ),

    (
        880,
        125,
        "04",
        "READ",
        "Books, ideas & things worth knowing",
        PURPLE
    ),

    (
        180,
        260,
        "05",
        "LISTEN",
        "Music, podcasts & audiobooks",
        BLUE
    ),

    (
        740,
        260,
        "06",
        "DISCONNECT",
        "Disappear. Think. Come back with an idea.",
        VIOLET
    ),

]


for hobby in hobbies:

    svg += hobby_card(*hobby)


# ============================================================
# FOOTER
# ============================================================

svg += f"""

<line
    x1="40"
    y1="390"
    x2="1160"
    y2="390"
    stroke="{BORDER}"
/>


<text
    x="40"
    y="408"
    fill="{MUTED}"
    font-family="monospace"
    font-size="9">

    SOMETIMES THE BEST IDEAS HAPPEN WHEN NOTHING IS BEING BUILT.

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
print("          OFFLINE SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()
print("Done.")