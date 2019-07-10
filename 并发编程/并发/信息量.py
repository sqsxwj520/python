import threading
import uuid
# import logging
# import time

# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.INFO)

# s = threading.Semaphore(3)
# print(s.acquire())
# print(s.acquire())
# print(s.acquire())
# # print(s.acquire())
# # print(s._value)
# # print(s.release())
# # print(s.release())
# # print(s._value)
# # print(s.release())
# # print(s._value)
# threading.Thread(target=lambda a: a.acquire(), args=(s, )).start()
# threading.Event().wait(2)
# print(s.__dict__)


class Conn:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4().hex


class ConnPool:  # 连接池
    def __init__(self, count=5):
        self.count = count
        self.__conns = [self._connection("conn-{}".format(i + 1)) for i in range(count)]
        # self.__lock = threading.Lock()
        self.sema = threading.BoundedSemaphore(count)

    @staticmethod
    def _connection(name):
        return Conn(name)

    def get_conn(self):
        # with self.__lock:  # 拿或者还的时候，只能有一个线程能操作
        #     if len(self.__conns) > 0:
        #         return self.__conns.pop()
        self.sema.acquire()
        return self.__conns.pop()

    def return_conn(self, conn: Conn):
        # with self.__lock:
        #     if len(self.__conns) < self.count:
        #         self.__conns.append(conn)
        self.__conns.append(conn)
        # 不需要考虑有大于count数量的人来归还，因为只有count个线程拿到了，其他线程都阻塞了，所有最多只有count线程来归还
        self.sema.release()  # 不能放在self.__conns.append(conn)上面
        # 如果先release，_value值增加1，但是实际上还没有归还，那么速度快的线程，看到release了，就去列表中去拿，实际上还没有归还


# cp = ConnPool()
# threading.Thread(target=cp.get_conn())
