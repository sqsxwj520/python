import threading
import time

# x = 0
global_data = threading.local()


def worker():
    global_data.x = 0
    # global x  # 输出的x的值是不确定的
    # x = 0  # 注意x为局部变量，在每个线程中都是独立的，在各自的线程中压栈
    for i in range(100):
        time.sleep(0.0001)
        global_data.x += 1
    print(threading.current_thread().name, global_data.x)


for j in range(10):
    threading.Thread(target=worker, name="worker-{}".format(j + 1)).start()
# 在多线程中，局部变量绝对是安全的，不会有任何安全问题。如果是全局变量，就要小心了。
