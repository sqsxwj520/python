from threading import Thread
import threading
import time


class MyThread(Thread):
    def start(self) -> None:  # 返回值是None
        print("start~~~~~")
        super().start()  # 跟启动操作系统线程有关

    def run(self):
        print("run~~~~~~~~")  # 运行函数有关
        super().run()


def worker():
    for i in range(5):
        time.sleep(0.5)
        print(threading.current_thread().name, "I'm working")


t1 = MyThread(target=worker, name="worker1")
t2 = MyThread(target=worker, name="worker2")
# t1.start()
# t2.start()

t1.run()  # 会先执行这句，执行完了，再执行下一条于语句，注意此时没有多线程了
t2.run()
print("~" * 30)
