import threading
import random
import logging
# import time
#
# cont = threading.Condition()
# # event = threading.Event()
# cups = []
#
#
# def boss():
#     print("I am waiting")
#     # event.wait()
#     with cont:
#         cont.wait()
#
#     print('Good job!')
#
#
# def worker(count=100):
#     print("I'm working")
#     with cont:
#         while len(cups) < count:
#             time.sleep(0.01)
#             cups.append(1)
#         print("I finished my job. {}".format(len(cups)))
#         # cont.notify_all()  # 通知所有人
#         cont.notify(2)  # 仅仅通知两个人（老板），释放线程
#     # event.set()
#
#
# threading.Thread(target=boss).start()
# threading.Thread(target=boss).start()
# threading.Thread(target=boss).start()
# threading.Thread(target=boss).start()
# threading.Thread(target=worker).start()
#
# print("~~~~~~~~end~~~~~~~~~~~~")


class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = threading.Event()
        self.cont = threading.Condition()

    def produce(self, count=100):
        print("produce~~~~~~~")

        for i in range(count):
            self.event.wait(1)
            with self.cont:
                data = random.randint(1, 100)
                logging.info(data)
                self.data = data
                self.cont.notify_all()
            # self.event.wait(1)

    def consume(self):
        print("consume~~~~~~~~~")
        while True:
            with self.cont:
                self.cont.wait()
                data = self.data
                logging.info(data)

        # while not self.event.wait(0.5):
        #     data = self.data
        #     logging.info(data)


d = Dispatcher()
p = threading.Thread(target=d.produce)
# c = threading.Thread(target=d.consume)
for j in range(2):
    c = threading.Thread(target=d.consume, name="consume-{}".format(j))
    c.start()
p.start()
