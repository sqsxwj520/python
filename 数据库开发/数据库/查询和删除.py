import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # , scoped_session
from sqlalchemy.orm.session import Session


IP = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'root'
DB_NAME = 'test'
PORT = 3306

print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DB_NAME), echo=True)
# +之间不能有空格，否则会出错
print(engine)

Base = declarative_base()  # 基类


class Student(Base):
    __tablename__ = 'student1'  # __tablename__是类的私有属性，不能改名字

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
    # 字段名与属性名一致，可以省略不写
    name = Column(String(64), nullable=False)  # nullable不可为空
    age = Column(Integer)

    def __repr__(self):
        return "<{} id={}, name={}, age={}>".format(__class__.__name__, self.id, self.name, self.age)


Base.metadata.create_all(engine)  # 创建继承自Base的所有表


# Session = scoped_session(sessionmaker(bind=engine))  # 线程是安全的
session: Session = sessionmaker(bind=engine)()  # 线程不安全
# print(session, type(session))

student = session.query(Student).get(2)  # 先查后改，先查后删

student.age = 33
student.name = 'KD'

# session.add(student)
session.delete(student)

try:
    session.commit()
    print('commit ok')

except Exception as e:
    session.rollback()
    print(e)
    print('rollback')
