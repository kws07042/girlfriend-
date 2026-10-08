# Same-name replacements: newest source wins. No source files are removed.
$taskRoot = $PSScriptRoot
$taskBgDestination = Join-Path $taskRoot 'RenPy_게임\game\images\bg'
$taskBgCandidates = @()
foreach ($taskFolder in @('backgrounds','backgrounds_styled')) {
    $taskSource = Join-Path $taskRoot $taskFolder
    if (Test-Path -LiteralPath $taskSource) {
        $taskBgCandidates += @(Get-ChildItem -LiteralPath $taskSource -File | Where-Object Extension -In '.png','.jpg','.jpeg','.webp')
    }
}
New-Item -ItemType Directory -Path $taskBgDestination -Force | Out-Null
$taskCount = 0
foreach ($taskGroup in ($taskBgCandidates | Group-Object Name)) {
    $taskLatest = $taskGroup.Group | Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1
    Copy-Item -LiteralPath $taskLatest.FullName -Destination (Join-Path $taskBgDestination $taskLatest.Name) -Force
    $taskCount += 1
}
Write-Output "배경 $taskCount 개를 게임에 연결했습니다."
