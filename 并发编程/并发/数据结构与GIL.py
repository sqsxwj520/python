
import threading
import logging
import datetime
#
#
# q = queue.Queue()
# #
# # def work():
# #     if q.qsize() == 1:
# #         print(q.get())  # 多线程会有问题，就是多个线程都看到还有一个数据，一个拿到了，其他的线程必然拿不到
# print(q.get(timeout=2))

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i=0):
    total = 0
    for i in range(1000000000):
        total += 1
    logging.info(total)
    return i, total


t1 = threading.Thread(target=calc, args=(1, ))
t2 = threading.Thread(target=calc, args=(2, ))
t3 = threading.Thread(target=calc, args=(3, ))
t4 = threading.Thread(target=calc, args=(4, ))
t1.start()  # 注意python中的多线程是假多线程，实际上是串行
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

start = datetime.datetime.now()
# calc()
# calc()
# calc()
# calc()
delta = (datetime.datetime.now() - start).total_seconds()
# print(delta)
logging.info(delta)
