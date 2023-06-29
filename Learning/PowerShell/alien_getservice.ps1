$services = Get-WmiObject win32_service
$rows = $services | select ProcessId, Name, DisplayName, ServiceType, @{Name="Path"; Expression={$_.PathName.split('"')[1]}}, Status, Description
foreach ($row in $rows)
{
    $line =  "{0}|{1}|{2}|{3}|{4}|{5}|{6}[SPLIT]" -f $row.ProcessID, $row.Name, $row.DisplayName, $row.ServiceType, $row.Path, $row.Status, $row.Description
    Write-Host $line
}