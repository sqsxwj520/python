from concurrent.futures import ProcessPoolExecutor  # , ThreadPoolExecutor
import logging
import time


FORMAT = "%(asctime)s %(threadName)s %(thread)8d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(n):
    logging.info('enter thread~~~~~~~{}'.format(n))
    time.sleep(5)
    logging.info('finished ----------{}'.format(n))
    return 1000 + n


if __name__ == "__main__":

    executor = ProcessPoolExecutor(max_workers=3)
    fs = []
    with executor:

        for i in range(6):
            future = executor.submit(worker, i + 2)
            logging.info(future)
            fs.append(future)

        while True:
            flag = True
            for f in fs:
                print(f.done())
                flag = flag and f.done()
                # if not flag:
                #     break
            time.sleep(1)
            print()

            if flag:
                break

    print('~' * 30)
    for f in fs:
        print(f.result())
