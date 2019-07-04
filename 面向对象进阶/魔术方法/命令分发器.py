class Dispatcher:
    def __init__(self):
        pass

    def reg(self, name, fn):
        setattr(self, name, fn)

    def run(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit':
                break

            getattr(self, cmd, lambda: print('Unknown command {}'.foramt(cmd)))()


d = Dispatcher()
d.reg('ls', lambda: print('ls command'))
print(d.__dict__)  # {'ls': <function <lambda> at 0x00000000021E3A60>}
d.run()
