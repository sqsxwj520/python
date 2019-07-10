import datetime
import threading
import socket
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket()
        self.address = ip, port
        self.event = threading.Event()
        self.clients = {}
        self.lock = threading.Lock()

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen()
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            new_sock, client_info = self.sock.accept()

            new_file = new_sock.makefile('rw')
            with self.lock:
                self.clients[client_info] = new_file, new_sock  # 增加了item，所以必须加锁，多线程处理同一个资源
                threading.Thread(target=self.rec, name='rec', args=(new_file, client_info)).start()

    def rec(self, f, client):
        while not self.event.is_set():
            line = f.readline()  # 阻塞等一行来，输入数据的时候要加换行符
            print(line)
            if line.strip() == 'quit' or line.strip() == '':  # line为字符串。不能再写成b''和b'quit'了
                with self.lock:
                    _, s = self.clients.pop(client)
                f.close()
                s.close()
                break

            msg = '{:%Y/%m/%d %H:%M:%S} [{}: {}] {}'.format(datetime.datetime.now(), *client, line)
            # 此处的line不用解码了，因为readline读取的是字符串

            with self.lock:
                for ff, _ in self.clients.values():  # 注意ff不能与上面的f重复
                    ff.write(msg)
                    ff.flush()

    # def rec(self, f, client):
    #     while not self.event.is_set():
    #         try:
    #             line = f.readline()
    #         except Exception as e:
    #             logging.error(e)
    #             line = 'quit'
    #         msg = line.strip()
    #         if msg == 'quit' or msg == '':
    #             with self.lock:
    #                 _, sock = self.clients.pop(client)
    #                 f.close()
    #                 sock.close()
    #                 logging.info('{} quits.'.format(client))
    #                 break
    #         msg = '{:%Y/%m/%d %H:%M:%S} [{}: {}] {}'.format(datetime.datetime.now(), *client, line)
    #         logging.info(msg)
    #         with self.lock:
    #             for ff, _ in self.clients.values():
    #                 ff.write()
    #                 ff.flush()

    def stop(self):
        self.event.set()
        # keys = []
        with self.lock:
            for f, s in self.clients.values():
                f.close()
                s.close()

        self.sock.close()


def main():
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input(">>>").strip()
        if cmd == 'quit':
            cs.stop()
            threading.Event().wait(3)
            break
        logging.info(threading.enumerate())
        logging.info(cs.clients)


if __name__ == '__main__':
    main()
