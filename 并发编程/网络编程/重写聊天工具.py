import threading
import socket
import logging
import datetime


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket()
        self.address = ip, port
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.clients = {}

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen()
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            try:
                new_sock, client_info = self.sock.accept()
            except Exception as e:
                logging.info(e)

            with self.lock:
                self.clients[client_info] = new_sock  # 增加字典的长度，必须加锁
                threading.Thread(target=self.rec, name='rec', args=(new_sock, client_info)).start()

    def rec(self, sock, client):
        while not self.event.is_set():
            try:
                data = sock.recv(1024)
            except Exception as e:
                logging.error(e)
                data = b''
            print(data)

            if data.strip() == b'quit' or data.strip() == b'':  # client主动断开的处理
                self.clients.pop(client)  # 此ip已经断开，就从字典中删除
                sock.close()
                break

            msg = "{:%Y/%m/%d %H:%M:%S} [{}:{}] {}".format(datetime.datetime.now(), *client, data.decode())
            # exp = []
            exs = []
            with self.lock:
                for c, s in self.clients.items():
                    try:
                        s.send(msg.encode())  # 有可能出错，如网络中断，所以可以捕获异常
                    except:
                        # exp.append(c)
                        exs.append(s)
                # for c in exp:
                #     self.clients.pop(c)  # 移除出现异常的ip和端口信息
            for s in exs:  # 此句比较耗时，所以放在锁的外面
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
        threading.Event().wait(3)
        break
    logging.info(threading.enumerate())
    logging.info(cs.clients)
