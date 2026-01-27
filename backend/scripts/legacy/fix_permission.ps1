$configPath = "$env:USERPROFILE\.ssh\config"

Write-Host "Fixing permissions for: $configPath"

if (!(Test-Path $configPath)) {
    Write-Error "File not found: $configPath"
    exit 1
}

# Get current ACL
$acl = Get-Acl -Path $configPath

# Disable inheritance and remove inherited rules
$acl.SetAccessRuleProtection($true, $false)

# Remove all existing explicit access rules to start clean
$acl.Access | ForEach-Object { $acl.RemoveAccessRule($_) }

# Add FullControl for the current user
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule($currentUser, "FullControl", "Allow")
$acl.AddAccessRule($rule)

# Add FullControl for SYSTEM (often required for system processes, usually safe and expected by OpenSSH on Windows)
$systemRule = New-Object System.Security.AccessControl.FileSystemAccessRule("SYSTEM", "FullControl", "Allow")
$acl.AddAccessRule($systemRule)

# Add FullControl for Administrators (optional but often good practice)
# OpenSSH StrictModes usually allows Administrator.
$adminRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Administrators", "FullControl", "Allow")
$acl.AddAccessRule($adminRule)

# Apply the new ACL
Set-Acl -Path $configPath -AclObject $acl

Write-Host "Permissions successfully reset. Current access rules:"
(Get-Acl -Path $configPath).Access | Format-Table IdentityReference, FileSystemRights, AccessControlType
