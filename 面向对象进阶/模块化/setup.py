# from distutils.core import setup
# from setuptools import setup
#
#
# setup(name='m', version='1.0', description='m project', author='Greg Ward', author_email='gward@python.net',
#       url='https://www.python.org/sigs/distutils-sig/', packages=['m'], )
from importlib import import_module


def plugin_load(plugin_name: str, sep=':'):
    m, _, c = plugin_name.partition(sep)
    mod = import_module(m)
    cls = getattr(mod, c)
    return cls()


if __name__ == '__main__':
    obj = plugin_load('test: A')
    obj.show()
