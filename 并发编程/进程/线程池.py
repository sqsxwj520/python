from concurrent.futures import ThreadPoolExecutor
import logging
import time
import threading


FORMAT = "%(asctime)s %(threadName)s %(thread)8d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(n):
    logging.info('enter thread~~~~~~~{}'.format(n))
    time.sleep(5)
    logging.info('finished ----------{}'.format(n))
    return 1000 + n


executor = ThreadPoolExecutor(max_workers=3)
fs = []
with executor:

    for i in range(3):
        future = executor.submit(worker, i)
        logging.info(future)
        fs.append(future)
    print('~' * 30)

    # time.sleep(5)
    # print('~' * 30)
    # print(threading.enumerate())
    # print('~' * 30)

    for j in range(3, 6):
        future = executor.submit(worker, j)
        logging.info(future)

    logging.info('=' * 30)

    while True:
        flag = True
        for f in fs:
            logging.info(f.done())
            flag = flag and f.done()
        # if threading.active_count() == 1:
        #     logging.info(threading.enumerate())
        #     logging.info(future)
        #     break
        time.sleep(1)
        print()

        if flag:
            executor.shutdown()
            logging.info(threading.enumerate())  # 进程的时候此句没什么用了
            break

print('~' * 30)
for f in fs:
    print(f.result())
