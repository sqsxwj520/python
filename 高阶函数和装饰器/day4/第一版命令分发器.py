
"""
程序员可以方便的注册函数到某一个命令，用户输入命令时，路由到注册的函数
如果此命令没有对应的注册函数，执行默认函数
用户输入用input(">>")
"""

cmds = {}


def x(fn, name):

    cmds[name] = fn


def _default():

    print('default function')


def check():

    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            return
        cmds.get(cmd, _default)()


def f1():

    print('f1')


def f2():

    print('f2')


x(f1, 'a')

x(f2, 'b')

check()
