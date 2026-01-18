#!/usr/bin/env powershell
<#
.SYNOPSIS
    Doctor — Environment validation script for agentcopilot project.
    
.DESCRIPTION
    Checks that the development environment is correctly configured:
    - PowerShell version compatibility
    - Node.js/npm installed and available
    - .env file exists (if needed)
    - Project folders are in place (docs, .github, src, output, data)
    - Package dependencies are installed
    
.EXAMPLE
    .\scripts\doctor.ps1
    
.NOTES
    Exit codes:
    0 = All checks passed
    1 = One or more checks failed
#>

param(
    [switch]$Verbose = $false
)

# Configuration
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$RequiredFolders = @("docs", ".github", ".vscode")
$OptionalFolders = @("src", "output", "data", "scripts")
$RequiredFiles = @("README.md", "LICENSE", "CONTRIBUTING.md", "index.html")
$PowerShellMinVersion = "5.1"

# Counters
$ChecksPassed = 0
$ChecksFailed = 0
$ChecksWarning = 0

# Helper functions
function Write-Status {
    param(
        [string]$Message,
        [ValidateSet("Pass", "Fail", "Warn", "Info")]
        [string]$Status = "Info"
    )
    
    $Symbols = @{
        "Pass" = "✓"
        "Fail" = "✗"
        "Warn" = "⚠"
        "Info" = "ℹ"
    }
    
    $Colors = @{
        "Pass" = "Green"
        "Fail" = "Red"
        "Warn" = "Yellow"
        "Info" = "Cyan"
    }
    
    $Symbol = $Symbols[$Status]
    $Color = $Colors[$Status]
    
    Write-Host "$Symbol " -ForegroundColor $Color -NoNewline
    Write-Host $Message
    
    if ($Status -eq "Pass") { $Script:ChecksPassed++ }
    elseif ($Status -eq "Fail") { $Script:ChecksFailed++ }
    elseif ($Status -eq "Warn") { $Script:ChecksWarning++ }
}

# Header
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Doctor — Environment Check" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check 1: PowerShell version
Write-Host "1. PowerShell Version" -ForegroundColor White
$PSVersion = $PSVersionTable.PSVersion
$PSVersionString = "$($PSVersion.Major).$($PSVersion.Minor)"

if ([version]$PSVersionString -ge [version]$PowerShellMinVersion) {
    Write-Status "PowerShell $PSVersionString (required: $PowerShellMinVersion)" "Pass"
} else {
    Write-Status "PowerShell $PSVersionString (required: $PowerShellMinVersion)" "Fail"
}

# Check 2: Project root location
Write-Host "`n2. Project Root" -ForegroundColor White
if (Test-Path $ProjectRoot) {
    Write-Status "Project root: $ProjectRoot" "Pass"
} else {
    Write-Status "Project root not found: $ProjectRoot" "Fail"
}

# Check 3: Required folders
Write-Host "`n3. Required Folders" -ForegroundColor White
foreach ($Folder in $RequiredFolders) {
    $FolderPath = Join-Path $ProjectRoot $Folder
    if (Test-Path $FolderPath -PathType Container) {
        Write-Status "$Folder/" "Pass"
    } else {
        Write-Status "$Folder/ (missing)" "Fail"
    }
}

# Check 4: Optional folders (with warnings if missing)
Write-Host "`n4. Optional Folders" -ForegroundColor White
foreach ($Folder in $OptionalFolders) {
    $FolderPath = Join-Path $ProjectRoot $Folder
    if (Test-Path $FolderPath -PathType Container) {
        Write-Status "$Folder/" "Pass"
    } else {
        Write-Status "$Folder/ (not yet created)" "Warn"
    }
}

# Check 5: Required files
Write-Host "`n5. Required Files" -ForegroundColor White
foreach ($File in $RequiredFiles) {
    $FilePath = Join-Path $ProjectRoot $File
    if (Test-Path $FilePath -PathType Leaf) {
        Write-Status $File "Pass"
    } else {
        Write-Status "$File (missing)" "Fail"
    }
}

# Check 6: Node.js/npm
Write-Host "`n6. Node.js & npm" -ForegroundColor White
try {
    $NodeVersion = node --version 2>$null
    $NpmVersion = npm --version 2>$null
    
    if ($NodeVersion -and $NpmVersion) {
        Write-Status "Node.js $NodeVersion" "Pass"
        Write-Status "npm $NpmVersion" "Pass"
    } else {
        Write-Status "Node.js or npm not found (optional for documentation-only projects)" "Warn"
    }
} catch {
    Write-Status "Node.js or npm not found (optional for documentation-only projects)" "Warn"
}

# Check 7: package.json and dependencies
Write-Host "`n7. Package Dependencies" -ForegroundColor White
$PackageJsonPath = Join-Path $ProjectRoot "package.json"
if (Test-Path $PackageJsonPath) {
    Write-Status "package.json exists" "Pass"
    
    $NodeModulesPath = Join-Path $ProjectRoot "node_modules"
    if (Test-Path $NodeModulesPath -PathType Container) {
        Write-Status "node_modules/ installed" "Pass"
    } else {
        Write-Status "node_modules/ not installed (run 'npm install')" "Warn"
    }
} else {
    Write-Status "package.json not found (optional for template-only projects)" "Warn"
}

# Check 8: .env file (if .env.example exists)
Write-Host "`n8. Environment Configuration" -ForegroundColor White
$EnvExamplePath = Join-Path $ProjectRoot ".env.example"
$EnvPath = Join-Path $ProjectRoot ".env"

if (Test-Path $EnvExamplePath) {
    if (Test-Path $EnvPath) {
        Write-Status ".env file exists" "Pass"
    } else {
        Write-Status ".env file missing (copy from .env.example or create manually)" "Fail"
    }
} else {
    Write-Status ".env not required for this project" "Info"
}

# Check 9: Git repository
Write-Host "`n9. Git Repository" -ForegroundColor White
$GitDir = Join-Path $ProjectRoot ".git"
if (Test-Path $GitDir -PathType Container) {
    Write-Status "Git repository initialized" "Pass"
} else {
    Write-Status "Not a Git repository (run 'git init' if needed)" "Warn"
}

# Check 10: VS Code workspace files
Write-Host "`n10. VS Code Configuration" -ForegroundColor White
$VscodeDirPath = Join-Path $ProjectRoot ".vscode"
$TasksJsonPath = Join-Path $VscodeDirPath "tasks.json"

if (Test-Path $VscodeDirPath) {
    Write-Status ".vscode/ directory exists" "Pass"
    
    if (Test-Path $TasksJsonPath) {
        Write-Status "tasks.json configured" "Pass"
    } else {
        Write-Status "tasks.json missing (create with 'Engineer' role)" "Warn"
    }
} else {
    Write-Status ".vscode/ not configured" "Warn"
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Summary" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Passed: " -NoNewline
Write-Host "$ChecksPassed" -ForegroundColor Green
Write-Host "Warnings: " -NoNewline
Write-Host "$ChecksWarning" -ForegroundColor Yellow
Write-Host "Failed: " -NoNewline
Write-Host "$ChecksFailed" -ForegroundColor Red

# Recommendations
if ($ChecksFailed -gt 0) {
    Write-Host "`n❌ Environment check FAILED. Please fix the issues above." -ForegroundColor Red
    Write-Host "`nNext steps:" -ForegroundColor White
    Write-Host "  1. Install missing required folders or files" -ForegroundColor Gray
    Write-Host "  2. If Node.js is needed, install from https://nodejs.org/" -ForegroundColor Gray
    Write-Host "  3. Run 'npm install' if package.json exists" -ForegroundColor Gray
    Write-Host "  4. Run this script again to verify" -ForegroundColor Gray
    exit 1
} elseif ($ChecksWarning -gt 0) {
    Write-Host "`n⚠️  Environment check PASSED with warnings." -ForegroundColor Yellow
    Write-Host "`nNext steps:" -ForegroundColor White
    Write-Host "  - Review warnings above and install optional dependencies if needed" -ForegroundColor Gray
    Write-Host "  - You can proceed with development, but some tasks may require additional setup" -ForegroundColor Gray
    exit 0
} else {
    Write-Host "`n✓ Environment check PASSED!" -ForegroundColor Green
    Write-Host "`nYou're ready to start. Use VS Code tasks:" -ForegroundColor White
    Write-Host "  - Ctrl+Shift+B: Run default build/test task" -ForegroundColor Gray
    Write-Host "  - Ctrl+Shift+P > 'Tasks: Run Task': See all available tasks" -ForegroundColor Gray
    exit 0
}
