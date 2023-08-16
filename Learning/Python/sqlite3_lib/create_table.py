import sqlite3

conn = sqlite3.connect('my_data.db')
cursor = conn.cursor()
sql = '''
    Create table students(
    id int,
    name text,
    gender text
    )
    '''
cursor.execute(sql) # Or just conn.execute(sql)
cursor.close()
conn.close()