$sshDir = "$env:USERPROFILE\.ssh"
$configFile = "$sshDir\config"

Write-Host "Checking SSH directory: $sshDir"

if (!(Test-Path $sshDir)) { 
    New-Item -ItemType Directory -Path $sshDir | Out-Null 
    Write-Host "Created .ssh directory"
}

if (!(Test-Path $configFile)) { 
    New-Item -ItemType File -Path $configFile | Out-Null 
    Write-Host "Created config file"
}

$entry = @"

Host 10.10.3.141
    HostName 10.10.3.141
    User Anshul
"@

$currentConfig = Get-Content $configFile -Raw -ErrorAction SilentlyContinue
if ($null -eq $currentConfig) { $currentConfig = "" }

if ($currentConfig -notmatch "Host 10.10.3.141") {
    Add-Content -Path $configFile -Value $entry
    Write-Host "Added Host 10.10.3.141 to $configFile"
} else {
    Write-Host "Host 10.10.3.141 already exists in config"
}

# Check for keys
$keyPath = "$sshDir\id_rsa"
if (!(Test-Path $keyPath)) {
    Write-Host "No default SSH key found. You can generate one with 'ssh-keygen'."
}
