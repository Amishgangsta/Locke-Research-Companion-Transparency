# Publish only this documentation folder via an authenticated local GitHub CLI.
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if ((Split-Path $root -Leaf) -ne 'Locke-Research-Companion-Transparency') { throw 'Unexpected folder name. Publication aborted.' }
Set-Location -LiteralPath $root
if (Test-Path -LiteralPath '.git') { throw 'Existing Git checkout detected. Inspect manually; nothing published.' }
foreach ($name in @('git', 'gh', 'python')) {
  if (-not (Get-Command $name -ErrorAction SilentlyContinue)) { throw "Required CLI unavailable: $name" }
}
python .\scripts\verify_public_docs.py
if ($LASTEXITCODE -ne 0) { throw 'Docs verification failed.' }
# gh prints authentication details to stderr even on success; judge by exit code.
$oldPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
& gh auth status *> $null
$authExit = $LASTEXITCODE
$ErrorActionPreference = $oldPreference
if ($authExit -ne 0) { throw 'GitHub CLI authentication required.' }
$target = 'Amishgangsta/Locke-Research-Companion-Transparency'
$oldPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
& gh repo view $target --json name -q .name *> $null
$viewExit = $LASTEXITCODE
$ErrorActionPreference = $oldPreference
if ($viewExit -eq 0) { throw "Target $target already exists. Refusing to overwrite." }
git init -b main
if ($LASTEXITCODE -ne 0) { throw 'git init failed.' }
git add README.md CHANGELOG.md PUBLISHING.md docs scripts .gitignore
if ($LASTEXITCODE -ne 0) { throw 'git add failed.' }
git commit -m 'docs: publish Locke Research Companion public technical reference'
if ($LASTEXITCODE -ne 0) { throw 'Git commit failed. Check Git identity.' }
gh repo create $target --public --source . --remote origin --push --description 'Public reference for Locke Research Companion legal research, case intelligence, privacy and source evidence'
if ($LASTEXITCODE -ne 0) { throw 'GitHub creation/push failed. Inspect status before retrying.' }
Write-Host "Published https://github.com/$target"
