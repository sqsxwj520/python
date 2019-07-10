import string
import shutil
import random
from pathlib import Path

lower_chars = string.ascii_lowercase
basedir = Path('f:/tmp')
sub = Path('a/b/c/d')
(basedir / sub).mkdir(parents=True, exist_ok=True)
# print(list(sub.parents))
dirs = [sub] + list(sub.parents)[: -1]

_file_names = ('{}.txt'.format(''.join(random.sample(lower_chars, 4))) for i in range(50))
# print(list(_file_names))
for file in _file_names:
    (basedir / random.choice(dirs) / file).touch()
# print('~' * 40)


def ignore(src, names):
    # ret = set()
    s = set('xyz')  # {'x', 'y', 'z'}
    # for name in names:
    #     if name[0] not in s and Path(src, name).is_file():
    #         ret.add(name)
    # print(ret)
    # return ret
    # return {name for name in names if name[0] not in s and Path(src, name).is_file()}
    return set(filter(lambda x: x[0] not in s and Path(src, x).is_file(), names))


shutil.copytree(str(basedir / 'a'), str(basedir / 'dst'), ignore=ignore)
