import sqlite3

conn = sqlite3.connect('UsersDb.db')

cur = conn.cursor()

cur.execute('SELECT * FROM USERS')

one_result = cur.fetchone()

print(one_result)