
from sqlalchemy import create_engine, Column, String, Integer, Enum, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship  # , scoped_session
# from sqlalchemy import and_, or_, not_
from sqlalchemy import func
import enum

Base = declarative_base()  # 基类


IP = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'root'
DB_NAME = 'test'
PORT = 3306

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
# https://docs.sqlalchemy.org/en/13/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
conn = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DB_NAME)
# pymysql 是驱动
engine = create_engine(conn, echo=True)
session = sessionmaker(bind=engine)()


class MyEnum(enum.Enum):  # 枚举一般不用，建议直接写0，1
    F = 'F'
    M = 'M'


class Employee(Base):
    __tablename__ = 'employees'
    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    depart = relationship('DeptEmp')

    def __repr__(self):
        return "<{} emp_no={}, name={}, gender={}, dept={}>".format(__class__.__name__, self.emp_no,
                                                                    "{} {}".format(self.first_name, self.last_name),
                                                                    self.gender.value, self.depart)


class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(Integer, primary_key=True)
    dept_name = Column(String(40), unique=True)

    def __repr__(self):
        return "<{} dept_no={}, dept_name={}>".format(__class__.__name__, self.dept_no, self.dept_name)


class DeptEmp(Base):
    __tablename__ = 'dept_emp'
    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    dept_no = Column(Integer, ForeignKey('departments.dept_no', ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "<{} emp_no={}, dept_no={}>".format(__class__.__name__, self.emp_no, self.dept_no)


def show(ems):
    for x in ems:
        print(x)
    print('\n\n')


# eps = session.query(Employee).filter(Employee.emp_no > 10015)  # filter相当于where
# # query可以理解为select * from
# show(eps)

# and or not

# eps = session.query(Employee).filter(Employee.emp_no > 10015, Employee.emp_no < 10019)
# show(eps)

# eps = session.query(Employee).filter(Employee.emp_no > 10015).filter(Employee.emp_no < 10019)
# show(eps)

# eps = session.query(Employee).filter((Employee.emp_no > 10015) & (Employee.emp_no < 10019))
# show(eps)

# eps = session.query(Employee).filter(and_(Employee.emp_no > 10015, Employee.emp_no < 10019))
# show(eps)
#
# es = session.query(Employee).filter(or_(Employee.emp_no == 10015, Employee.emp_no == 10018))
# show(es)
#
# # es = session.query(Employee).filter((Employee.emp_no == 10015) | (Employee.emp_no == 10018))
# # show(es)
#
# ss = session.query(Employee).filter(not_(Employee.emp_no < 10019))
# show(ss)

# ss = session.query(Employee).filter(~(Employee.emp_no < 10019))
# show(ss)

# # in, 注意调用的是in_函数
# emp_list = (10010, 10019, 10021)
#
# esm = session.query(Employee).filter(Employee.emp_no.in_(emp_list))
# show(esm)
#
# # # not in
# # ems = session.query(Employee).filter(~(Employee.emp_no.in_(emp_list)))
# # show(ems)
#
# # like
# ms = session.query(Employee).filter(Employee.first_name.like('P%'))
# show(ms)
#
#
# # # not like,ilike默认不区分大小写
# # mse = session.query(Employee).filter(Employee.last_name.notlike('M%'))
# # show(mse)
#
# sm = session.query(Employee).filter(Employee.emp_no > 10017).order_by(Employee.emp_no)
# show(sm)
#
# sme = session.query(Employee).filter(Employee.emp_no > 10017).\
#     order_by(Employee.gender).order_by(Employee.emp_no.desc())
# # 注意Employees.gender不是按照升序排列的，而是类变量的定义顺序，暂时还是有问题，明天继续探索？
# show(sme)

# 分页
sem = session.query(Employee).filter(Employee.emp_no > 10015).limit(2).offset(2)
show(sem)


# 消费者方法,消费者方法调用后，Query对象就转换成了一个容器
ps = session.query(Employee)
# print(ps.count())  # 聚合函数count(*)的查询，用了子查询，效率不高
print(len(list(ps)))
# for i in ps:
#     print(i)

print(ps.all())  # 结果是列表，列表中是21个对象，查不到返回空列表
print(ps.first())  # 返回行首，查不到返回None

# print(ps.one())  # 有且只能有一行，如果查询结果是多行则抛异常

# 删除 delete
# session.query(Employee).filter(Employee.emp_no > 10019).delete()
# session.commit()  # 提交后就真的删除了


# # 聚合、分组
# query = session.query(func.count(Employee.emp_no))
# print(query.all())  # [(21,)]，结果是列表
# print(query.first())  # (21,)，结果是元组
# print(query.one())  # (21,),结果是元组
# print(query.scalar())  # 21，取one的第一个元素
query = session.query(Employee.gender, func.count(Employee.emp_no)).group_by(Employee.gender).all()

print(query)
# [(<MyEnum.M: 'M'>, 13), (<MyEnum.F: 'F'>, 8)]
for g, y in query:
    print(g)
    print(g.value, y)
print("~~~~~~~~~~~~~~~")


# 关联查询
# 查询10010员工的所在部门编号及员工信息
result = session.query(Employee, DeptEmp).filter(Employee.emp_no == DeptEmp.emp_no, Employee.emp_no == 10010).all()
# 隐式连接等价于
"""\
SELECT *
from employees, dept_emp
where employees.emp_no = dept_emp.emp_no and employees.emp_no = 10018;
"""
show(result)  # 结果是两个对象

# 使用join
# results = session.query(Employee).join(DeptEmp).filter(Employee.emp_no == 10010).all()
# show(results)

# results = session.query(Employee).join(DeptEmp, Employee.emp_no == DeptEmp.emp_no).\
#           filter(Employee.emp_no == 10010).all()
#
# show(results)


results = session.query(Employee).join(DeptEmp, (Employee.emp_no == DeptEmp.emp_no) & (Employee.emp_no == 10010))
show(results.all())  # 注意返回的结果是一个对象
# <Employee emp_no=10010, name=Duangkaew Piveteau, gender=F, dept=[<DeptEmp emp_no=10010, dept_no=d004>,
# <DeptEmp emp_no=10010, dept_no=d006>]>

for j in results:
    print(j)
    print(j.emp_no)  # 10010
    print(j.departments)
    # [<DeptEmp emp_no=10010, dept_no=d004>, <DeptEmp emp_no=10010, dept_no=d006>]
