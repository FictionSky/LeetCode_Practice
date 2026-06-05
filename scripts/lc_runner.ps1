param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Problem
)

$ErrorActionPreference = "Stop"
$utf8 = [System.Text.UTF8Encoding]::new($false)
[Console]::InputEncoding = $utf8
[Console]::OutputEncoding = $utf8
$OutputEncoding = $utf8

function Invoke-Native {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [string[]]$Arguments = @()
    )

    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$FilePath exited with code $LASTEXITCODE"
    }
}

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$rawProblem = $Problem.Trim()

if (-not ($rawProblem -match '^\d+$')) {
    throw "Use a numeric problem id, for example: .\lc 1 or .\lc 014"
}

$problemId = if ($rawProblem.Length -lt 3) { $rawProblem.PadLeft(3, '0') } else { $rawProblem }
$problemDir = Join-Path $root "problems\$problemId"

if (-not (Test-Path -LiteralPath $problemDir)) {
    throw "Problem folder not found: problems\$problemId"
}

$cppFiles = @(Get-ChildItem -LiteralPath $problemDir -Filter "*.cpp")
if ($cppFiles.Count -eq 0) {
    throw "No C++ file found in problems\$problemId"
}
if ($cppFiles.Count -gt 1) {
    $names = ($cppFiles | ForEach-Object { $_.Name }) -join ", "
    throw "Multiple C++ files found in problems\${problemId}: $names"
}

$target = $cppFiles[0].BaseName
$buildDir = Join-Path $root "build"
$cachePath = Join-Path $buildDir "CMakeCache.txt"

if (-not (Test-Path -LiteralPath $cachePath)) {
    Invoke-Native "cmake" @("-S", $root, "-B", $buildDir)
}

Invoke-Native "cmake" @("--build", $buildDir, "--target", $target)

$exePath = Join-Path $buildDir "bin\$target.exe"
if (-not (Test-Path -LiteralPath $exePath)) {
    throw "Executable not found after build: $exePath"
}

Write-Host ""
Write-Host "Running $target"
Write-Host ""
Invoke-Native $exePath
