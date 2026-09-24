from pathlib import Path
from html import escape
import urllib.request
import re


OUTPUT = Path("assets/activity.svg")

WIDTH = 1200
HEIGHT = 430

BG = "#070914"
PANEL = "#0c0f20"
BORDER = "#24284a"

TEXT = "#f4f1ff"
MUTED = "#858aa8"

PURPLE = "#c084fc"
VIOLET = "#8b5cf6"
BLUE = "#38bdf8"


USERNAME = "Spade-2006"


def fetch(url):

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    with urllib.request.urlopen(
        request,
        timeout=20
    ) as response:

        return response.read().decode(
            "utf-8",
            errors="ignore"
        )


def esc(value):
    return escape(str(value))


# ============================================================
# FETCH CONTRIBUTION DATA
# ============================================================

print()
print("Fetching GitHub activity...")
print()

url = (
    f"https://github.com/users/"
    f"{USERNAME}/contributions"
)

html = fetch(url)


matches = re.findall(
    r'<td[^>]*data-date="([^"]+)"[^>]*'
    r'data-level="([^"]+)"[^>]*>',
    html
)


cells = []

for date, level in matches:

    cells.append(
        (
            date,
            int(level)
        )
    )


print(
    f"Found {len(cells)} activity cells."
)


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

    ACTIVITY // RECENT BUILD CYCLE

</text>


<text
    x="40"
    y="78"
    fill="{TEXT}"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    CODE NEVER REALLY SLEEPS

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


<!-- ACTIVITY PANEL -->

<rect
    x="40"
    y="125"
    width="1120"
    height="210"
    rx="18"
    fill="{PANEL}"
    stroke="{BORDER}"
/>


<text
    x="65"
    y="157"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="11"
    font-weight="700">

    CONTRIBUTION FLOW

</text>


<!-- MATRIX -->

<g>
"""


# ============================================================
# MATRIX
# ============================================================

start_x = 65
start_y = 185

cell_size = 12
gap = 4

rows = 7
columns = 72


for i, (date, level) in enumerate(cells):

    column = i // rows
    row = i % rows

    if column >= columns:
        break

    x = start_x + column * (
        cell_size + gap
    )

    y = start_y + row * (
        cell_size + gap
    )


    if level == 0:

        fill = "#111426"

    elif level == 1:

        fill = "#3b245c"

    elif level == 2:

        fill = "#663b8f"

    elif level == 3:

        fill = "#995bd1"

    else:

        fill = "#c084fc"


    svg += f"""
    <rect
        x="{x}"
        y="{y}"
        width="{cell_size}"
        height="{cell_size}"
        rx="3"
        fill="{fill}">

        <title>{esc(date)}</title>

    </rect>
    """


svg += f"""
</g>


<!-- LEGEND -->

<text
    x="65"
    y="310"
    fill="{MUTED}"
    font-family="monospace"
    font-size="9">

    LESS

</text>


<rect
    x="105"
    y="301"
    width="11"
    height="11"
    rx="3"
    fill="#111426"
/>


<rect
    x="122"
    y="301"
    width="11"
    height="11"
    rx="3"
    fill="#3b245c"
/>


<rect
    x="139"
    y="301"
    width="11"
    height="11"
    rx="3"
    fill="#663b8f"
/>


<rect
    x="156"
    y="301"
    width="11"
    height="11"
    rx="3"
    fill="#995bd1"
/>


<rect
    x="173"
    y="301"
    width="11"
    height="11"
    rx="3"
    fill="#c084fc"
/>


<text
    x="193"
    y="310"
    fill="{MUTED}"
    font-family="monospace"
    font-size="9">

    MORE

</text>


<!-- FOOTER -->

<line
    x1="40"
    y1="365"
    x2="1160"
    y2="365"
    stroke="{BORDER}"
/>


<text
    x="40"
    y="397"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    BUILDING • COMMITTING • LEARNING • REPEATING

</text>


<text
    x="1160"
    y="397"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="10"
    text-anchor="end">

    @{USERNAME}

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
print("          ACTIVITY SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()
print("Done.")