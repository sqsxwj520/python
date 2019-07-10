from threading import Thread, Lock
import threading
import time


class Counter:
    def __init__(self):
        self._val = 0
        self._lock = Lock()

    @property
    def value(self):
        with self._lock:  # 此位置可以不加锁，但是加锁是一个好习惯
            return self._val

    def inc(self):
        with self._lock:  # 上下文管理
            self._val += 1

    def dec(self):
        with self._lock:
            self._val -= 1


def run(r: Counter, count=100):
    for _ in range(count):
        for j in range(-50, 50):
            if j < 0:
                r.dec()
            else:
                r.inc()


thread_list = []
c = Counter()
c1 = 10  # 线程数
c2 = 10
for i in range(c1):
    t = Thread(target=run, args=(c, c2))
    t.start()  # 多线程，线程之间相互干扰，所以考虑添加锁
    thread_list.append(t)

for x in thread_list:
    x.join()  # 注意分析，为什么可以？考虑速度最慢的线程和速度最快的线程

print(c.value, "~~~~~~~~~~~")  # 注意这是主线程的语句，必须等其他工作线程都结束了，再执行该条语句


lock = threading.Lock()


def worker(l: threading.Lock):
    print("enter ~~~~~~~")
    while True:
        time.sleep(1)
        f = l.acquire(False)  # 非阻塞的锁
        if f:
            print("True")  # 此句能输出的话，说明捕获了锁
            break
    print("exit")


for y in range(3):
    t = threading.Thread(target=worker, name="worker-{}".format(y), args=(lock,))
    t.start()
"""\
enter ~~~~~~~
enter ~~~~~~~
enter ~~~~~~~
True
exit
"""
