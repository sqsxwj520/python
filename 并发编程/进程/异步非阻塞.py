import multiprocessing
import logging
import threading
import datetime


FORMAT = "%(asctime)s %(process)8s %(processName)s %(threadName)s %(thread)8d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i):
    total = 0
    for _ in range(1000000):
        total += 1
    ret = i, total
    logging.info("{}".format(ret))
    # if i % 2 == 0:
    #     1 / 0
    return ret  # 这个返回值是拿不到的


if __name__ == "__main__":
    start = datetime.datetime.now()

    pool = multiprocessing.Pool(4)

    ps = []
    for j in range(4):
        r = pool.apply_async(calc, (j, ), callback=lambda x: logging.info("{} in main~~~".format(x)))  # 异步 非阻塞
        # callback为结果回调函数，在主进程中完成的
        logging.info(r)  # 可以拿到函数的返回值了
        print("***********************")
    print("+++++++++++++++++++++++")
    # pool.terminate()  # 强行终止，一般不用
    pool.close()
    print("========================")
    pool.join()  # 用join方法，状态必须是close或terminate
    print("~~~~~~~~~~~~~~~~~~~~~~~~")

    delta = (datetime.datetime.now() - start).total_seconds()
    print(threading.enumerate())  # 只有一个线程，就是主线程
    print("===end===", delta)
