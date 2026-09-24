$ErrorActionPreference = "Stop"

# ============================================================
# CONFIG
# ============================================================

$username = "Spade-2006"

$repoRoot = Get-Location
$assetsDir = Join-Path $repoRoot "assets"
$output = Join-Path $assetsDir "contribution.svg"


# ============================================================
# ENSURE ASSETS FOLDER EXISTS
# ============================================================

if (!(Test-Path -LiteralPath $assetsDir)) {

    New-Item `
        -ItemType Directory `
        -Path $assetsDir `
        -Force | Out-Null
}


Write-Host ""
Write-Host "=============================================="
Write-Host "     GITHUB CONTRIBUTION MATRIX"
Write-Host "=============================================="
Write-Host ""

Write-Host "Repository : $repoRoot"
Write-Host "Output     : $output"
Write-Host ""



# ============================================================
# FETCH GITHUB CONTRIBUTIONS
# ============================================================

Write-Host "Fetching GitHub contribution data..."
Write-Host ""

$url = "https://github.com/users/$username/contributions"

$response = Invoke-WebRequest `
    -Uri $url `
    -UseBasicParsing

$html = $response.Content


# ============================================================
# EXTRACT CONTRIBUTION CELLS
# ============================================================

$pattern = '<td[^>]*data-date="([^"]+)"[^>]*data-level="([^"]+)"[^>]*>'

$matches = [regex]::Matches(
    $html,
    $pattern
)


if ($matches.Count -eq 0) {

    Write-Host ""
    Write-Host "ERROR: Could not find contribution data."
    Write-Host ""
    exit 1
}


Write-Host "Found $($matches.Count) contribution cells."
Write-Host ""


# ============================================================
# BUILD CONTRIBUTION DATA
# ============================================================

$cells = @()


foreach ($match in $matches) {

    $date = $match.Groups[1].Value

    $level = [int]$match.Groups[2].Value


    $cells += [PSCustomObject]@{

        Date = $date

        Level = $level

    }

}



# ============================================================
# BASIC ACTIVITY SCORE
# ============================================================

$total = 0


foreach ($cell in $cells) {

    $total += $cell.Level

}



# ============================================================
# SVG CONFIG
# ============================================================

$width = 1200

$height = 480



# ============================================================
# SVG START
# ============================================================

$svg = @"
<svg
xmlns="http://www.w3.org/2000/svg"
width="$width"
height="$height"
viewBox="0 0 $width $height">

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
            stop-color="#8b5cf6"/>

        <stop
            offset="50%"
            stop-color="#c084fc"/>

        <stop
            offset="100%"
            stop-color="#38bdf8"/>

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

"@


for ($x = 0; $x -le $width; $x += 50) {

    $svg += @"
    <line
        x1="$x"
        y1="0"
        x2="$x"
        y2="$height"
        stroke="#252846"/>

"@

}


for ($y = 0; $y -le $height; $y += 50) {

    $svg += @"
    <line
        x1="0"
        y1="$y"
        x2="$width"
        y2="$y"
        stroke="#252846"/>

"@

}


$svg += @"
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
    fill="#858aa8"
    font-family="monospace"
    font-size="13"
    font-weight="600">

    CONTRIBUTION MATRIX // $username

</text>


<text
    x="40"
    y="78"
    fill="#f4f1ff"
    font-family="monospace"
    font-size="27"
    font-weight="700">

    BUILDING CONSISTENTLY

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
<!-- ACTIVITY -->
<!-- ===================================================== -->

<text
    x="45"
    y="145"
    fill="#c084fc"
    font-family="monospace"
    font-size="12">

    ACTIVITY

</text>


<text
    x="45"
    y="175"
    fill="#f4f1ff"
    font-family="monospace"
    font-size="22"
    font-weight="700">

    $total

</text>


<text
    x="45"
    y="196"
    fill="#858aa8"
    font-family="Arial"
    font-size="11">

    contribution intensity

</text>



<!-- ===================================================== -->
<!-- CONTRIBUTION MATRIX -->
<!-- ===================================================== -->

<g>

"@


# ============================================================
# MATRIX
# ============================================================

$startX = 45

$startY = 230

$cellSize = 12

$gap = 4

$columns = 78

$rows = 7


for ($i = 0; $i -lt $cells.Count; $i++) {


    $column = [math]::Floor($i / $rows)

    $row = $i % $rows


    if ($column -ge $columns) {

        break

    }


    $x = $startX + (
        $column * ($cellSize + $gap)
    )


    $y = $startY + (
        $row * ($cellSize + $gap)
    )


    $level = $cells[$i].Level


    switch ($level) {

        0 {

            $fill = "#111426"

        }

        1 {

            $fill = "#3b245c"

        }

        2 {

            $fill = "#663b8f"

        }

        3 {

            $fill = "#995bd1"

        }

        4 {

            $fill = "#c084fc"

        }

        default {

            $fill = "#c084fc"

        }

    }


    $date = $cells[$i].Date


    $svg += @"
    <rect
        x="$x"
        y="$y"
        width="$cellSize"
        height="$cellSize"
        rx="3"
        fill="$fill">

        <title>$date</title>

    </rect>

"@

}



$svg += @"
</g>



<!-- ===================================================== -->
<!-- LEGEND -->
<!-- ===================================================== -->

<text
    x="45"
    y="365"
    fill="#858aa8"
    font-family="monospace"
    font-size="10">

    LESS

</text>


<rect
    x="85"
    y="355"
    width="12"
    height="12"
    rx="3"
    fill="#111426"
/>


<rect
    x="103"
    y="355"
    width="12"
    height="12"
    rx="3"
    fill="#3b245c"
/>


<rect
    x="121"
    y="355"
    width="12"
    height="12"
    rx="3"
    fill="#663b8f"
/>


<rect
    x="139"
    y="355"
    width="12"
    height="12"
    rx="3"
    fill="#995bd1"
/>


<rect
    x="157"
    y="355"
    width="12"
    height="12"
    rx="3"
    fill="#c084fc"
/>


<text
    x="180"
    y="365"
    fill="#858aa8"
    font-family="monospace"
    font-size="10">

    MORE

</text>



<!-- ===================================================== -->
<!-- FOOTER -->
<!-- ===================================================== -->

<line
    x1="40"
    y1="405"
    x2="1160"
    y2="405"
    stroke="#202443"
/>


<text
    x="40"
    y="435"
    fill="#858aa8"
    font-family="monospace"
    font-size="10">

    BUILDING • LEARNING • SHIPPING

</text>


<text
    x="1160"
    y="435"
    fill="#c084fc"
    font-family="monospace"
    font-size="10"
    text-anchor="end">

    github.com/$username

</text>


</svg>

"@



# ============================================================
# WRITE SVG
# ============================================================

[System.IO.File]::WriteAllText(
    $output,
    $svg,
    [System.Text.Encoding]::UTF8
)



# ============================================================
# DONE
# ============================================================

Write-Host ""

Write-Host "=============================================="

Write-Host "       CONTRIBUTION MATRIX GENERATED"

Write-Host "=============================================="

Write-Host ""

Write-Host "Output: $output"

Write-Host ""

Write-Host "Done."

Write-Host ""