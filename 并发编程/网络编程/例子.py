
import logging
import random
import threading
import time


FORMAT = "[%(name)s] %(thread)8d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


def add_item(d: dict):
    count = 1
    while True:
        d[count] = random.randint(1, 10)
        count += 1
        time.sleep(0.001)


def iter_item(d: dict):
    while True:
        time.sleep(1)
        for k, v in d.items():  # 注意字典在遍历的过程中，其长度不能改变，否则直接报错
            print(k, v)
            d[k] = random.randint(100, 110)
            # RuntimeError: dictionary changed size during iteration


dic = {}
a = threading.Thread(target=add_item, name='add', args=(dic, ))
i = threading.Thread(target=iter_item, name='iter', args=(dic, ))
a.start()
i.start()
print(1, threading.enumerate())
while True:
    time.sleep(1)
    if threading.active_count() <= 2:
        print(2, threading.enumerate())
        break
print(dic.keys())

print('===end===')
