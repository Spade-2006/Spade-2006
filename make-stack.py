import base64
import urllib.request
from pathlib import Path
from html import escape


OUT = Path("assets/stack.svg")

# Simple Icons CDN
CDN = "https://cdn.simpleicons.org/{}"

# ------------------------------------------------------------
# TECH STACK
# ------------------------------------------------------------

SECTIONS = {
    "FRONTEND": [
        ("html5", "HTML"),
        ("css", "CSS"),
        ("javascript", "JavaScript"),
        ("typescript", "TypeScript"),
        ("react", "React"),
        ("nextdotjs", "Next.js"),
        ("react", "React Native"),
        ("tailwindcss", "Tailwind"),
        ("vite", "Vite"),
        ("threedotjs", "Three.js"),
        ("phaser", "Phaser"),
        ("tiled", "Tiled"),
    ],

    "BACKEND": [
        ("nodedotjs", "Node.js"),
        ("express", "Express"),
        ("nestjs", "NestJS"),
        ("java", "Java"),
        ("python", "Python"),
        ("graphql", "GraphQL"),
    ],

    "DATABASES": [
        ("postgresql", "PostgreSQL"),
        ("mongodb", "MongoDB"),
        ("redis", "Redis"),
        ("prisma", "Prisma"),
        ("mongoose", "Mongoose"),
    ],

    "AI / ENGINEERING": [
        ("python", "Python"),
        ("openai", "OpenAI"),
        ("huggingface", "Hugging Face"),
        ("langchain", "LangChain"),
    ],

    "TOOLS / INFRA": [
        ("git", "Git"),
        ("github", "GitHub"),
        ("linux", "Linux"),
        ("docker", "Docker"),
        ("kubernetes", "Kubernetes"),
        ("amazonwebservices", "AWS"),
        ("figma", "Figma"),
        ("githubactions", "GitHub Actions"),
        ("visualstudiocode", "VS Code"),
    ],

    "CORE CS": [
        ("cplusplus", "C++"),
        ("algorithm", "DSA"),
        ("cplusplus", "OOP"),
        ("postgresql", "DBMS"),
        ("linux", "OS"),
        ("network", "CN"),
        ("architecture", "Computer Architecture"),
        ("design", "LLD"),
        ("systemdesign", "System Design"),
    ],
}


# ------------------------------------------------------------
# COLORS
# ------------------------------------------------------------

BG = "#070914"
PANEL = "#0b0d1d"
GRID = "#171a32"
TEXT = "#f4f1ff"
MUTED = "#8d91ad"
PURPLE = "#c084fc"
VIOLET = "#8b5cf6"
BLUE = "#38bdf8"


# ------------------------------------------------------------
# DOWNLOAD + EMBED ICON
# ------------------------------------------------------------

def get_icon(slug):
    url = CDN.format(slug)

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()

        return base64.b64encode(data).decode()

    except Exception:
        print(f"[!] Could not load icon: {slug}")
        return None


# ------------------------------------------------------------
# SVG
# ------------------------------------------------------------

WIDTH = 1200
ROW_HEIGHT = 118
TOP = 105

section_count = len(SECTIONS)
HEIGHT = TOP + section_count * ROW_HEIGHT + 35

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}"
     height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

<defs>

    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#070914"/>
        <stop offset="55%" stop-color="#0a0b1b"/>
        <stop offset="100%" stop-color="#11091e"/>
    </linearGradient>

    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="{VIOLET}"/>
        <stop offset="50%" stop-color="{PURPLE}"/>
        <stop offset="100%" stop-color="{BLUE}"/>
    </linearGradient>

    <filter id="glow">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>

</defs>

<!-- BACKGROUND -->

<rect width="100%" height="100%" rx="28" fill="url(#bg)"/>

<!-- subtle grid -->

<g opacity="0.16">
'''

# Grid
for x in range(0, WIDTH + 1, 50):
    svg += f'<line x1="{x}" y1="0" x2="{x}" y2="{HEIGHT}" stroke="{GRID}" />'

for y in range(0, HEIGHT + 1, 50):
    svg += f'<line x1="0" y1="{y}" x2="{WIDTH}" y2="{y}" stroke="{GRID}" />'

svg += '''
</g>

<!-- HEADER -->

<circle cx="38" cy="35" r="6" fill="#22c55e"/>
<text x="55" y="41"
      fill="#9ca3af"
      font-family="monospace"
      font-size="14">
    TECH FIELDS // CURRENT STACK
</text>

<text x="40" y="78"
      fill="#ffffff"
      font-family="monospace"
      font-size="28"
      font-weight="700">
    THE STUFF I ACTUALLY BUILD WITH
</text>

<line x1="40" y1="91" x2="1160" y2="91"
      stroke="url(#accent)"
      stroke-width="2"
      opacity="0.7"/>

'''

# ------------------------------------------------------------
# SECTIONS
# ------------------------------------------------------------

y = TOP

for section_name, technologies in SECTIONS.items():

    # Section label
    svg += f'''
    <text x="40" y="{y}"
          fill="{PURPLE}"
          font-family="monospace"
          font-size="13"
          font-weight="700">
        {escape(section_name)}
    </text>
    '''

    # Small accent line
    svg += f'''
    <line x1="40" y1="{y + 9}"
          x2="145" y2="{y + 9}"
          stroke="{VIOLET}"
          stroke-width="2"
          opacity="0.7"/>
    '''

    # Technology cards
    card_x = 175
    card_y = y - 25

    for slug, name in technologies:

        icon = get_icon(slug)

        card_width = max(92, len(name) * 7 + 50)

        # Keep cards inside SVG
        if card_x + card_width > WIDTH - 35:
            card_x = 175
            card_y += 68

        svg += f'''
        <g>

            <rect
                x="{card_x}"
                y="{card_y}"
                width="{card_width}"
                height="54"
                rx="12"
                fill="{PANEL}"
                stroke="{GRID}"
                stroke-width="1"
            />
        '''

        if icon:

            svg += f'''
            <image
                x="{card_x + 12}"
                y="{card_y + 12}"
                width="30"
                height="30"
                href="data:image/svg+xml;base64,{icon}"
            />
            '''

        svg += f'''
            <text
                x="{card_x + 50}"
                y="{card_y + 33}"
                fill="{TEXT}"
                font-family="Arial, sans-serif"
                font-size="12"
                font-weight="600">
                {escape(name)}
            </text>

        </g>
        '''

        card_x += card_width + 10

    y += ROW_HEIGHT


# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

svg += f'''
<line x1="40" y1="{HEIGHT - 25}"
      x2="1160" y2="{HEIGHT - 25}"
      stroke="{GRID}"/>

<text x="40" y="{HEIGHT - 7}"
      fill="{MUTED}"
      font-family="monospace"
      font-size="11">
    SATYANSH_ACHARYA // STACK.md // BUILDING IN PROGRESS
</text>

</svg>
'''


OUT.write_text(svg, encoding="utf-8")

print()
print("✓ assets/stack.svg generated successfully")
print()
