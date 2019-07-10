"""分析器"""
# ip分析

import re
import datetime
import threading
from pathlib import Path
from queue import Queue
from urllib.parse import urlparse
from user_agents import parse

# log_line = """123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
# "GET / HTTP/1.1" 200 8642 "-" \
# "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
# """

# regex = re.compile('([\d.]{7,}) - - \[(.*)\] "([^"]+)" (\d{3}) (\d+) "[^"]+" "([^"]+)"')
pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>.*)\] "(?P<method>.+) (?P<url>.+) \
(?P<protocol>.+)" (?P<status>\d{3}) (?P<size>\d+) "[^"]+" "(?P<useragent>[^"]+)"
'''
regex = re.compile(pattern)

conversion = {
    'datetime': lambda date_str: datetime.datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'size': int,
    'useragent': lambda ua: parse(ua)
}  # %z是时区，conversion的值是函数


def extract(line: str):

    m = regex.match(line)
    # print(m)  # 思考为什么后面的不显示,注意span的值变化
    if m:
        # print(m.groups())
        # print(m.groupdict())
        # d = {}
        # for k, v in m.groupdict().items():
        #     if k in conversion:
        #         d[k] = conversion[k](v)
        #     else:
        #         d[k] = v
        return {k: conversion[k](v) if k in conversion else v for k, v in m.groupdict().items()}
        # d2 = {k: conversion.get(k, lambda x: x)(v) for k, v in m.groupdict().items()}
    else:  # 匹配不上
        # print('xxxxx {}'.format(line))  # 输出记录一下，可以设置一个阈值，超过就提醒一下
        # raise Exception()  # 抛出异常
        # return None  # 返回None，就是说匹配失败
        pass
    # date_str = '06/Apr/2017:18:09:25 +0800'
    # dt = datetime.datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
# print(dt)


def loadfile(filename: str, encoding='utf-8'):

    with open(filename, encoding=encoding) as f:
        for line in f:
            fields = extract(line)
            if fields:
                # print(fields)
                yield fields
            else:
                print('xxxxx {}'.format(line))


# loadfile('E:\VM\slides\chapter07文本处理\logs\\test.log')


def _load(*paths, encoding='utf-8', ext='*.log', recursive=False):
    for x in paths:
        p = Path(x)
        if p.is_dir():
            if isinstance(ext, str):
                ext = [ext]
            else:
                ext = list(ext)  # 多个扩展名
            # *.log, *.txt
            for e in ext:
                files = p.rglob(e) if recursive else p.glob(e)
                for file in files:
                    yield from loadfile(str(file.absolute()), encoding=encoding)
        elif p.is_file():
            yield from loadfile(str(p.absolute()), encoding=encoding)


_load('E:\VM\slides\chapter07文本处理\logs')
# for n in _load('.'):
#     print(n)


def dispatcher(src):
    queues = []
    handlers = []

    def _reg(fn):

        q = Queue()
        queues.append(q)

        t = threading.Thread(target=fn, args=(q, ))
        handlers.append(t)

    def _run():
        for t in handlers:
            t.start()  # 注册几个，就启动几个消费者线程
            # 数据源生成数据
            for item in src:
                for q in queues:
                    q.put(item)

    return _reg, _run


_src = _load('E:\VM\slides\chapter07文本处理\logs')
reg, run = dispatcher(_src)


@reg  # handle = reg(handle)  # reg的返回值为None，此后不再用了，直接通过各线程调用
def ip_handle(q: Queue):  # IP分析，分析一段时间内，不同IP地址出现的次数，基于IP可以分析出用户的地理分布
    ips = {}
    count = 0
    while True:
        data = q.get()
        if data:  # dict
            print(data)
            ip = data['remote']
            ips[ip] = ips.get(ip, 0) + 1
            count += 1
            print(ips)
            print(len(ips.keys()), count)


@reg
def pv_handle(q: Queue):  # pv分析
    pvs = {}  # {path1: {ip1: 5, ip2: 3}}
    while True:
        data = q.get()
        path = urlparse(data['url']).path
        ip = data['remote']

        # pvs[path] = pvs.get(path, 0) + 1
        if path not in pvs.keys():
            pvs[path] = {}
        pvs[path][ip] = pvs[path].get(ip, 0) + 1
        print(pvs)


@reg
def ua_handle(q: Queue):  # UserAgent分析
    browsers = {}
    count = 0
    while True:
        data = q.get()
        browser = data['useragent'].browser
        family = browser.family
        version = browser.version[0] if len(browser.version) else 0

        key = family, version
        browsers[key] = browsers.get(key, 0) + 1
        count += 1
        print(browsers)


run()
