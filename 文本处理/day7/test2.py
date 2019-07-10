# 分发 生产者消费者模型
import queue
import threading
import time

q = queue.Queue()

q.put(1)
q.put('abc')

print(q.get())  # queue满了，也会阻塞，会阻塞到队列可以put为止。也可以设置阻塞时间，超过时间仍然不能put的话，直接抛出异常
print(q.get())
# print(q.get(True, 5))  # queue中没有元素了，就会阻塞;指定阻塞的时间为5秒，会抛出异常，队列为空
# True默认指定等到拿到数据为止，还可以指定等待的时间，指定时间拿不到数据，抛出异常；False为不阻塞
# print(q.get_nowait())  # 仍然抛出队列为空的异常


def handle(p: queue.Queue):  # 此处的p为局部参数
    time.sleep(5)
    p.put('xyz')


# threading模块————线程
t = threading.Thread(target=handle, args=(q, ))  # 创建线程对象；args为元组；q为全局变量
t.start()  # 启动线程
print(q.get())
print('+++++end+++++++')
