import socket
import threading
import logging
import datetime


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='192.168.31.1', port=9999):
        self.sock = socket.socket()
        self.address = ip, port
        self.clients = {}
        self.lock = threading.Lock()
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen()
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            try:
                new_sock, client_info = self.sock.accept()  # 阻塞，等待连接
            except Exception as e:
                logging.error(e)

            with self.lock:
                self.clients[client_info] = new_sock
                threading.Thread(target=self.rec, name='rec', args=(new_sock, client_info)).start()

    def rec(self, sock, client):
        while not self.event.is_set():
            try:
                data = sock.recv(1024)  # 阻塞等待接收数据，此句也可能出现异常，如网线断了
            except Exception as e:
                logging.error(e)
                data = b''
            print(data.decode(encoding='cp936'))

            if data.strip() == b'quit' or data.strip() == b'':  # 客户端主动断开
                with self.lock:
                    self.clients.pop(client)  # 从字典中删除主动断开连接的客户端ip和端口，因为下文还要遍历字典
                    sock.close()
                    break

            msg = "{:%Y/%m/%d %H:%M:%S} [{}:{}] {}".format(datetime.datetime.now(),
                                                           *client, data.decode(encoding='cp936'))
            exc = []
            exs = []
            with self.lock:
                for c, s in self.clients.items():
                    try:
                        s.send(msg.encode(encoding='cp936'))  # 此句可能出现异常，如网络中断

                    except Exception as e:
                        logging.error(e)
                        exs.append(s)
                        exc.append(c)
                for c in exc:
                    self.clients.pop(c)  # 移除出现异常的ip和端口信息
            for s in exs:  # 此句比较耗时，所以放在锁的外部
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
