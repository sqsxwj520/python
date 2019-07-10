import sqlalchemy
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html,如何使用sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, aliased
# from sqlalchemy.orm.state import InstanceState


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


session = sessionmaker(bind=engine)()


# def get_state(instance, i):
#     state: InstanceState = sqlalchemy.inspect(instance)
#     output = "{} :{} {} \n"\
#         "attached={}, transient={}, pending={}\n"\
#         "persistent={}, deleted={}, detached={}\n".format(i, state.key, state.session_id,
#                                                           state._attached, state.transient, state.pending,
#                                                           state.persistent, state.deleted, state.detached)
#     print(output, end="~~~~~~~~~~~~~~~\n")
#
#
# student = session.query(Student).get(2)
# get_state(student, 1)  # persistent
#
# try:
#     student = Student(id=5, name='AD', age=28)
#     get_state(student, 2)  # transient
#
#     student = Student(id=6, name='Durant', age=32)
#     get_state(student, 3)  # transient
#     session.add(student)
#     get_state(student, 4)  # pending
#
#     session.commit()
#     get_state(student, 5)  # persistent
#
# except Exception as e:
#     session.rollback()
#     print(e, '~~~~~~~~~~~~')
#
# student = session.query(Student).get(6)
# get_state(student, 6)  # persistent
#
# try:
#     session.delete(student)
#     get_state(student, 7)  # persistent(未flush)
#
#     session.flush()
#     get_state(student, 8)  # deleted
#     session.commit()
#     get_state(student, 9)  # detached(分离)
# except Exception as e:
#     session.rollback()
#     print('++++++++++++++++')
#     print(e)

# Querying

for ins in session.query(Student).order_by(Student.id):
    print(ins.name, ins.age)

for name, age in session.query(Student.name, Student.age):
    print(name,  age)

for row in session.query(Student, Student.name).all():
    print(row.Student, row.name)
    """\
    <id='1', name='Klay', age='28'> Klay
    <id='2', name='Curry', age='31'> Curry
    <id='3', name='Kevin', age='32'> Kevin
    <id='4', name='Green', age='29'> Green
    """

for row in session.query(Student.name.label('name_label')).all():
    # 给字段name添加标签
    print(row.name_label)

s = aliased(Student, name='student_alias')  # 相当于给表取别名为name(student_alias)
for row in session.query(s, s.name).all():
    # print(row)
    """
    (<id='1', name='Klay', age='28'>, 'Klay')
    (<id='2', name='Curry', age='31'>, 'Curry')
    (<id='3', name='Kevin', age='32'>, 'Kevin')
    (<id='4', name='Green', age='29'>, 'Green')
    """
    print(row.student_alias)
    """
    <id='1', name='Klay', age='28'>
    <id='2', name='Curry', age='31'>
    <id='3', name='Kevin', age='32'>
    <id='4', name='Green', age='29'>
    """

for u in session.query(Student).order_by(Student.id).limit(1).offset(3):
    print(u)
    """
   <id='4', name='Green', age='29'>       
    """
for name, in session.query(Student.name).filter_by(name='Curry'):
    print(name)  # Curry

# # 等价于下面的sql语句
# for name, in session.query(Student.name).filter(Student.name == 'Curry'):
#     print(name)

# for name in session.query(Student.name).filter_by(name='Curry'):
#     print(name)  # ('Curry',),注意与上面查询结果的区别

que = session.query(Student.name).filter(Student.name.match('Curry'))
print(que)
