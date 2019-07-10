import argparse

parser = argparse.ArgumentParser(prog='ls', description='list files', add_help=True)

# parser.add_argument('a', nargs="?", default='.')  # a为必须提供的位置参数，且必须是一个
parser.add_argument('path', nargs="?", default='.')  # ?表示可有可无；*表示可以任意个；+表示至少一个
parser.add_argument('-b')

parser.print_help()
print('~' * 30)

args = parser.parse_args(('/etc', ))  # 解析你提供的参数是否满足现在的定义;必须是字符串，不能为整型；且只能为一个
print(args)
print(args.b, args.path)
