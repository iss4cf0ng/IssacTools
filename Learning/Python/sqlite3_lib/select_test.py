import sqlite3

conn = sqlite3.connect('my_data.db')
results = conn.execute('select * from students')
for record in results:
    print('ID :', record[0])
    print('Name :', record[1])
    print('Gender :', record[2])
conn.close()