"""
程序员可以方便的注册函数到某一个命令，用户输入命令时，路由到注册的函数
如果此命令没有对应的注册函数，执行默认函数
用户输入用input(">>")
"""


def command_dispatcher():

    commands = {}

    def _reg(name):

        def wrapper(fn):

            commands[name] = fn
            return fn
        return wrapper

    def default_func():

        print('Unknown command')

    def _dispatcher():

        while True:
            cmd = input('>>>')
            if cmd.strip() == '':
                break
            commands.get(cmd, default_func)()

    return _reg, _dispatcher


reg, dispatcher = command_dispatcher()


@reg('f1')  # foo1 = reg('f1')(foo1)
def foo1():

    print('foo1')


@reg('f2')
def foo2():

    print('foo2')


dispatcher()
