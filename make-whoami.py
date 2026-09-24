import base64
from pathlib import Path

photo = Path("assets/satyansh.jpg")
output = Path("assets/whoami.svg")

photo_b64 = base64.b64encode(photo.read_bytes()).decode("utf-8")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="1200"
height="520"
viewBox="0 0 1200 520">

<defs>

<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#080612"/>
    <stop offset=".5" stop-color="#10091f"/>
    <stop offset="1" stop-color="#070914"/>
</linearGradient>

<linearGradient id="accent" x1="0" x2="1">
    <stop stop-color="#7c3aed"/>
    <stop offset=".5" stop-color="#22d3ee"/>
    <stop offset="1" stop-color="#a855f7"/>
</linearGradient>

<filter id="glow">
    <feGaussianBlur stdDeviation="5" result="blur"/>
    <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
    </feMerge>
</filter>

<clipPath id="photoClip">
    <rect x="75" y="118" width="300" height="340" rx="24"/>
</clipPath>

<style>

.title {{
    font-family:Arial,sans-serif;
    font-size:34px;
    font-weight:800;
    fill:#f8fafc;
    letter-spacing:2px;
}}

.role {{
    font-family:Arial,sans-serif;
    font-size:15px;
    fill:#a78bfa;
    letter-spacing:1px;
}}

.label {{
    font-family:"Courier New",monospace;
    font-size:11px;
    fill:#64748b;
    letter-spacing:2px;
}}

.text {{
    font-family:"Courier New",monospace;
    font-size:13px;
    fill:#cbd5e1;
}}

.muted {{
    font-family:"Courier New",monospace;
    font-size:12px;
    fill:#64748b;
}}

</style>

</defs>


<!-- BACKGROUND -->

<rect
    width="1200"
    height="520"
    rx="28"
    fill="url(#bg)"
/>


<!-- subtle ambient glow -->

<circle
    cx="210"
    cy="290"
    r="180"
    fill="#7c3aed"
    opacity=".10"
    filter="url(#glow)"
/>


<!-- TERMINAL HEADER -->

<rect
    x="28"
    y="28"
    width="1144"
    height="48"
    rx="14"
    fill="#0b0817"
    stroke="#292342"
/>

<circle cx="51" cy="52" r="6" fill="#ef4444"/>
<circle cx="71" cy="52" r="6" fill="#eab308"/>
<circle cx="91" cy="52" r="6" fill="#22c55e"/>

<text
    x="120"
    y="57"
    class="label"
>
SATYANSH@DEVBOX
</text>

<text
    x="1145"
    y="57"
    class="label"
    text-anchor="end"
>
WHOAMI
</text>


<!-- ================================================= -->
<!-- PHOTO FRAME -->
<!-- ================================================= -->

<!-- outer glow -->

<rect
    x="58"
    y="103"
    width="334"
    height="370"
    rx="30"
    fill="none"
    stroke="url(#accent)"
    stroke-width="3"
    opacity=".35"
    filter="url(#glow)"
/>


<!-- actual frame -->

<rect
    x="62"
    y="107"
    width="326"
    height="362"
    rx="28"
    fill="#0d0a1c"
    stroke="url(#accent)"
    stroke-width="2"
/>


<!-- PHOTO -->

<g clip-path="url(#photoClip)">

    <image
        href="data:image/jpeg;base64,{photo_b64}"
        x="75"
        y="118"
        width="300"
        height="340"
        preserveAspectRatio="xMidYMid slice"
    />

    <!-- dark subtle overlay -->

    <rect
        x="75"
        y="118"
        width="300"
        height="340"
        fill="#070914"
        opacity=".08"
    />

</g>


<!-- photo scanline -->

<rect
    x="75"
    y="118"
    width="300"
    height="2"
    fill="#22d3ee"
    opacity=".45"
/>


<!-- corner brackets -->

<path
    d="M75 155V130Q75 118 87 118H112"
    fill="none"
    stroke="#22d3ee"
    stroke-width="2"
/>

<path
    d="M338 118H363Q375 118 375 130V155"
    fill="none"
    stroke="#a855f7"
    stroke-width="2"
/>

<path
    d="M75 420V446Q75 458 87 458H112"
    fill="none"
    stroke="#7c3aed"
    stroke-width="2"
/>

<path
    d="M338 458H363Q375 458 375 446V420"
    fill="none"
    stroke="#22d3ee"
    stroke-width="2"
/>


<!-- online badge -->

<rect
    x="92"
    y="420"
    width="158"
    height="28"
    rx="8"
    fill="#080612"
    opacity=".92"
    stroke="#292342"
/>

<circle
    cx="108"
    cy="434"
    r="4"
    fill="#22c55e"
    filter="url(#glow)"
/>

<text
    x="120"
    y="438"
    class="label"
>
ONLINE / BUILDING
</text>


<!-- ================================================= -->
<!-- RIGHT SIDE -->
<!-- ================================================= -->

<g transform="translate(430 115)">

<!-- command -->

<text
    x="0"
    y="0"
    class="text"
>
<tspan fill="#22d3ee">$</tspan>
<tspan dx="8">cat identity.json</tspan>
</text>


<!-- name -->

<text
    x="0"
    y="55"
    class="title"
>
SATYANSH ACHARYA
</text>


<text
    x="0"
    y="82"
    class="role"
>
B.Tech CSE  ·  DEVELOPER  ·  BUILDER
</text>


<!-- separator -->

<path
    d="M0 106H690"
    stroke="#292342"
/>


<!-- identity -->

<text
    x="0"
    y="135"
    class="label"
>
IDENTITY
</text>


<text x="0" y="165" class="text">
├── builds    → web / backend / systems
</text>

<text x="0" y="190" class="text">
├── solves    → DSA / core CS
</text>

<text x="0" y="215" class="text">
├── explores  → AI / RAG / agents
</text>

<text x="0" y="240" class="text">
└── creates   → products / experiments
</text>


<!-- current mode -->

<text
    x="0"
    y="278"
    class="label"
>
CURRENT MODE
</text>


<rect
    x="0"
    y="296"
    width="690"
    height="48"
    rx="10"
    fill="#0b0817"
    stroke="#292342"
/>


<circle
    cx="23"
    cy="320"
    r="5"
    fill="#22c55e"
    filter="url(#glow)"
/>


<text
    x="42"
    y="325"
    class="text"
>
BUILDING
</text>


<text
    x="145"
    y="325"
    class="muted"
>
→ turning ideas into things that actually run
</text>


<!-- process -->

<text
    x="0"
    y="382"
    class="label"
>
PROCESS
</text>


<text x="0" y="412" class="text">
learn
</text>

<text x="55" y="412" class="muted">
→
</text>

<text x="82" y="412" class="text">
build
</text>

<text x="140" y="412" class="muted">
→
</text>

<text x="167" y="412" class="text">
break
</text>

<text x="225" y="412" class="muted">
→
</text>

<text x="252" y="412" class="text">
fix
</text>

<text x="290" y="412" class="muted">
→
</text>

<text x="317" y="412" class="text">
repeat
</text>


<!-- command -->

<text
    x="0"
    y="450"
    class="text"
>
<tspan fill="#a855f7">$</tspan>
<tspan dx="8">./keep_building.sh</tspan>
<tspan fill="#22c55e" dx="8">✓</tspan>
</text>

</g>


<!-- bottom -->

<path
    d="M62 488H1138"
    stroke="url(#accent)"
    stroke-width="1"
/>

<text
    x="62"
    y="508"
    class="label"
>
STATUS: ONLINE
</text>

<text
    x="1138"
    y="508"
    class="label"
    text-anchor="end"
>
BUILD MODE
</text>

</svg>
'''

output.write_text(svg, encoding="utf-8")

print("✅ assets/whoami.svg generated successfully")
