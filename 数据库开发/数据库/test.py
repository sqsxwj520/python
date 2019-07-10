import pymysql
from pymysql.cursors import DictCursor


IP = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'root'
DB_NAME = 'test'
PORT = 3306

conn = pymysql.connect(IP, USERNAME, PASSWORD, DB_NAME, PORT)
cursor = conn.cursor(DictCursor)

_id = '6 or 1=1'
# sql = "select * from student where id={}".format('1 or 6=6')  # 拼接字符串，相当有风险
# print(sql)  # select * from student where id=1 or 6=6, 6=6是True，相当于where True，所以会显示所有信息
# cursor.execute(sql)

# sql = "select * from student where id=%s"  # C风格的
sql2 = "select * from student where name=%(n)s and id=%(a)s"
print(sql2)
# r = cursor.execute(sql, (_id, ))  # 参数化查询，后面的数据类型可以是列表、元组、字典
# print(r)
r = cursor.execute(sql2, {'n': 'Curry', 'a': 5})
print(r)

for x in cursor.fetchall():
    print(x)
