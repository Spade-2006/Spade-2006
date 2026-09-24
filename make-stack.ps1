$ErrorActionPreference = "Stop"

$iconDir = "assets\icons"
New-Item -ItemType Directory -Force -Path $iconDir | Out-Null

$icons = @{
    "html5"       = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"
    "css3"        = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"
    "javascript"  = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"
    "typescript"  = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg"
    "react"       = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"
    "nextjs"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg"
    "tailwind"    = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg"
    "vite"        = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vitejs/vitejs-original.svg"
    "nodejs"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"
    "express"     = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg"
    "nestjs"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nestjs/nestjs-original.svg"
    "java"        = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"
    "python"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
    "graphql"     = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/graphql/graphql-plain.svg"
    "postgresql"  = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"
    "mongodb"     = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"
    "redis"       = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg"
    "prisma"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/prisma/prisma-original.svg"
    "git"         = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"
    "github"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
    "linux"       = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"
    "docker"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"
    "kubernetes"  = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg"
    "aws"         = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg"
    "figma"       = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg"
    "vscode"      = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"
    "cpp"         = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"
}

foreach ($name in $icons.Keys) {
    $output = "$iconDir\$name.svg"

    Write-Host "Downloading $name..."

    Invoke-WebRequest `
        -Uri $icons[$name] `
        -OutFile $output

    if (!(Test-Path $output)) {
        throw "Failed to download $name"
    }
}

Write-Host ""
Write-Host "========================================"
Write-Host "  ALL TECH ICONS DOWNLOADED"
Write-Host "========================================"
Write-Host ""