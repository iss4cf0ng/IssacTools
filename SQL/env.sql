SELECT 'MachineName' AS PropertyName, SERVERPROPERTY('MachineName') AS PropertyValue
UNION ALL
SELECT 'InstanceName', SERVERPROPERTY('InstanceName')
UNION ALL
SELECT 'Edition', SERVERPROPERTY('Edition')
UNION ALL
SELECT 'ProductVersion', SERVERPROPERTY('ProductVersion')
UNION ALL
SELECT 'ProductLevel', SERVERPROPERTY('ProductLevel')
UNION ALL
SELECT 'Collation', SERVERPROPERTY('Collation')
UNION ALL
SELECT 'BuildClrVersion', SERVERPROPERTY('BuildClrVersion')
UNION ALL
SELECT 'IsIntegratedSecurityOnly', SERVERPROPERTY('IsIntegratedSecurityOnly')
UNION ALL
SELECT 'IsHadrEnabled', SERVERPROPERTY('IsHadrEnabled')
UNION ALL
SELECT 'IsPolyBaseInstalled', SERVERPROPERTY('IsPolyBaseInstalled')
UNION ALL
SELECT 'InstanceDefaultDataPath', SERVERPROPERTY('InstanceDefaultDataPath')
UNION ALL
SELECT 'InstanceDefaultLogPath', SERVERPROPERTY('InstanceDefaultLogPath')
UNION ALL
SELECT 'InstanceDefaultBackupPath', SERVERPROPERTY('InstanceDefaultBackupPath')
UNION ALL
SELECT 'InstanceDefaultDumpPath', SERVERPROPERTY('InstanceDefaultDumpPath')