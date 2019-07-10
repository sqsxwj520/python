import multiprocessing
import logging
import threading
import datetime


FORMAT = '%(asctime)s %(process)8s %(processName)s %(threadName)s %(thread)8d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i):
    total = 0
    for _ in range(1000000):
        total += 1
    ret = i, total
    logging.info(ret)
    # if i % 2 == 0:
    #     1 / 0
    return ret  # 这个返回值是拿不到的


def sub(p, tr, x):
    r = p.apply(tr, (x,))  # 同步阻塞的方法，函数执行完才会返回；一个进程结束才会开启另一个进程（串行）
    logging.info(r)


if __name__ == "__main__":
    start = datetime.datetime.now()

    pool = multiprocessing.Pool(2)

    ps = []
    for j in range(4):
        t = threading.Thread(target=sub, args=(pool, calc, j), name="{}".format(j))
        t.start()
        print('-' * 30)
        # r = pool.apply(calc, (j, ))  # 同步阻塞的方法，函数执行完才会返回；一个进程结束才会开启另一个进程（串行）
        # logging.info(r)  # 可以拿到函数的返回值了
        # print("**********************")
    print("+++++++++++++++++++++++")
    # pool.terminate()
    pool.close()
    pool.join()  # 用join方法，状态必须是close或terminate

    delta = (datetime.datetime.now() - start).total_seconds()
    print(threading.enumerate())  # 只有一个线程，就是主线程
    print("===end===", delta)
