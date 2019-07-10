
from sqlalchemy import create_engine, Column, String, Integer, Enum, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship  # , scoped_session
import enum


Base = declarative_base()  # 基类

IP = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'root'
DB_NAME = 'test'
PORT = 3306

conn = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DB_NAME)

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

    departments = relationship('DeptEmp')
    title = relationship('Title')

    def __repr__(self):
        return "<{} emp_no={}, name={}, gender={}, depart_info={}, title={}>".\
            format(__class__.__name__, self.emp_no,
                   "{} {}".format(self.first_name, self.last_name),
                   self.gender.value, self.departments, self.title)


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

    depart_info = relationship('Department')

    def __repr__(self):
        return "<{} emp_no={}, dept_no={}, dept_name={}>".format(__class__.__name__, self.emp_no, self.dept_no,
                                                                 self.depart_info.dept_name)


class Title(Base):
    __tablename__ = 'titles'
    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    title = Column(String(50), primary_key=True)
    from_date = Column(Date, primary_key=True)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "<{} title={}>".format(__class__.__name__, self.title)


def show(ems):
    for x in ems:
        print(x)
    print('\n\n')


result = session.query(Employee).join(DeptEmp).filter(Employee.emp_no == DeptEmp.emp_no, Employee.emp_no == 10010)

show(result.all())
