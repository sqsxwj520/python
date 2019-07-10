import sqlalchemy
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html,如何使用sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


print(sqlalchemy.__version__)

IP = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'root'
DB_NAME = 'test'
PORT = 3306

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
# https://docs.sqlalchemy.org/en/13/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
conn = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DB_NAME)
# pymysql是驱动

engine = create_engine(conn, echo=True)
# echo=True 引擎是否打印执行的语句
print(engine)
# Engine(mysql+pymysql://root:***@127.0.0.1:3306/test)
# lazy connecting: 懒连接，创建引擎不会马上连接数据库，直到让数据库执行任务时才连接

Base = declarative_base()  # 基类


class Student(Base):
    __tablename__ = 'students'

    # 字段名和属性名一致时，字段名可以省略不写
    id = Column(Integer, primary_key=True)  # 定义字段类型和属性
    name = Column(String(40), nullable=False)
    age = Column(Integer, nullable=False)
    # age = Column('age', Integer, nullable=False)

    def __repr__(self):
        # return "<{} id={}, name={}, age={}>".format(__class__.__name__, self.id, self.name, self.age)
        # 推荐使用C风格的写法
        return "<id='%s', name='%s', age='%s'>" % (self.id, self.name, self.age)


print(Student.__dict__)
# print(Student.__table__)  # 没有出自己想要的结果（默认调用str方法），可以调用一下repr方法
print(repr(Student.__table__))

Base.metadata.create_all(engine)  # 创建继承自Base的所有表
# Base.metadata.drop_all(engine)

student = Student(name='James', age=35)
print(student.name, student.age, student.id)

session = sessionmaker(bind=engine)()  # 线程不安全，不适用多线程

student = Student(id=1, name='James', age=28)
session.add(student)

session.commit()

try:
    student.name = 'Klay'
    session.add_all([
        Student(id=2, name='Curry', age=31),
        Student(id=3, name='KD', age=32),
        Student(id=4, name='Green', age=29)
    ])

    session.commit()
    print('~~~~~~~~~~~~~~~')
except Exception as e:
    session.rollback()
    print(e)
    print('+++++++++++++++++')

students = session.query(Student)
print(students)  # 无内容，惰性的
for s in students:
    print(s)
print('-----------------')

"""\
<id='1', name='Klay', age='28'>
<id='2', name='Curry', age='31'>
<id='3', name='KD', age='32'>
<id='4', name='Green', age='29'>
"""
student = session.query(Student).get(2)  # 通过主键查询
print(student)

# <id='2', name='Curry', age='31'>

student = session.query(Student).get(3)  # 必须先查出来，然后修改，最后在提交
print(student)
# <id='3', name='KD', age='32'>

student.name = 'Kevin'
student.age = 32
print(student)
# <id='3', name='Kevin', age='32'>
session.add(student)
session.commit()
