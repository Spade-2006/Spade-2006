from pathlib import Path
from html import escape


# ============================================================
# CONFIG
# ============================================================

OUTPUT = Path("assets/achievements.svg")

WIDTH = 1200
HEIGHT = 900

BG = "#070914"
PANEL = "#0c0f20"
PANEL_2 = "#10132a"
BORDER = "#24284a"

TEXT = "#f4f1ff"
MUTED = "#858aa8"

PURPLE = "#c084fc"
VIOLET = "#8b5cf6"
BLUE = "#38bdf8"


# ============================================================
# HELPERS
# ============================================================

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


def metric_card(x, y, value, label):

    return f"""
    <g>

        <rect
            x="{x}"
            y="{y}"
            width="255"
            height="115"
            rx="18"
            fill="{PANEL}"
            stroke="{BORDER}"
        />

        <text
            x="{x + 24}"
            y="{y + 48}"
            fill="{TEXT}"
            font-family="monospace"
            font-size="28"
            font-weight="700">

            {esc(value)}

        </text>

        <text
            x="{x + 24}"
            y="{y + 82}"
            fill="{MUTED}"
            font-family="Arial"
            font-size="11">

            {esc(label)}

        </text>

    </g>
    """


def cert_card(
    x,
    y,
    title,
    issuer,
    year,
    accent
):

    return f"""
    <g>

        <rect
            x="{x}"
            y="{y}"
            width="535"
            height="82"
            rx="14"
            fill="{PANEL}"
            stroke="{BORDER}"
        />

        <rect
            x="{x}"
            y="{y}"
            width="4"
            height="82"
            rx="2"
            fill="{accent}"
        />

        <circle
            cx="{x + 27}"
            cy="{y + 27}"
            r="7"
            fill="{accent}"
        />

        <text
            x="{x + 48}"
            y="{y + 30}"
            fill="{TEXT}"
            font-family="Arial"
            font-size="13"
            font-weight="700">

            {esc(title)}

        </text>

        <text
            x="{x + 48}"
            y="{y + 54}"
            fill="{MUTED}"
            font-family="Arial"
            font-size="11">

            {esc(issuer)}

        </text>

        <text
            x="{x + 490}"
            y="{y + 30}"
            fill="{accent}"
            font-family="monospace"
            font-size="10"
            text-anchor="end">

            {esc(year)}

        </text>

        <text
            x="{x + 490}"
            y="{y + 56}"
            fill="{MUTED}"
            font-family="monospace"
            font-size="9"
            text-anchor="end">

            VERIFIED

        </text>

    </g>
    """


# ============================================================
# SVG START
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

    ACHIEVEMENTS // CREDENTIALS

</text>


<text
    x="40"
    y="78"
    fill="{TEXT}"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    PROOF OF WORK

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
<!-- METRICS -->
<!-- ===================================================== -->

"""

svg += metric_card(
    40,
    125,
    "550+",
    "LEETCODE PROBLEMS"
)

svg += metric_card(
    315,
    125,
    "1600",
    "PEAK CONTEST RATING"
)

svg += metric_card(
    590,
    125,
    "9.16",
    "CURRENT CGPA"
)

svg += metric_card(
    865,
    125,
    "150+",
    "CURATED DSA PROBLEMS"
)


# ============================================================
# CERTIFICATIONS HEADER
# ============================================================

svg += f"""

<text
    x="40"
    y="285"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="12"
    font-weight="700">

    CERTIFICATIONS

</text>


<text
    x="40"
    y="310"
    fill="{MUTED}"
    font-family="Arial"
    font-size="11">

    A growing collection of things actually completed.

</text>

"""


# ============================================================
# CERTIFICATIONS
# ============================================================

certs = [

    (
        "Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate",
        "Oracle",
        "2025",
        PURPLE
    ),

    (
        "Agentic AI Certified Foundations Associate",
        "Oracle",
        "2026",
        BLUE
    ),

    (
        "Node.js Intermediate",
        "HackerRank",
        "2026",
        "#22c55e"
    ),

    (
        "MERN Full-Stack Web Development",
        "30DaysCoding",
        "2026",
        PURPLE
    ),

    (
        "Introduction to Cloud Job Simulation",
        "Datacom / Forage",
        "2026",
        BLUE
    ),

    (
        "Agentic AI by OpenCode",
        "Udemy",
        "2026",
        "#a78bfa"
    ),

    (
        "Summer PEP 2026",
        "Coding Spoon",
        "2026",
        "#67e8f9"
    ),

]


left_x = 40
right_x = 625

start_y = 340
gap = 94


for i, cert in enumerate(certs):

    if i % 2 == 0:

        x = left_x

    else:

        x = right_x


    row = i // 2

    y = start_y + row * gap


    svg += cert_card(
        x,
        y,
        cert[0],
        cert[1],
        cert[2],
        cert[3]
    )


# ============================================================
# FOOTER
# ============================================================

footer_y = 340 + 4 * gap + 20


svg += f"""

<line
    x1="40"
    y1="{footer_y}"
    x2="1160"
    y2="{footer_y}"
    stroke="{BORDER}"
/>


<text
    x="40"
    y="{footer_y + 30}"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    LEARN • BUILD • SOLVE • SHIP

</text>


<text
    x="1160"
    y="{footer_y + 30}"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="10"
    text-anchor="end">

    SATYANSH_ACHARYA

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
print("       ACHIEVEMENTS SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()
print("Done.")
print()