import mysql.connector;


def delete(id):
    conn = mysql.connector.connect(host='localhost', database='employeedb', user='mydb', password='2016331086$sp')

    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()
        str = "delete from employee where emp_id='%d'" % id
        # args=(id)
        try:
            # cursor.execute(str % args)
            cursor.execute(str)
            conn.commit()
            # print("Employee Deleted")
            cursor.execute('select * from employee')
            rows = cursor.fetchall()
            print("Total Number of records", cursor.rowcount)

            for row in rows:
                print(row)
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


empId = int(input('Enter Emp Id:'))
delete(empId)
