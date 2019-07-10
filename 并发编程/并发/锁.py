# from threading import Lock
# import time
# import threading
# import logging
#
#
# FORMAT = "%(asctime)s %(threadName)s % (thread)d %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
# cups = []
# lock = Lock()
#
#
# def worker(count):
#     logging.info("{} is working".format(threading.current_thread().name))
#     flag = False
#     while True:
#         time.sleep(0.1)
#         lock.acqure()
#         if len(cups) >= count:
#             flag = True
#         if not flag:
#             cups.append(1)
#         if flag:
#             break
#     logging.info("{} finished my job. cups={}".format(threading.current_thread().name, len(cups)))
#
#
# for i in range(10):
#     threading.Thread(target=worker, name="worker-{}".format(i + 1), args=(1000, )).start()


import threading
from threading import Thread, Lock
import logging
import time


FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

cups = []
lock = Lock()


def worker(l: threading.Lock, count=10):
    logging.info("I'm working for U.")
    flag = False
    while True:
        l.acquire()  # 加了一把锁，只有当前线程能使用该资源，其他线程全部阻塞

        if len(cups) >= count:
            flag = True
        time.sleep(0.0001)  # 为了看出线程切换效果
        # l.release()
        #  此位置不能释放锁，假设此时已经生产了999个杯子，此时释放锁，很多线程都可以看到999个杯子，没到1000，会继续生产，结果肯定会超过1000
        if not flag:
            cups.append(1)
        l.release()
        if flag:  # 注意flag是局部变量，线程之间互不干扰，线程函数压栈是独立的
            break
        # l.release()  # 此位置不行，前面假设已经生产了1000，直接break了，不会再释放锁，就形成了死锁
    logging.info('I finished. cups = {}'.format(len(cups)))


for _ in range(10):
    Thread(target=worker, args=(lock, 1000)).start()
