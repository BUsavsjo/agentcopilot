#!/usr/bin/env powershell
<#
.SYNOPSIS
    Initiera projekt-memory från template.
    
.DESCRIPTION
    Skapar project.memory.json baserat på project.memory.template.json.
    Fyller i metadata.started med dagens datum.
    Frågar innan befintlig memory skrivs över.
    
.EXAMPLE
    .\scripts\init-memory.ps1
    
.NOTES
    Kör detta INNAN du börjar med någon roll (Analyst, Architect, etc.)
#>

param(
    [switch]$Force = $false
)

# Paths
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$TemplatePath = Join-Path $ProjectRoot "project.memory.template.json"
$MemoryPath = Join-Path $ProjectRoot "project.memory.json"

# Colors
$Green = "Green"
$Yellow = "Yellow"
$Red = "Red"
$Cyan = "Cyan"

Write-Host "`n=== Project Memory Initialisering ===" -ForegroundColor $Cyan

# Check template exists
if (-not (Test-Path $TemplatePath)) {
    Write-Host "ERROR: Template file not found: $TemplatePath" -ForegroundColor $Red
    Write-Host "  Check that project.memory.template.json exists in project root." -ForegroundColor $Yellow
    exit 1
}

# Check if memory already exists
if (Test-Path $MemoryPath) {
    if (-not $Force) {
        Write-Host "WARNING: project.memory.json already exists!" -ForegroundColor $Yellow
        $response = Read-Host "Overwrite? (y/n)"
        if ($response -ne "y" -and $response -ne "Y") {
            Write-Host "Aborted. Existing memory unchanged." -ForegroundColor $Green
            exit 0
        }
    }
    Write-Host "Overwriting existing memory..." -ForegroundColor $Yellow
}

# Read template
try {
    $template = Get-Content $TemplatePath -Raw | ConvertFrom-Json
} catch {
    Write-Host "ERROR: Could not read template file." -ForegroundColor $Red
    Write-Host "  Detail: $_" -ForegroundColor $Red
    exit 1
}

# Update metadata with current date
$currentDate = Get-Date -Format "yyyy-MM-dd"
$template.metadata.started = $currentDate

# Detect current branch
try {
    $currentBranch = git rev-parse --abbrev-ref HEAD 2>$null
    if ($LASTEXITCODE -eq 0 -and $currentBranch) {
        $template.metadata.branch = $currentBranch
    }
} catch {
    # Ignore if git not available
}

# Write to project.memory.json
try {
    $template | ConvertTo-Json -Depth 10 | Set-Content $MemoryPath -Encoding UTF8
    Write-Host "SUCCESS: project.memory.json created!" -ForegroundColor $Green
    Write-Host "  Location: $MemoryPath" -ForegroundColor $Cyan
    Write-Host "  Date: $currentDate" -ForegroundColor $Cyan
    if ($template.metadata.branch) {
        Write-Host "  Branch: $($template.metadata.branch)" -ForegroundColor $Cyan
    }
} catch {
    Write-Host "ERROR: Could not write memory file." -ForegroundColor $Red
    Write-Host "  Detail: $_" -ForegroundColor $Red
    exit 1
}

Write-Host "`nReady! Start with /analyst or /router in Copilot Chat." -ForegroundColor $Green
Write-Host "=========================================`n" -ForegroundColor $Cyan

exit 0
