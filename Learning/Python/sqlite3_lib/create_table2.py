import sqlite3

conn = sqlite3.connect('my_info2.py')
sql = '''
    Create table student2(
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gender TEXT
    )
'''
conn.execute(sql)
conn.close()