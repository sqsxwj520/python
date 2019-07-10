"""实现ls命令功能
实现ls命令功能，实现-l、-a和-all、-h选项
实现显示路径下的文件列表
-a和-all显示包含.开头的文件
-l详细列表显示
-h和-l配合，人性化显示文件大小，例如1K、1G、1T等，可以认为1G=1000M

"""
import argparse
import datetime
from pathlib import Path


parser = argparse.ArgumentParser(prog='ls', description='list files', add_help=False)
# add_help为False时，可以有-h参数，add_help为True时，不能有-h参数

# parser.add_argument('a', nargs="?", default='.')  # a为必须提供的位置参数，且必须是一个
parser.add_argument('path', nargs="*", default='E:\VM\\videos\chapter01Python入门\\20190325')  # ?表示可有可无；*表示可以任意个；+表示至少一个
parser.add_argument('-l', action='store_true')  # store_true,-l给了，args.l就是True；store_false正好相反
parser.add_argument('-a', '--all', action='store_true')
parser.add_argument('-h', '--human-readable', action='store_true', dest='human')
# dest只改变Namespace中的显示，本来为human-readable,现在为human

parser.print_help()
print('~' * 30)

args = parser.parse_args(['-lah'])  # 解析你提供的参数是否满足现在的定义;必须是字符串，不能为整型；且只能为一个
print(args)
# print(args.l, args.path, args.a, args.h)


def get_file_type(p: Path):
    if p.is_dir():
        return 'd'
    elif p.is_symlink():
        return 'l'
    elif p.is_socket():
        return 's'
    elif p.is_char_device():
        return 'c'
    elif p.is_block_device():
        return 'b'
    else:
        return '-'


_mode_str = list('rwx' * 3)


# def get_mode_str(mode: int):
#     # m = '{:9b}'.format(mode)
#     # m = bin(mode)[-9:]
#     _m_str = ''
#     for i, x in enumerate('{:9b}'.format(mode)[-9:]):
#         _m_str += _mode_str[i] if x == '1' else '-'
#     return _m_str


def get_mode_str(mode: int):
    # m = '{:9b}'.format(mode)
    # m = bin(mode)[-9:]
    _m_str = ''
    for i in range(8, -1, -1):
        _m_str += _mode_str[8 - i] if mode >> i & 1 else '-'
    return _m_str


def get_human_str(size: int) -> str:
    units = " KMGTP"  # 字符串是字面常量，每次调用不会重复创建
    # units = ['', 'K', 'M', 'G', 'T', 'P']  # 列表的坏处是每次调用都要创建，非要用列表的话，可以将列表放在函数外，或者作为函数的缺省参数
    index = 0
    length = len(units)
    while size >= 1000 and index < length - 1:  # and后是考虑边界问题
        size //= 1000
        index += 1

    return '{}{}'.format(size, units[index])


# print(_get_human_str(1300))  # 1k
# print(_get_human_str(1300000))  # 1M
# print(_get_human_str(130))  # 130


def list_dir(path, detail=False, _all=False, human=False):
    p = Path(path)
    # if not p.exists() or not p.is_dir():
    #     return
    ret = []
    for f in p.iterdir():
        if not _all and f.name.startswith('.'):
            continue
        if not detail:
            ret.append((f.name, ))
        else:
            typ = get_file_type(f)
            st = f.stat()
            # print(st)
            dt = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m%d %H:%M:%S')
            mode = get_mode_str(st.st_mode)
            size = get_human_str(st.st_size) if human else st.st_size
            ret.append((typ, mode, st.st_nlink, st.st_uid, st.st_gid, size, dt, f.name))

        # print(type(f), str(f), f.name)

    return ret


file_list = list_dir(args.path, args.l, args.all, args.human)
print(sorted(file_list, key=lambda x: x[-1]))
