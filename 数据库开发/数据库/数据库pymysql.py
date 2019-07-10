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

    sql = "insert into student(name, age) values('Curry', 31)"
    sql2 = "select id from student where name='Curry'"

    cursor = conn.cursor()

    r = cursor.execute(sql2)
    print(r)  # 影响的行数

    if r == 1:
        student_id = cursor.fetchone()
        print(student_id)
        sql = "update student set name='Klay' where id={}".format(student_id)
        cursor.execute(sql)

    conn.commit()  # 要和rollback同时使用
except Exception as e:
    conn.rollback()
    print(e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
