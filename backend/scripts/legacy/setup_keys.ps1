$sshDir = "$env:USERPROFILE\.ssh"
$keyFile = "$sshDir\id_rsa"

if (Test-Path "$keyFile") {
    Write-Host "Key already exists at $keyFile. Skipping generation."
}
else {
    Write-Host "Generating new SSH key non-interactively..."
    # Quotes are essential for paths with spaces
    ssh-keygen -t rsa -b 4096 -f "$keyFile" -N ""
    Write-Host "Key generated successfully."
}

$deployCmd = "type `"$keyFile.pub`" | ssh anshul@10.10.3.141 `"mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys`""

Write-Host "`nTo finish, COPY AND RUN the following command to enable password-less login:"
Write-Host "---------------------------------------------------------------------------------"
Write-Host $deployCmd
Write-Host "---------------------------------------------------------------------------------"
Write-Host "(You will be asked for the password 'GPU4Naman' one last time)"
