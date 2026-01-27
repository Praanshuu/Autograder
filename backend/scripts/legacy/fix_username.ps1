$configFile = "$env:USERPROFILE\.ssh\config"
if (Test-Path $configFile) {
    (Get-Content $configFile).Replace('User Anshul', 'User anshul') | Set-Content $configFile
    Write-Host "Updated configuration to use lowercase 'anshul'"
}
else {
    Write-Host "Config file not found"
}
