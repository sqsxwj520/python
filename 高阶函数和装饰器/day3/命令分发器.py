

# 第四题
from functools import partial


cmds = {}


def f(name, *args, **kwargs):
    def _x(fn):
        newfunc = partial(fn, *args, **kwargs)

        cmds[name] = newfunc
        return newfunc
    return _x


def _default1():

    print('default function')


def check():

    while True:

        cmd = input('>>>')
        if cmd == 'quit':
            return
        cmds.get(cmd, _default1)()


@f('a', 200, 300)   # f1 = @x('a')(f1)
def f1(x, y):

    return x + y


@f('b', 500, 600)
def f2(m, n):

    return m - n


check()
