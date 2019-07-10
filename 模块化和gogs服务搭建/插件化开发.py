# # test.py
# class A:
#     def show_me(self):
#         print('I am A')
#
#
# #主模块
# if __name__ == '__main__':
#     mod = __import__('test')
#     cls = getattr(mod, 'A')  # ——> cls = A
#     cls().show_me()  # I am A


import importlib


def plugin_load(plugin_name: str, sep=':'):
    m, _, c = plugin_name.partition(sep)
    mod = importlib.import_module(m)
    cls = getattr(mod, c)
    return cls()


if __name__ == '__main__':
    a = plugin_load('test:A')
    a.show_me()  # I am A
