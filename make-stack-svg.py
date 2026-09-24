import base64
from pathlib import Path
from html import escape


# ============================================================
# CONFIG
# ============================================================

ICON_DIR = Path("assets/icons")
OUTPUT = Path("assets/stack.svg")

WIDTH = 1200

BG = "#070914"
PANEL = "#0c0f20"
BORDER = "#202443"
TEXT = "#f4f1ff"
MUTED = "#858aa8"
PURPLE = "#c084fc"
VIOLET = "#8b5cf6"
BLUE = "#38bdf8"


# ============================================================
# TECH STACK
# ============================================================

SECTIONS = [
    (
        "FRONTEND",
        [
            ("html5", "HTML"),
            ("css3", "CSS"),
            ("javascript", "JavaScript"),
            ("typescript", "TypeScript"),
            ("react", "React"),
            ("nextjs", "Next.js"),
            ("react", "React Native"),
            ("tailwind", "Tailwind"),
            ("vite", "Vite"),
        ],
    ),

    (
        "BACKEND",
        [
            ("nodejs", "Node.js"),
            ("express", "Express"),
            ("nestjs", "NestJS"),
            ("java", "Java"),
            ("python", "Python"),
            ("graphql", "GraphQL"),
        ],
    ),

    (
        "DATABASES",
        [
            ("postgresql", "PostgreSQL"),
            ("mongodb", "MongoDB"),
            ("redis", "Redis"),
            ("prisma", "Prisma"),
        ],
    ),

    (
        "AI / ENGINEERING",
        [
            ("python", "Python"),
        ],
    ),

    (
        "TOOLS / INFRA",
        [
            ("git", "Git"),
            ("github", "GitHub"),
            ("linux", "Linux"),
            ("docker", "Docker"),
            ("kubernetes", "Kubernetes"),
            ("aws", "AWS"),
            ("figma", "Figma"),
            ("vscode", "VS Code"),
        ],
    ),

    (
        "CORE CS",
        [
            ("cpp", "C++"),
        ],
    ),
]


# ============================================================
# LOAD LOCAL ICON
# ============================================================

def load_icon(name):
    path = ICON_DIR / f"{name}.svg"

    if not path.exists():
        print(f"[!] Missing icon: {path}")
        return None

    data = path.read_bytes()

    return base64.b64encode(data).decode("utf-8")


# ============================================================
# SVG HELPERS
# ============================================================

def text(x, y, value, size=13, color=TEXT, weight="400",
         anchor="start", family="Arial"):

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


def tech_card(x, y, slug, name):

    icon = load_icon(slug)

    width = max(100, len(name) * 7 + 58)
    height = 72

    svg = f"""
    <g>

        <rect
            x="{x}"
            y="{y}"
            width="{width}"
            height="{height}"
            rx="14"
            fill="{PANEL}"
            stroke="{BORDER}"
            stroke-width="1"
        />

    """

    if icon:
        svg += f"""
        <image
            x="{x + 14}"
            y="{y + 14}"
            width="34"
            height="34"
            href="data:image/svg+xml;base64,{icon}"
        />
        """

    svg += text(
        x + width / 2,
        y + 59,
        name,
        size=10,
        color=TEXT,
        weight="600",
        anchor="middle",
    )

    svg += """
    </g>
    """

    return svg, width


# ============================================================
# HEIGHT
# ============================================================

ROW_HEIGHT = 112
HEADER_HEIGHT = 125
FOOTER_HEIGHT = 45

HEIGHT = (
    HEADER_HEIGHT
    + len(SECTIONS) * ROW_HEIGHT
    + FOOTER_HEIGHT
)


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


<!-- subtle grid -->

<g opacity="0.12">

'''

# vertical grid
for x in range(0, WIDTH + 1, 50):
    svg += f'''
    <line
        x1="{x}"
        y1="0"
        x2="{x}"
        y2="{HEIGHT}"
        stroke="#252846"
        stroke-width="1"
    />
    '''

# horizontal grid
for y in range(0, HEIGHT + 1, 50):
    svg += f'''
    <line
        x1="0"
        y1="{y}"
        x2="{WIDTH}"
        y2="{y}"
        stroke="#252846"
        stroke-width="1"
    />
    '''

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
    "TECH FIELDS // STACK",
    13,
    MUTED,
    "600",
    "start",
    "monospace",
)

svg += text(
    40,
    78,
    "WHAT I BUILD WITH",
    27,
    TEXT,
    "700",
    "start",
    "monospace",
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
# SECTIONS
# ============================================================

current_y = HEADER_HEIGHT

for section_name, technologies in SECTIONS:

    # Section title
    svg += text(
        40,
        current_y + 20,
        section_name,
        12,
        PURPLE,
        "700",
        "start",
        "monospace",
    )

    # little line
    svg += f"""
    <line
        x1="40"
        y1="{current_y + 30}"
        x2="145"
        y2="{current_y + 30}"
        stroke="{VIOLET}"
        stroke-width="2"
    />
    """

    card_x = 175
    card_y = current_y - 8

    for slug, name in technologies:

        card_svg, card_width = tech_card(
            card_x,
            card_y,
            slug,
            name
        )

        svg += card_svg

        card_x += card_width + 10

    current_y += ROW_HEIGHT


# ============================================================
# FOOTER
# ============================================================

svg += f"""
<line
    x1="40"
    y1="{HEIGHT - 30}"
    x2="1160"
    y2="{HEIGHT - 30}"
    stroke="{BORDER}"
/>
"""

svg += text(
    40,
    HEIGHT - 11,
    "SATYANSH_ACHARYA // STACK // BUILDING IN PROGRESS",
    10,
    MUTED,
    "400",
    "start",
    "monospace",
)

svg += """
</svg>
"""


# ============================================================
# WRITE FILE
# ============================================================

OUTPUT.write_text(svg, encoding="utf-8")

print()
print("==============================================")
print("        TECH STACK SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()