# from distutils.core import setup
from setuptools import setup

setup(name='m',
      version='1.0',
      description='m project',
      author='野马',
      author_email='17826854776@163.com',
      url='https://mp.csdn.net',
      packages=['m', 'm.m2', 'm.m2.m21'],  # 会打包最后m21内的所有文件（m21内没有子包了）
      # 注意这里只能放包，不会递归打包包内的子包和 __init__.py文件和.py文件
      )


# terminal中，输入 python setup.py build; python setup.py install

# 在site-packages中多了一个m包
