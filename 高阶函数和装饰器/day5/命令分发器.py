
"""完善命令分发器，实现函数可以带任意参数（可变参数除外），解析参数并要求用户输入"""


def command_dispatcher():

    commands = {}

    def reg(name):

        def _reg(fn):

            commands[name] = fn
            return fn
        return _reg

    def default_func():

        print('Unknown command')

    def dispatcher():

        while True:
            cmd = input('>>>')
            if cmd.strip() == '':
                return
            fname, *params = cmd.replace(',', ' ').split()  # 右边是列表
            args = []
            kwargs = {}
            for param in params:
                x = param.split('=', maxsplit=1)  # 切割完都是字符串
                if len(x) == 1:  # 顺序传参
                    args.append(int(x[0]))
                elif len(x) == 2:
                    kwargs[x[0]] = int(x[1])  # a=1,切割成['a', '1']

            commands.get(fname, default_func)(*args, **kwargs)

    return reg, dispatcher


reg, dispatcher = command_dispatcher()


@reg('f1')  # foo1 = reg('f1')(foo1)
def foo1():

    print('foo1')


# 方法二
@reg('f2')
def foo2(a: int, b: int=100):

    print('foo2', a, b, a + b)


dispatcher()
