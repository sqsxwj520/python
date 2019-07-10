
"""完善命令分发器，实现函数可以带任意参数（可变参数除外），解析参数并要求用户输入"""


def command_dispatcher():

    commands = {}

    def _reg(name, *args, **kwargs):

        def wrapper(fn):

            commands[name] = fn, args, kwargs
            return fn
        return wrapper

    def default_func():

        print('Unknown command')

    def _dispatcher():

        while True:
            cmd = input('>>>')
            if cmd.strip() == '':
                break
            fn, args, kwargs = commands.get(cmd, (default_func, (), {}))  # 注意如果找不到，缺省值需要注意
            fn(*args, **kwargs)

    return _reg, _dispatcher


reg, dispatcher = command_dispatcher()


# 方法一
@reg('f3', x=100, y=200)
@reg('f1', 200, 300)  # foo1 = reg('f1')(foo1)
def foo1(x, y):

    print('foo1', x, y, x + y)


@reg('f2')
def foo2():

    print('foo2')


dispatcher()
