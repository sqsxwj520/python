import sqlalchemy
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html,如何使用sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


print(sqlalchemy.__version__)

# Session = sessionmaker()

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

Base = declarative_base()  # 基类


class Student(Base):
    __tablename__ = 'students'

    # 字段名和属性名一致时，字段名可以省略不写
    id = Column(Integer, primary_key=True)  # 定义字段类型和属性
    name = Column(String(40), nullable=False)
    age = Column(Integer, nullable=False)

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

# Session.configure(bind=engine)
# session = Session()
session = sessionmaker(bind=engine)()  # 线程不安全，不适用多线程
ed_student = Student(id=1, name='Klay', age=28)
session.add(ed_student)

# my_student = session.query(Student).filter_by(name='Klay').first()
# print(my_student)
# [<id='1', name='Klay', age='28'>]

# print(ed_student is my_student)  # True

try:
    session.add_all([
        Student(id=2, name='Curry', age=31),
        Student(id=3, name='KD', age=32),
        Student(id=4, name='Green', age=29)
    ])

    # ed_student.name = 'Lunny'  # 会默认覆盖第一个对象
    # print(session.dirty)
    # # IdentitySet([<id='1', name='Lunny', age='28'>])
    #
    # print(session.new)
    # # IdentitySet([<id='2', name='Curry', age='31'>, <id='3', name='KD', age='32'>, <id='4', name='Green', age='29'>])

    session.commit()
    print('~~~~~~~~~~~~~~~')
except Exception as e:
    session.rollback()
    print(e)
    print('+++++++++++++++++')
