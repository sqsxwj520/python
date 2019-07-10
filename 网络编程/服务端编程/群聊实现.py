# tcp server 端开发

import socket
import threading
import logging
from datetime import datetime


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket()
        self.address = ip, port
        self.event = threading.Event()
        self.lock = threading.Lock()
        self.clients = {}

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen()

        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            try:
                new_sock, client_info = self.sock.accept()  # 阻塞等待连接
            except Exception as e:
                logging.error(e)

            with self.lock:
                self.clients[client_info] = new_sock
                threading.Thread(target=self.rec, name='rec', args=(new_sock, client_info)).start()

    def rec(self, sock, client):
        while not self.event.is_set():
            try:
                data = sock.recv(1024)  # 阻塞等待接收信息，接收信息也可能出现异常
            except Exception as e:
                logging.error(e)
                data = b''
            print(data.decode(encoding='cp936'))

            if data.strip() == b'quit' or data.strip() == b'':  # 客户端主动断开连接
                with self.lock:
                    self.clients.pop(client)  # 将断开连接的客户ip和端口从字典中移除，因为下文还要遍历字典
                sock.close()  # 此句比较耗时，可以放在锁的外面
                break

            msg = "{:%Y/%m/%d %H:%M:%S} [{}:{}] - {}".format(datetime.now(), *client, data.decode(encoding='cp936'))

            exc = []
            exs = []
            with self.lock:
                for c, s in self.clients.items():  # 遍历的是时候不允许别人pop和add，所以加锁
                    try:
                        s.send(msg.encode(encoding='cp936'))  # 给所有的new_sock发送的信息。注意此句可能会出现异常，如网络断了
                    except Exception as e:
                        logging.error(e)
                        exc.append(c)
                        exs.append(s)
                for c in exc:
                    self.clients.pop(c)
            for s in exs:  # 此句比较耗时，所以放在锁外面
                s.close()

    def stop(self):
        self.event.set()
        with self.lock:
            values = list(self.clients.values())
            self.clients.clear()  # 这是一个好习惯
        for s in values:
            s.close()
        self.sock.close()


cs = ChatServer()
cs.start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        cs.stop()
        break
    logging.info(threading.enumerate())
    logging.info(cs.clients)
