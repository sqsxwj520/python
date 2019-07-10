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
    logging.info(ret)
    # if i % 2 == 0:
    #     1 / 0
    return ret  # 这个返回值是拿不到的


if __name__ == "__main__":
    start = datetime.datetime.now()

    pool = multiprocessing.Pool(2)

    ps = []
    for j in range(4):
        r = pool.apply(calc, (j, ))
        logging.info(r)
        # p = multiprocessing.Process(target=calc, args=(j,), name="calc-{}".format(j))
        # ps.append(p)
        # p.start()
    # pool.terminate()
    pool.close()
    pool.join()  # 用join方法，状态必须是close或terminate

    # for p in ps:
    #     p.join()
    #     logging.info("{} {}".format(p.name, p.exitcode))

    delta = (datetime.datetime.now() - start).total_seconds()
    print(threading.enumerate())  # 只有一个线程，就是主线程
    print("===end===", delta)
