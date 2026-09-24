from pathlib import Path
from html import escape


# ============================================================
# CONFIG
# ============================================================

OUTPUT = Path("assets/cs.svg")

WIDTH = 1200
HEIGHT = 700

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
# SVG HELPERS
# ============================================================

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
        {escape(value)}
    </text>
    """


def card(x, y, width, height, title, items):

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
            stroke-width="1.2"
        />

        <rect
            x="{x}"
            y="{y}"
            width="4"
            height="{height}"
            rx="2"
            fill="url(#accent)"
        />

    """

    svg += text(
        x + 24,
        y + 32,
        title,
        15,
        PURPLE,
        "700",
        "start",
        "monospace"
    )

    line_y = y + 47

    svg += f"""
    <line
        x1="{x + 24}"
        y1="{line_y}"
        x2="{x + width - 24}"
        y2="{line_y}"
        stroke="{BORDER}"
    />
    """

    item_y = y + 73

    for item in items:

        svg += f"""
        <circle
            cx="{x + 27}"
            cy="{item_y - 5}"
            r="3"
            fill="{BLUE}"
        />
        """

        svg += text(
            x + 40,
            item_y,
            item,
            12,
            TEXT,
            "500"
        )

        item_y += 27

    svg += """
    </g>
    """

    return svg


# ============================================================
# SVG START
# ============================================================

svg = f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<defs>

    <linearGradient
        id="background"
        x1="0"
        y1="0"
        x2="1"
        y2="1">

        <stop offset="0%" stop-color="#070914"/>
        <stop offset="55%" stop-color="#090b19"/>
        <stop offset="100%" stop-color="#12091d"/>

    </linearGradient>

    <linearGradient
        id="accent"
        x1="0"
        y1="0"
        x2="1"
        y2="0">

        <stop offset="0%" stop-color="{VIOLET}"/>
        <stop offset="50%" stop-color="{PURPLE}"/>
        <stop offset="100%" stop-color="{BLUE}"/>

    </linearGradient>

    <filter id="glow">

        <feGaussianBlur
            stdDeviation="5"
            result="blur"
        />

        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>

    </filter>

</defs>


<!-- ===================================================== -->
<!-- BACKGROUND -->
<!-- ===================================================== -->

<rect
    width="100%"
    height="100%"
    rx="28"
    fill="url(#background)"
/>


<!-- GRID -->

<g opacity="0.11">

'''

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

svg += """
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
"""

svg += text(
    57,
    41,
    "COMPUTER SCIENCE // CORE",
    13,
    MUTED,
    "600",
    "start",
    "monospace"
)

svg += text(
    40,
    78,
    "THE STUFF UNDER THE HOOD",
    27,
    TEXT,
    "700",
    "start",
    "monospace"
)

svg += """
<line
    x1="40"
    y1="100"
    x2="1160"
    y2="100"
    stroke="url(#accent)"
    stroke-width="2"
    opacity="0.7"
/>
"""


# ============================================================
# CENTRAL CORE
# ============================================================

CORE_X = 600
CORE_Y = 345

# Outer glow ring

svg += f"""
<circle
    cx="{CORE_X}"
    cy="{CORE_Y}"
    r="92"
    fill="none"
    stroke="{VIOLET}"
    stroke-width="1"
    opacity="0.18"
    filter="url(#glow)"
/>

<circle
    cx="{CORE_X}"
    cy="{CORE_Y}"
    r="70"
    fill="{PANEL_2}"
    stroke="url(#accent)"
    stroke-width="2"
/>

<circle
    cx="{CORE_X}"
    cy="{CORE_Y}"
    r="55"
    fill="{BG}"
    stroke="{PURPLE}"
    stroke-width="1"
    opacity="0.9"
/>
"""

svg += text(
    CORE_X,
    CORE_Y - 5,
    "CSE",
    25,
    TEXT,
    "800",
    "middle",
    "monospace"
)

svg += text(
    CORE_X,
    CORE_Y + 19,
    "CORE",
    10,
    PURPLE,
    "700",
    "middle",
    "monospace"
)


# ============================================================
# CONNECTIONS
# ============================================================

connections = [
    (260, 205, 545, 315),
    (940, 205, 655, 315),
    (260, 500, 545, 375),
    (940, 500, 655, 375),
]

for x1, y1, x2, y2 in connections:

    svg += f"""
    <line
        x1="{x1}"
        y1="{y1}"
        x2="{x2}"
        y2="{y2}"
        stroke="{VIOLET}"
        stroke-width="1.5"
        opacity="0.45"
    />

    <circle
        cx="{x2}"
        cy="{y2}"
        r="4"
        fill="{PURPLE}"
        opacity="0.9"
    />
    """


# ============================================================
# KNOWLEDGE DOMAINS
# ============================================================

svg += card(
    55,
    150,
    390,
    205,
    "ALGORITHMS & DATA STRUCTURES",
    [
        "Arrays / Strings",
        "Linked Lists / Stacks / Queues",
        "Trees / BST / Heaps",
        "Graphs / Traversal",
        "Dynamic Programming",
    ]
)

svg += card(
    755,
    150,
    390,
    205,
    "SYSTEMS",
    [
        "Operating Systems",
        "Computer Networks",
        "Computer Architecture",
        "Concurrency",
        "Memory & Processes",
    ]
)

svg += card(
    55,
    430,
    390,
    205,
    "SOFTWARE ENGINEERING",
    [
        "OOP",
        "Design Patterns",
        "Low-Level Design",
        "System Design",
        "Software Architecture",
    ]
)

svg += card(
    755,
    430,
    390,
    205,
    "DATABASES",
    [
        "DBMS",
        "SQL",
        "Transactions",
        "Indexing",
        "Normalization",
    ]
)


# ============================================================
# SMALL STATUS ELEMENTS
# ============================================================

svg += f"""
<g>

    <rect
        x="500"
        y="575"
        width="200"
        height="38"
        rx="19"
        fill="{PANEL_2}"
        stroke="{BORDER}"
    />

    <circle
        cx="523"
        cy="594"
        r="5"
        fill="#22c55e"
    />

"""

svg += text(
    540,
    599,
    "LEARNING / SOLVING",
    10,
    MUTED,
    "600",
    "start",
    "monospace"
)

svg += """
</g>
"""


# ============================================================
# FOOTER
# ============================================================

svg += f"""
<line
    x1="40"
    y1="{HEIGHT - 28}"
    x2="1160"
    y2="{HEIGHT - 28}"
    stroke="{BORDER}"
/>
"""

svg += text(
    40,
    HEIGHT - 10,
    "SATYANSH_ACHARYA // COMPUTER SCIENCE // ALWAYS LEARNING",
    10,
    MUTED,
    "400",
    "start",
    "monospace"
)


# ============================================================
# CLOSE SVG
# ============================================================

svg += """
</svg>
"""


# ============================================================
# WRITE
# ============================================================

OUTPUT.write_text(svg, encoding="utf-8")

print()
print("==============================================")
print("      COMPUTER SCIENCE SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()