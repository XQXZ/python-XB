import MySQLdb

conn = MySQLdb.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'xb',
    charset = 'utf8'
    )
cursor = conn.cursor()
print conn
print cursor

cursor.close()
conn.close()