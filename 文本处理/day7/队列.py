import queue
import threading
import time

q = queue.Queue()

q.put(1)  # 默认也是阻塞的（True），可以设置超时时间，超过此时间仍然不能put的话，会抛异常

q.put('abc')

print(q.get())
print(q.get())
# print(q.get())  # 队列中没有数据了，会阻塞，默认会一等等待，直到天老天荒
# print(q.get(True, 5))  # True为阻塞（默认值），阻塞时间为5秒，拿不到数据的话，会抛异常
# print(q.get_nowait())  # 不等待，拿不到数据就会抛异常，能拿到数据，就ok
# print(q.get(False))  # False非阻塞，拿不到数据，就抛异常


def handle(p: queue.Queue):  # p为局部变量
    time.sleep(5)
    p.put('xyz')


# 线程————threading模块
t = threading.Thread(target=handle, args=(q, ))  # 创建线程对象,args必须为元组，q为全局变量
t.start()  # 启动线程


print(q.get())  # 5秒钟之后，给q中放入一个数据，然后此语句就不在阻塞了

# 进程是国与国的关系，线程是省与省的关系
