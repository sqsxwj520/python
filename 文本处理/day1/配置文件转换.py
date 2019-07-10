"""配置文件转换
有一个配置文件test.ini内容如下，将其转换json格式文件

"""
import json
from configparser import ConfigParser

src = 'c:/mysql.ini'
dst = 'c:/mysql.json'

cfg = ConfigParser()
cfg.read(src)

d = {}
for s in cfg.sections():
    print(s)
    print(cfg.items(s))
    d[s] = dict(cfg.items(s))

with open(dst, 'w') as f:
        json.dump(d, f)
