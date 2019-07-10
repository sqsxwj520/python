"""选择一个已经存在的目录作为当前工作目录，在其下创建a/b/c/d这样的子目录结构并
在这些子目录的不同层级生成50个普通文件，要求文件名由4个随机的小写字母构成。
将a目录下所有内容复制到当前工作目录dst下，要求复制的普通文件的文件名必须是以x、y、z开头。
"""
import random
import shutil
from string import ascii_lowercase
from pathlib import Path

basedir = Path('d:/tmp')
sub = Path('a/b/c/d')
dirs = [sub] + list(sub.parents)[:-1]

print(basedir / sub)
(basedir / sub).mkdir(parents=True, exist_ok=True)

# for i in range(50):
#     _file_names = random.choices(ascii_lowercase, k=4)  # choices拿出的元素不会重复
#     print(_file-names)
_file_names = (''.join(random.choices(ascii_lowercase, k=4)) for i in range(50))
# print(list(_file_names))

# print([sub] + list(sub.parents)[:-1])
for filename in _file_names:
    (basedir / random.choice(dirs) / filename).touch()
print('~' * 30)


def ignore(src, names, s=set('xyz')):
    # ret = set()
    # print(src, type(src))

    # for name in names:
    #     # if name.startswith('x') and name.startswith('y') and name.startswith('z'):
    #     if name[0] not in s and Path(src, name).is_file():
    #         ret.add(name)
    # print(ret)
    # return ret
    # return {name for name in names if name[0] not in s  and Path(src, name).is_file()}
    return set(filter(lambda name: name[0] not in s and Path(src, name).is_file(), names))


shutil.copytree(str(basedir / 'a'), str(basedir / 'dst'), ignore=ignore)
