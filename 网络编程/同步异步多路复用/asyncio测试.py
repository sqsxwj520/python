import threading
import time
import multiprocessing


def a():
    for i in range(3):
        time.sleep(0.0001)
        print('a.x', i)


def b():
    for i in 'abc':
        time.sleep(0.0001)
        print('b.x', i)


t1 = threading.Thread(target=a, name='a')
t2 = threading.Thread(target=b, name='b')
t1.start()  # 交替
t2.start()


if __name__ == "__main__":

    t3 = multiprocessing.Process(target=a, name='a')
    t4 = multiprocessing.Process(target=b, name='b')
    t3.start()
    t4.start()
