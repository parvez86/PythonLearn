import mysql.connector;

conn = mysql.connector.connect(host='localhost', database='employeedb', user='mydb', password='12345$sp')


if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

cursor.execute('drop table if exists emp')
cursor.execute('create table emp(id int, name varchar(50), sal int)')
cursor.execute('''INSERT IGNORE into emp(id, name, sal) VALUES 
            (1, 'Bob', 10000),
            (2, 'John', 20000)
''')

# second method for check inserting

try:
    cursor.execute("INSERT INTO emp(id, name, sal) VALUE(3, 'Abhy', 30000)")
    conn.commit()
except:
    conn.rollback()

cursor.execute('select * from emp')
rows = cursor.fetchall()
print("Total Number of records",cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()
