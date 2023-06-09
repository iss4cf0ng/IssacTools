SELECT name, STUFF(CONVERT(varchar(max), password_hash, 2), 1, 2, '') AS password_hash_hex FROM sys.sql_logins;

SELECT name, CONVERT(VARCHAR(64), HASHBYTES('SHA2_256', CONVERT(VARCHAR(MAX), password_hash), 1), 2) AS sha_password_hash FROM sys.sql_logins

SELECT name, CONVERT(VARCHAR(512), HASHBYTES('SHA2_512', CAST(password_hash AS varbinary(max))), 2) AS password_sha512 FROM sys.sql_logins

SELECT name, CONVERT(varchar(max), password_hash, 1) AS hashed_password FROM sys.sql_logins