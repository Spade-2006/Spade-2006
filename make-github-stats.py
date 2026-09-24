import json
import re
import urllib.request
from pathlib import Path
from collections import Counter


# ============================================================
# CONFIG
# ============================================================

USERNAME = "Spade-2006"

OUTPUT = Path("assets/github-stats.svg")

WIDTH = 1200
HEIGHT = 620

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
# HTTP HELPER
# ============================================================

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


# ============================================================
# FETCH PROFILE
# ============================================================

print()
print("Fetching GitHub profile...")
print()

profile_url = f"https://github.com/{USERNAME}"

html = fetch(profile_url)

print("Profile loaded.")


# ============================================================
# PUBLIC REPOSITORIES
# ============================================================

repo_matches = re.findall(
    rf'href="/{re.escape(USERNAME)}/([^"/]+)"',
    html
)

repositories = set()

for repo in repo_matches:

    if repo not in [
        "followers",
        "following",
        "repositories",
        "stars",
        "projects"
    ]:

        repositories.add(repo)


public_repos = len(repositories)


# ============================================================
# FOLLOWERS
# ============================================================

followers_match = re.search(
    r'href="/Spade-2006\?tab=followers"[^>]*>.*?([0-9][0-9,]*)',
    html,
    re.S
)

if followers_match:

    followers = int(
        followers_match.group(1).replace(",", "")
    )

else:

    followers = 0


# ============================================================
# FOLLOWING
# ============================================================

following_match = re.search(
    r'href="/Spade-2006\?tab=following"[^>]*>.*?([0-9][0-9,]*)',
    html,
    re.S
)

if following_match:

    following = int(
        following_match.group(1).replace(",", "")
    )

else:

    following = 0


# ============================================================
# ACCOUNT CREATION
# ============================================================

account_match = re.search(
    r'Joined\s+([A-Za-z]+\s+\d{4})',
    html
)

if account_match:

    account_created = account_match.group(1)

else:

    account_created = "GitHub"


# ============================================================
# REPOSITORY PAGES
# ============================================================

print(
    f"Found approximately {public_repos} repositories."
)

print("Scanning repository languages...")


languages = Counter()

stars = 0

forks = 0


for repo in sorted(repositories):

    try:

        repo_url = (
            f"https://github.com/"
            f"{USERNAME}/{repo}"
        )

        repo_html = fetch(repo_url)


        # ----------------------------------------------------
        # LANGUAGE
        # ----------------------------------------------------

        language_match = re.search(
            r'aria-label="([^"]+) percentage"',
            repo_html
        )

        if language_match:

            language_text = (
                language_match.group(1)
            )

            languages[
                language_text
            ] += 1


        # ----------------------------------------------------
        # STARS
        # ----------------------------------------------------

        star_match = re.search(
            r'href="/[^"]+/stargazers"[^>]*>\s*([^<]*)',
            repo_html
        )

        if star_match:

            value = (
                star_match.group(1)
                .strip()
                .replace(",", "")
            )

            if value.isdigit():

                stars += int(value)


        # ----------------------------------------------------
        # FORKS
        # ----------------------------------------------------

        fork_match = re.search(
            r'href="/[^"]+/forks"[^>]*>\s*([^<]*)',
            repo_html
        )

        if fork_match:

            value = (
                fork_match.group(1)
                .strip()
                .replace(",", "")
            )

            if value.isdigit():

                forks += int(value)


    except Exception:

        continue


# ============================================================
# CONTRIBUTION ACTIVITY
# ============================================================

print("Fetching contribution activity...")


try:

    contribution_url = (
        f"https://github.com/users/"
        f"{USERNAME}/contributions"
    )

    contribution_html = fetch(
        contribution_url
    )


    contribution_matches = re.findall(
        r'<td[^>]*data-level="(\d+)"',
        contribution_html
    )


    contribution_levels = [
        int(level)
        for level in contribution_matches
    ]


    contribution_total = sum(
        contribution_levels
    )


    contribution_cells = len(
        contribution_levels
    )


except Exception:

    contribution_total = 0

    contribution_cells = 0


print(
    f"Contribution cells: "
    f"{contribution_cells}"
)


# ============================================================
# HELPERS
# ============================================================

def esc(value):

    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


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


def stat_card(
    x,
    y,
    width,
    title,
    value,
    subtitle
):

    return f"""

    <g>

        <rect
            x="{x}"
            y="{y}"
            width="{width}"
            height="105"
            rx="16"
            fill="{PANEL}"
            stroke="{BORDER}"
        />

        <text
            x="{x + 20}"
            y="{y + 27}"
            fill="{MUTED}"
            font-family="monospace"
            font-size="10"
            font-weight="600">

            {esc(title)}

        </text>

        <text
            x="{x + 20}"
            y="{y + 64}"
            fill="{TEXT}"
            font-family="monospace"
            font-size="25"
            font-weight="700">

            {esc(value)}

        </text>

        <text
            x="{x + 20}"
            y="{y + 87}"
            fill="{MUTED}"
            font-family="Arial"
            font-size="10">

            {esc(subtitle)}

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

for x in range(
    0,
    WIDTH + 1,
    50
):

    svg += f"""
    <line
        x1="{x}"
        y1="0"
        x2="{x}"
        y2="{HEIGHT}"
        stroke="#252846"
    />
    """


for y in range(
    0,
    HEIGHT + 1,
    50
):

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

    GITHUB // DEVELOPER TELEMETRY

</text>


<text
    x="40"
    y="78"
    fill="{TEXT}"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    BUILDING IN PUBLIC

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


<!-- STAT CARDS -->

"""

card_width = 255

svg += stat_card(
    40,
    125,
    card_width,
    "PUBLIC REPOSITORIES",
    public_repos,
    "projects currently public"
)

svg += stat_card(
    315,
    125,
    card_width,
    "FOLLOWERS",
    followers,
    "developers following"
)

svg += stat_card(
    590,
    125,
    card_width,
    "TOTAL STARS",
    stars,
    "stars across repositories"
)

svg += stat_card(
    865,
    125,
    card_width,
    "FORKS",
    forks,
    "repository forks"
)


# ============================================================
# CONTRIBUTION PANEL
# ============================================================

svg += f"""

<rect
    x="40"
    y="260"
    width="540"
    height="265"
    rx="18"
    fill="{PANEL}"
    stroke="{BORDER}"
/>


<text
    x="65"
    y="295"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="11"
    font-weight="700">

    CONTRIBUTION ACTIVITY

</text>


<text
    x="65"
    y="335"
    fill="{TEXT}"
    font-family="monospace"
    font-size="30"
    font-weight="700">

    {contribution_total}

</text>


<text
    x="65"
    y="357"
    fill="{MUTED}"
    font-family="Arial"
    font-size="11">

    contribution intensity

</text>


<line
    x1="65"
    y1="382"
    x2="555"
    y2="382"
    stroke="{BORDER}"
/>


<text
    x="65"
    y="414"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    ACCOUNT

</text>


<text
    x="160"
    y="414"
    fill="{TEXT}"
    font-family="Arial"
    font-size="11">

    {account_created}

</text>


<text
    x="65"
    y="443"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    FOLLOWING

</text>


<text
    x="160"
    y="443"
    fill="{TEXT}"
    font-family="Arial"
    font-size="11">

    {following}

</text>


<text
    x="65"
    y="472"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    PROFILE

</text>


<text
    x="160"
    y="472"
    fill="{BLUE}"
    font-family="monospace"
    font-size="10">

    github.com/{USERNAME}

</text>



<!-- LANGUAGE PANEL -->

<rect
    x="600"
    y="260"
    width="560"
    height="265"
    rx="18"
    fill="{PANEL}"
    stroke="{BORDER}"
/>


<text
    x="625"
    y="295"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="11"
    font-weight="700">

    LANGUAGE DISTRIBUTION

</text>

"""


# ============================================================
# LANGUAGE BARS
# ============================================================

language_order = languages.most_common(5)

if language_order:

    total_language_repos = sum(
        count
        for _, count in language_order
    )

    language_colors = [
        PURPLE,
        BLUE,
        VIOLET,
        "#a78bfa",
        "#67e8f9"
    ]

    y = 335

    for index, (
        language,
        count
    ) in enumerate(language_order):

        percentage = (
            count /
            total_language_repos *
            100
        )

        bar_width = max(
            20,
            int(
                percentage *
                3.2
            )
        )

        color = language_colors[
            index %
            len(language_colors)
        ]


        svg += f"""

        <text
            x="625"
            y="{y}"
            fill="{TEXT}"
            font-family="Arial"
            font-size="12"
            font-weight="600">

            {esc(language)}

        </text>


        <rect
            x="625"
            y="{y + 10}"
            width="320"
            height="8"
            rx="4"
            fill="#15182b"
        />


        <rect
            x="625"
            y="{y + 10}"
            width="{bar_width}"
            height="8"
            rx="4"
            fill="{color}"
        />


        <text
            x="965"
            y="{y + 17}"
            fill="{MUTED}"
            font-family="monospace"
            font-size="10">

            {percentage:.0f}%

        </text>

        """

        y += 43

else:

    svg += text(
        625,
        340,
        "Language data unavailable",
        12,
        MUTED
    )


# ============================================================
# FOOTER
# ============================================================

svg += f"""

<line
    x1="40"
    y1="555"
    x2="1160"
    y2="555"
    stroke="{BORDER}"
/>


<text
    x="40"
    y="585"
    fill="{MUTED}"
    font-family="monospace"
    font-size="10">

    CODE • SHIP • LEARN • REPEAT

</text>


<text
    x="1160"
    y="585"
    fill="{PURPLE}"
    font-family="monospace"
    font-size="10"
    text-anchor="end">

    {USERNAME}

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
print("        GITHUB STATS SVG GENERATED")
print("==============================================")
print()
print(f"Output: {OUTPUT}")
print()
print("Done.")
print()