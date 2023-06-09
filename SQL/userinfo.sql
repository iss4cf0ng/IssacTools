SELECT 
    name AS UserName,
    CONCAT('0x', CONVERT(varchar(max), password_hash, 2)) AS PasswordHash,
    create_date AS CreateDate,
    modify_date AS ModifyDate
FROM sys.sql_logins
WHERE name NOT LIKE '##%' AND name NOT LIKE 'NT%' AND name NOT LIKE 'MS%'