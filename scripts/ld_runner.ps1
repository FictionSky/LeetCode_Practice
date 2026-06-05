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

function Write-JsonFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        $Data
    )

    $json = $Data | ConvertTo-Json -Depth 10
    $json | Set-Content -LiteralPath $Path -Encoding utf8
}

function Get-ProblemTarget {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RootPath,
        [Parameter(Mandatory = $true)]
        [string]$RawProblem
    )

    if (-not ($RawProblem -match '^\d+$')) {
        throw "Use a numeric problem id, for example: .\ld 1 or .\ld 014"
    }

    $problemId = if ($RawProblem.Length -lt 3) { $RawProblem.PadLeft(3, '0') } else { $RawProblem }
    $problemDir = Join-Path $RootPath "problems\$problemId"
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

    return @{
        ProblemId = $problemId
        CppPath = $cppFiles[0].FullName
        Target = $cppFiles[0].BaseName
    }
}

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$targetInfo = Get-ProblemTarget -RootPath $root -RawProblem $Problem.Trim()
$buildDir = Join-Path $root "build"
$cachePath = Join-Path $buildDir "CMakeCache.txt"
$exePath = Join-Path $buildDir "bin\$($targetInfo.Target).exe"
$vscodeDir = Join-Path $root ".vscode"
$launchPath = Join-Path $vscodeDir "launch.json"
$tasksPath = Join-Path $vscodeDir "tasks.json"

if (-not (Test-Path -LiteralPath $cachePath)) {
    Invoke-Native "cmake" @("-S", $root, "-B", $buildDir)
}

Invoke-Native "cmake" @("--build", $buildDir, "--target", $targetInfo.Target)

if (-not (Test-Path -LiteralPath $exePath)) {
    throw "Executable not found after build: $exePath"
}

New-Item -ItemType Directory -Path $vscodeDir -Force | Out-Null

$workspaceRoot = $root.Replace('\', '/')
$cppPath = $targetInfo.CppPath.Replace('\', '/')
$exePathForward = $exePath.Replace('\', '/')

$launchConfig = @{
    version = "0.2.0"
    configurations = @(
        @{
            name = "Debug Active LeetCode Target"
            type = "cppdbg"
            request = "launch"
            program = $exePathForward
            args = @()
            stopAtEntry = $false
            cwd = $workspaceRoot
            environment = @()
            externalConsole = $false
            MIMode = "gdb"
            miDebuggerPath = "gdb"
            preLaunchTask = "Build Active LeetCode Target"
        }
    )
}

$tasksConfig = @{
    version = "2.0.0"
    tasks = @(
        @{
            label = "Build Active LeetCode Target"
            type = "shell"
            command = "cmake --build build --target $($targetInfo.Target)"
            options = @{
                cwd = $workspaceRoot
            }
            problemMatcher = @('$gcc')
            group = @{
                kind = "build"
                isDefault = $true
            }
        }
    )
}

Write-JsonFile -Path $launchPath -Data $launchConfig
Write-JsonFile -Path $tasksPath -Data $tasksConfig

Write-Host ""
Write-Host "Prepared VSCode debug for $($targetInfo.Target)"
Write-Host "launch.json: $launchPath"
Write-Host "tasks.json: $tasksPath"
Write-Host "source: $($targetInfo.CppPath)"
Write-Host "Press F5 in VSCode to start debugging with your breakpoints."
Write-Host ""

Start-Process -FilePath "code" -ArgumentList @("--reuse-window", "--goto", "${cppPath}:1") -WindowStyle Hidden
