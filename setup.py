#!/usr/bin/env python

from distutils.core import setup
import glob

setup(name='blog',
      version='1.0',
      description='博客项目',
      author='sun',
      author_email='17826854776@163.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['blog', 'user', 'post', 'utils', 'templates'],
      py_modules=['manage'],  # 直接打包.py文件
      data_files=glob.glob('templates/*.html') + ['requirements']  # 可以将.html的所有文件进行打包，还可以加其他类型的文件
      )
