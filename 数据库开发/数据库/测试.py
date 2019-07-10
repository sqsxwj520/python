import pymysql


IP = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'root'
DB_NAME = 'test'
PORT = 3306

conn = None  # 对结果集的操作
cursor = None

try:
    conn = pymysql.connect(IP, USERNAME, PASSWORD, DB_NAME, PORT)
    # print(conn)

    # conn.ping(False)  # 连接过程中出现错误或连接失败，是否需要重新连接，False为不重新连接

    # sql = 'select * from employees'
    sql3 = "delete from employees where emp_no=10001"
    sql4 = "insert into employees(emp_no, birth_date, first_name, last_name, gender, hire_date)\
            values(10021, '1945-09-01','curry', 'Jack', 'M', '1988-07-08')"
    # sql2 = "insert into employees() values()"
    # r = conn.query(sql)
    # print(r)
    # print(type(r))

    sql5 = "select emp_no from employees where first_name='Curry'"

    sql6 = 'select * from employees'
    cursor = conn.cursor()

    r = cursor.execute(sql5)
    print(r)  # 影响的行数

    if r == 1:
        first_name = cursor.fetchone()
        print(first_name)  # 结果是元组

    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print('~~~~~~~~~~~~')
    # print(cursor.fetchmany(5))
    # print('~~~~~~~~~~~~~~~')
    # print(cursor.fetchall())
    # print('~~~~~~~~~~~~')
    # cursor.rownumber = 0
    # print(cursor.fetchall())

    conn.commit()  # 要和rollback同时使用
except Exception as e:
    conn.rollback()
    print(e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
