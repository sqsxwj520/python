import argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='ls', description='list files', add_help=True)

# parser.add_argument('a', nargs="?", default='.')  # a为必须提供的位置参数，且必须是一个
parser.add_argument('path', nargs="?", default='.')  # ?表示可有可无；*表示可以任意个；+表示至少一个
parser.add_argument('-l', action='store_true')  # store_true,-l给了，args.l就是True；store_false正好相反

parser.print_help()
print('~' * 30)

args = parser.parse_args()  # 解析你提供的参数是否满足现在的定义;必须是字符串，不能为整型；且只能为一个
print(args)
print(args.l, args.path)


def listdir(path):
    p = Path(path)
    # if not p.exists() or not p.is_dir():
    #     return
    ret = []
    for f in p.iterdir():
        print(type(f), str(f), f.name)
        ret.append(f.name)
    return ret


print(listdir('.'))
print(listdir(args.path))
