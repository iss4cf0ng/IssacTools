EXEC sp_msforeachdb '
USE [?];
IF DB_ID() > 4 AND EXISTS (SELECT * FROM sys.databases WHERE name = DB_NAME() AND state = 0)
BEGIN
    SELECT @@SERVERNAME AS [ServerName], DB_NAME() AS [DatabaseName], @@VERSION AS [EngineVersion]
END
'