# from threading import Thread
# import time
# import threading
# import logging
#
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'  # 注意%后不能有空格
# logging.basicConfig(format=FORMAT, level=logging.INFO)
# # flag = False
# event = threading.Event()
#
#
# def worker(e, count=10):
#     # global flag
#     logging.info("I'm working for U")
#     cups = []
#     while True:
#         time.sleep(1)
#         if len(cups) >= count:
#             e.set()
#             break
#         cups.append(1)
#     logging.info("I finish my job. {}".format(len(cups)))
#     # flag = True
#
#
# def boss(e):
#     logging.info("I'm boss, waiting U")
#     # while not flag:
#     #     time.sleep(1)
#     e.wait()
#     logging.info("Good job")
#
#
# b = Thread(target=boss, name='boss', args=(event, ))
# w = Thread(target=worker, name='worker', args=(event, 10))
#
# w.start()
# b.start()
# print("++end++")  # 注意此语句的输出顺序不是固定的
# """\
# ++end++
# 2019-06-09 20:03:24,950 boss 8780 I'm boss, waiting U
# 2019-06-09 20:03:24,950 worker 8288 I'm working for U
# 2019-06-09 20:03:36,006 worker 8288 I finish my job. 10
# 2019-06-09 20:03:36,006 boss 8780 Good job
# """

# from threading import Event, Thread
# import logging
#
#
# logging.basicConfig(level=logging.INFO)
#
#
# def do(event: Event, interval: int):
#     while not event.wait(interval):  # 条件中使用，返回True或者False
#         logging.info('do sth.')
#
#
# e = Event()
# Thread(target=do, args=(e, 3)).start()
# e.wait(10)  # 也可以使用time.sleep(10)
# e.set()
# print('main exit')
# """\
# INFO:root:do sth.
# INFO:root:do sth.
# INFO:root:do sth.
# main exit
# """
from threading import Event, Thread
import datetime
import logging
# FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
logging.basicConfig(level=logging.INFO)


def add(x: int, y: int):
    logging.info(x + y)


class Timer:
    def __init__(self, interval, fn, *args, **kwargs):
        self.interval = interval
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.event = Event()

    def start(self):
        Thread(target=self.__run).start()

    def cancel(self):
        return self.event.set()

    def __run(self):
        start = datetime.datetime.now()
        logging.info('waiting')
        self.event.wait(self.interval)
        if not self.event.is_set():
            self.fn(*self.args, **self.kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        logging.info('finished {}'.format(delta))
        self.event.set()


t = Timer(10, add, 4, 50)
t.start()
# t.cancel()
e = Event()
e.wait(4)
print("+++++++++end+++++++++")

"""\
INFO:root:waiting
+++++++++end+++++++++
INFO:root:54
INFO:root:finished 10.00982
"""
