SELECT 
  sessions.session_id AS ID,
  sessions.login_name AS [User],
  sessions.host_name AS Host,
  DB_NAME(sessions.database_id) AS DB,
  requests.command AS [Command],
  DATEDIFF(minute,requests.start_time,GETDATE()) AS Time,
  requests.status AS Status,
  requests.percent_complete AS Progress,
  (SELECT text FROM sys.dm_exec_sql_text(requests.sql_handle)) AS [SQL Query]
FROM 
  sys.dm_exec_sessions sessions
  INNER JOIN sys.dm_exec_requests requests ON sessions.session_id = requests.session_id