$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Log = Join-Path $env:LOCALAPPDATA "huginn-release.log"
$env:GH_TOKEN = $null
$env:GITHUB_TOKEN = $null
$stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Add-Content -Path $Log -Value "$stamp start"
try {
  Set-Location $Root
  py -3.13 (Join-Path $PSScriptRoot "publish_release.py") 2>&1 | ForEach-Object { Add-Content -Path $Log -Value "$stamp $_" }
  if ($LASTEXITCODE -ne 0) { throw "publish_release.py exited $LASTEXITCODE" }
  Add-Content -Path $Log -Value "$stamp done"
} catch {
  Add-Content -Path $Log -Value "$stamp FAILED $($_.Exception.Message)"
  throw
}
