from pathlib import Path
import base64
import html


# ============================================================
# CONFIG
# ============================================================

ROOT = Path(__file__).resolve().parent

ICONS_DIR = ROOT / "assets" / "icons"
OUTPUT = ROOT / "assets" / "stack.svg"

WIDTH = 1280

BG = "#080b18"
CARD = "#0d1224"
BORDER = "#252d50"
TEXT = "#f4f4f5"
MUTED = "#8b93b7"
PURPLE = "#a855f7"
PURPLE_LIGHT = "#c084fc"


# ============================================================
# LAYOUT
# ============================================================

LABEL_X = 32
CARDS_X = 175

CARD_W = 108
CARD_H = 78

GAP_X = 10
GAP_Y = 12

# Maximum cards per row.
#
# Frontend = 12 items
#
# Row 1:
# HTML | CSS | JavaScript | TypeScript | React | Next.js
#
# Row 2:
# React Native | Tailwind | Vite | Three.js | Phaser | Tiled
#
MAX_COLUMNS = 8


# ============================================================
# LOCAL ICON MAP
# ============================================================
#
# These point to files inside:
#
# assets/icons/
#
# NO INTERNET REQUESTS.
# NO CDN.
#

ICON_MAP = {

    # --------------------------------------------------------
    # FRONTEND
    # --------------------------------------------------------

    "HTML": "html.svg",
    "CSS": "css3.svg",
    "JavaScript": "javascript.svg",
    "TypeScript": "typescript.svg",
    "React": "react.svg",
    "Next.js": "nextjs.svg",
    "React Native": "react.svg",
    "Tailwind": "tailwind.svg",
    "Vite": "vite.svg",

    # If these exist in your icons folder, they will be used.
    # If not, the script automatically falls back to text.

    "Three.js": "threejs.svg",
    "Phaser": "phaser.svg",
    "Tiled": "tiled.svg",


    # --------------------------------------------------------
    # BACKEND
    # --------------------------------------------------------

    "Node.js": "nodejs.svg",
    "Express": "express.svg",
    "NestJS": "nestjs.svg",
    "REST": None,
    "GraphQL": "graphql.svg",
    "Java": "java.svg",
    "Python": "python.svg",


    # --------------------------------------------------------
    # DATABASES
    # --------------------------------------------------------

    "PostgreSQL": "postgresql.svg",
    "MongoDB": "mongodb.svg",
    "Mongoose": "mongodb.svg",
    "Prisma": "prisma.svg",
    "Redis": "redis.svg",


    # --------------------------------------------------------
    # AI
    # --------------------------------------------------------

    "Python": "python.svg",
    "OpenAI": None,
    "RAG": None,
    "Agentic AI": None,
    "Hugging Face": None,
    "LangChain": None,


    # --------------------------------------------------------
    # OTHER TOOLS
    # --------------------------------------------------------

    "Git": "git.svg",
    "GitHub": "github.svg",
    "Linux": "linux.svg",
    "Docker": "docker.svg",
    "Kubernetes": "kubernetes.svg",
    "AWS": "aws.svg",
    "VS Code": None,
    "Figma": "figma.svg",
    "GitHub Actions": None,


    # --------------------------------------------------------
    # CORE CS
    # --------------------------------------------------------

    "C++": "cpp.svg",
    "DSA": None,
    "OOP": None,
    "DBMS": None,
    "OS": "linux.svg",
    "CN": None,
    "Computer Architecture": None,
    "LLD": None,
    "System Design": None,
}


# ============================================================
# SECTIONS
# ============================================================

SECTIONS = [

    (
        "FRONTEND",
        [
            "HTML",
            "CSS",
            "JavaScript",
            "TypeScript",
            "React",
            "Next.js",
            "React Native",
            "Tailwind",
            "Vite",
            "Three.js",
            "Phaser",
            "Tiled",
        ],
    ),

    (
        "BACKEND",
        [
            "Node.js",
            "Express",
            "NestJS",
            "REST",
            "GraphQL",
            "Java",
            "Python",
        ],
    ),

    (
        "DATABASES",
        [
            "PostgreSQL",
            "MongoDB",
            "Mongoose",
            "Prisma",
            "Redis",
        ],
    ),

    (
        "AI",
        [
            "Python",
            "OpenAI",
            "RAG",
            "Agentic AI",
            "Hugging Face",
            "LangChain",
        ],
    ),

    (
        "OTHER TOOLS",
        [
            "Git",
            "GitHub",
            "Linux",
            "Docker",
            "Kubernetes",
            "AWS",
            "VS Code",
            "Figma",
            "GitHub Actions",
        ],
    ),

    (
        "CORE CS",
        [
            "C++",
            "DSA",
            "OOP",
            "DBMS",
            "OS",
            "CN",
            "Computer Architecture",
            "LLD",
            "System Design",
        ],
    ),
]


# ============================================================
# HELPERS
# ============================================================

def esc(value):
    return html.escape(str(value))


def local_icon_path(filename):
    if not filename:
        return None

    path = ICONS_DIR / filename

    if path.exists():
        return path

    return None


def find_icon(name):
    """
    Finds the local SVG icon.

    First uses ICON_MAP.
    Then performs a small fallback search based on the name.
    """

    mapped = ICON_MAP.get(name)

    if mapped:
        path = local_icon_path(mapped)

        if path:
            return path

    # --------------------------------------------------------
    # Fallback filename matching
    # --------------------------------------------------------

    normalized = (
        name.lower()
        .replace(".", "")
        .replace(" ", "")
        .replace("-", "")
        .replace("/", "")
    )

    if ICONS_DIR.exists():

        for path in ICONS_DIR.glob("*.svg"):

            filename = (
                path.stem.lower()
                .replace(".", "")
                .replace(" ", "")
                .replace("-", "")
                .replace("/", "")
            )

            if filename == normalized:
                return path

    return None


def svg_to_data_uri(path):
    """
    Reads an existing local SVG and embeds it directly
    into the generated stack.svg.
    """

    try:

        data = path.read_bytes()

        encoded = base64.b64encode(data).decode("ascii")

        return f"data:image/svg+xml;base64,{encoded}"

    except Exception as error:

        print(
            f"[WARN] Could not read icon: "
            f"{path.name}"
        )

        print(f"       {error}")

        return None


def font_size_for(name):

    if len(name) >= 19:
        return 8

    if len(name) >= 15:
        return 9

    if len(name) >= 11:
        return 10

    return 11


# ============================================================
# ICON RENDER
# ============================================================

def render_icon(name, x, y):

    SIZE = 34

    icon_path = find_icon(name)

    # --------------------------------------------------------
    # Real local icon
    # --------------------------------------------------------

    if icon_path:

        uri = svg_to_data_uri(icon_path)

        if uri:

            return f"""
            <image
                href="{uri}"
                x="{x}"
                y="{y}"
                width="{SIZE}"
                height="{SIZE}"
                preserveAspectRatio="xMidYMid meet"
            />
            """

    # --------------------------------------------------------
    # Fallback for technologies where no local icon exists
    # --------------------------------------------------------

    fallback_labels = {
        "HTML": "HTML",
        "REST": "API",
        "OpenAI": "AI",
        "RAG": "RAG",
        "Agentic AI": "AI",
        "Hugging Face": "HF",
        "LangChain": "LC",
        "VS Code": "VS",
        "GitHub Actions": "CI",
        "DSA": "DSA",
        "OOP": "OOP",
        "DBMS": "DB",
        "CN": "CN",
        "Computer Architecture": "CPU",
        "LLD": "LLD",
        "System Design": "SYS",
        "Three.js": "3D",
        "Phaser": "PH",
        "Tiled": "TL",
    }

    label = fallback_labels.get(
        name,
        name[:3].upper()
    )

    return f"""
    <rect
        x="{x}"
        y="{y}"
        width="34"
        height="34"
        rx="9"
        fill="#151b32"
        stroke="{PURPLE}"
        stroke-width="1"
    />

    <text
        x="{x + 17}"
        y="{y + 22}"
        text-anchor="middle"
        font-family="monospace"
        font-size="9"
        font-weight="800"
        fill="{PURPLE_LIGHT}"
    >{esc(label)}</text>
    """


# ============================================================
# CARD
# ============================================================

def render_card(name, x, y):

    icon_x = x + (CARD_W - 34) / 2
    icon_y = y + 12

    font_size = font_size_for(name)

    return f"""
    <g>

        <rect
            x="{x}"
            y="{y}"
            width="{CARD_W}"
            height="{CARD_H}"
            rx="16"
            fill="{CARD}"
            stroke="{BORDER}"
            stroke-width="1"
        />

        {render_icon(
            name,
            icon_x,
            icon_y
        )}

        <text
            x="{x + CARD_W / 2}"
            y="{y + 63}"
            text-anchor="middle"
            font-family="monospace"
            font-size="{font_size}"
            font-weight="700"
            fill="{TEXT}"
        >{esc(name)}</text>

    </g>
    """


# ============================================================
# SECTION RENDER
# ============================================================

def render_section(title, items, start_y):

    parts = []

    # --------------------------------------------------------
    # Calculate rows
    # --------------------------------------------------------

    row_count = (
        len(items) + MAX_COLUMNS - 1
    ) // MAX_COLUMNS

    # --------------------------------------------------------
    # Section title
    # --------------------------------------------------------

    parts.append(
        f"""
        <text
            x="{LABEL_X}"
            y="{start_y + 25}"
            font-family="monospace"
            font-size="13"
            font-weight="700"
            fill="{PURPLE_LIGHT}"
        >{esc(title)}</text>

        <line
            x1="{LABEL_X}"
            y1="{start_y + 38}"
            x2="{LABEL_X + 112}"
            y2="{start_y + 38}"
            stroke="{PURPLE}"
            stroke-width="2"
        />
        """
    )

    # --------------------------------------------------------
    # Cards
    # --------------------------------------------------------

    for index, name in enumerate(items):

        # THIS is the wrapping fix.

        row = index // MAX_COLUMNS
        column = index % MAX_COLUMNS

        x = (
            CARDS_X
            + column * (CARD_W + GAP_X)
        )

        y = (
            start_y
            + row * (CARD_H + GAP_Y)
        )

        parts.append(
            render_card(
                name,
                x,
                y
            )
        )

    # --------------------------------------------------------
    # Dynamic section height
    # --------------------------------------------------------

    cards_height = (
        row_count * CARD_H
        + (row_count - 1) * GAP_Y
    )

    section_height = max(
        cards_height,
        78
    )

    return (
        "\n".join(parts),
        section_height
    )


# ============================================================
# SVG START
# ============================================================

svg_parts = []

svg_parts.append(
    f"""
    <defs>

        <pattern
            id="grid"
            width="32"
            height="32"
            patternUnits="userSpaceOnUse"
        >
            <path
                d="M 32 0 L 0 0 0 32"
                fill="none"
                stroke="#151b31"
                stroke-width="1"
                opacity="0.55"
            />
        </pattern>

        <linearGradient
            id="background"
            x1="0"
            y1="0"
            x2="1"
            y2="1"
        >
            <stop
                offset="0%"
                stop-color="#0a0e20"
            />

            <stop
                offset="100%"
                stop-color="#080b18"
            />
        </linearGradient>

    </defs>

    <!-- Background -->

    <rect
        x="0"
        y="0"
        width="{WIDTH}"
        height="100%"
        fill="{BG}"
    />

    <rect
        x="0"
        y="0"
        width="{WIDTH}"
        height="100%"
        fill="url(#grid)"
    />

    <rect
        x="0"
        y="0"
        width="{WIDTH}"
        height="100%"
        fill="url(#background)"
        opacity="0.65"
    />

    <!-- Header -->

    <text
        x="32"
        y="30"
        font-family="monospace"
        font-size="25"
        font-weight="800"
        fill="{TEXT}"
    >WHAT I BUILD WITH</text>
    """
)


# ============================================================
# RENDER SECTIONS
# ============================================================

current_y = 62

for section_index, (title, items) in enumerate(SECTIONS):

    section_svg, section_height = render_section(
        title,
        items,
        current_y
    )

    svg_parts.append(section_svg)

    # --------------------------------------------------------
    # IMPORTANT:
    #
    # Next section automatically moves down.
    #
    # So Frontend can become 2 rows without overlapping
    # Backend.
    # --------------------------------------------------------

    current_y += section_height + 42

    # Divider

    if section_index < len(SECTIONS) - 1:

        svg_parts.append(
            f"""
            <line
                x1="32"
                y1="{current_y - 20}"
                x2="{WIDTH - 32}"
                y2="{current_y - 20}"
                stroke="#171d35"
                stroke-width="1"
            />
            """
        )


# ============================================================
# FOOTER
# ============================================================

current_y += 5

svg_parts.append(
    f"""
    <text
        x="32"
        y="{current_y}"
        font-family="monospace"
        font-size="10"
        fill="{MUTED}"
    >BUILDING • LEARNING • SHIPPING</text>

    <text
        x="{WIDTH - 32}"
        y="{current_y}"
        text-anchor="end"
        font-family="monospace"
        font-size="10"
        fill="{PURPLE_LIGHT}"
    >@Spade-2006</text>
    """
)


# ============================================================
# FINAL SVG
# ============================================================

HEIGHT = current_y + 35

final_svg = f"""<?xml version="1.0" encoding="UTF-8"?>

<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
>

{''.join(svg_parts)}

</svg>
"""


# ============================================================
# WRITE
# ============================================================

OUTPUT.write_text(
    final_svg,
    encoding="utf-8"
)


# ============================================================
# RESULT
# ============================================================

print()
print("==============================================")
print("       STACK SVG GENERATED SUCCESSFULLY")
print("==============================================")
print()
print(f"Output : {OUTPUT}")
print(f"Width  : {WIDTH}px")
print(f"Height : {HEIGHT}px")
print()
print("Icon source:")
print(f"  {ICONS_DIR}")
print()
print("Frontend layout:")
print("  Row 1 → HTML | CSS | JavaScript | TypeScript | React | Next.js | React Native | Tailwind")
print("  Row 2 → Vite | Three.js | Phaser | Tiled")
print()
print("All sections automatically reposition.")
print()