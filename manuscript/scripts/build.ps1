[CmdletBinding()]
param(
    [switch]$Clean,
    [switch]$Watch
)

$ErrorActionPreference = "Stop"

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$manuscriptRoot = Split-Path -Parent $scriptRoot
$buildDir = Join-Path $manuscriptRoot "build"
$mainTex = Join-Path $manuscriptRoot "main.tex"
$mainJobName = [System.IO.Path]::GetFileNameWithoutExtension($mainTex)

function Clear-BuildDirectory {
    $resolvedRoot = (Resolve-Path -LiteralPath $manuscriptRoot).Path
    $buildParent = Split-Path -Parent $buildDir
    $resolvedBuildParent = (Resolve-Path -LiteralPath $buildParent).Path

    if ($resolvedBuildParent -ne $resolvedRoot) {
        throw "Refusing to clear build directory outside manuscript root: $buildDir"
    }

    if (Test-Path $buildDir) {
        Get-ChildItem -LiteralPath $buildDir -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
    }

    New-Item -ItemType Directory -Force -Path $buildDir | Out-Null
}

if (-not (Test-Path $mainTex)) {
    throw "Could not find main.tex at $mainTex"
}

New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

if ($Clean) {
    Clear-BuildDirectory
}

Push-Location $manuscriptRoot
try {
    $latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
    $xelatex = Get-Command xelatex -ErrorAction Stop
    $biber = Get-Command biber -ErrorAction Stop
    $perl = Get-Command perl -ErrorAction SilentlyContinue

    $usedFallback = $false

    if ($Watch -and -not $latexmk) {
        throw "Watch mode requires latexmk, but latexmk is not available on this system."
    }

    if ($latexmk -and $perl) {
        $latexmkArgs = @(
            "-xelatex"
            "-interaction=nonstopmode"
            "-file-line-error"
            "-synctex=1"
            "-outdir=$buildDir"
        )

        if ($Watch) {
            $latexmkArgs += "-pvc"
        }

        $latexmkArgs += $mainTex

        & $latexmk.Source @latexmkArgs
        if ($LASTEXITCODE -ne 0) {
            $usedFallback = $true
            Clear-BuildDirectory
        }
    }
    else {
        $usedFallback = $true
    }

    if ($usedFallback) {
        if ($Watch) {
            throw "Watch mode requires a working latexmk installation. Install Perl or run without -Watch."
        }

        $xelatexArgs = @(
            "-interaction=nonstopmode"
            "-file-line-error"
            "-synctex=1"
            "-output-directory=$buildDir"
            $mainTex
        )

        & $xelatex.Source @xelatexArgs
        if ($LASTEXITCODE -ne 0) {
            throw "First XeLaTeX pass failed with exit code $LASTEXITCODE"
        }

        & $biber.Source "--output-directory" $buildDir $mainJobName
        if ($LASTEXITCODE -ne 0) {
            throw "Biber failed with exit code $LASTEXITCODE"
        }

        & $xelatex.Source @xelatexArgs
        if ($LASTEXITCODE -ne 0) {
            throw "Second XeLaTeX pass failed with exit code $LASTEXITCODE"
        }

        & $xelatex.Source @xelatexArgs
        if ($LASTEXITCODE -ne 0) {
            throw "Final XeLaTeX pass failed with exit code $LASTEXITCODE"
        }
    }
}
finally {
    Pop-Location
}

$outputPdf = Join-Path $buildDir "main.pdf"
if (Test-Path $outputPdf) {
    Write-Host "Build completed: $outputPdf"
}
