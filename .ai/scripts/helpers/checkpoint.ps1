<#
.SYNOPSIS
    One-shot checkpoint commit (LiteRealm rule 1: proactive git).
    Stages everything and commits with or without AI marker prefix based on context.
.EXAMPLE
    .\.ai\scripts\helpers\checkpoint.ps1 "feat(latex): add uvod chapter"
    .\.ai\scripts\helpers\checkpoint.ps1 -UserDriven "feat(model): add road profile data"
#>
param(
    [Parameter(Mandatory = $true)][string]$Message,
    [Alias("NoAi", "User")][switch]$UserDriven
)

# ASCII-only source file: build the robot emoji from its code point.
$ai = [char]::ConvertFromUtf32(0x1F916) + " [AI]"

$root = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))

if (-not (git -C $root status --porcelain)) {
    Write-Host "Nothing to commit - working tree clean." -ForegroundColor Gray
    exit 0
}

if ($UserDriven) {
    # User-driven / co-authored commit: keep clean Conventional Commit without AI marker
    if ($Message -notmatch '^[a-z]+(\([^)]+\))?!?:\s*(.+)$') {
        $Message = "chore: $Message"
    }
} else {
    # Autonomous AI commit: inject AI marker if not already present
    if ($Message -notmatch '\[AI\]') {
        if ($Message -match '^[a-z]+(\([^)]+\))?!?:\s*(.+)$') {
            # Conventional commit: insert the marker after "type(scope):".
            $Message = $Message -replace '^([a-z]+(\([^)]+\))?!?:)\s*', "`$1 $ai "
        } else {
            $Message = "chore: $ai $Message"
        }
    }
}

git -C $root add -A
git -C $root commit -m $Message
exit $LASTEXITCODE
