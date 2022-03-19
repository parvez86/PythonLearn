import mysql.connector;

conn = mysql.connector.connect(host='localhost', database='employeedb', user='mydb', password='2016331086$sp')

if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

cursor.execute('select * from employee')

rows = cursor.fetchall()
print("Total Number of records", cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()
