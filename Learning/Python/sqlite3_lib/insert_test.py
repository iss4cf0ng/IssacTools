import sqlite3

conn = sqlite3.connect('my_data.db')
print('Enter mu_data data')
while True:
    new_id = int(input('ID : '))
    new_name = input('Name : ')
    new_gender = input('Gender : ')
    x = (new_id, new_name, new_gender)
    sql = '''insert into students values(?,?,?)'''
    conn.execute(sql, x)
    conn.commit()
    again = input('Continue(y/n)? : ')
    if again[0] == 'n':
        break
conn.close()