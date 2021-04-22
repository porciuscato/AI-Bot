$mysql = Get-Service -Name "MySQL80"
if ($mysql.Status -eq "Stopped") {
    Set-Service -Name "Mysql80" -Status "Running"
}

# for ($i = 0; $i -lt 1000000; $i++) { Write-Host $mysql.Status }

