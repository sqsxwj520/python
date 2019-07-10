import datetime
import threading
import socket
import logging


FORMAT = "%(asctime) %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


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
            with self.lock:
                self.clients[client_info] = new_sock  # 增加了item，所以必须加锁，多线程处理同一个资源
                threading.Thread(target=self.rec, name='rec', args=(new_sock, client_info)).start()

    def rec(self, sock: socket.socket, client):
        while not self.event.is_set():
            try:
                data = sock.recv(1024)
            except Exception as e:
                logging.error(e)
                data = b''
            print(data)

            if data.strip() == b'quit' or data.strip() == b'':
                with self.lock:
                    self.clients.pop(client)
                sock.close()
                break

            msg = '{:%Y/%m/%d %H:%M:%S} [{}: {}] {}'.format(datetime.datetime.now(), *client, data.decode())

            exp = []
            exs = []
            with self.lock:
                for c, s in self.clients.items():
                    try:
                        s.send(msg.encode())  # 有可能出错
                    except:
                        exp.append(c)
                        exs.append(s)
                for c in exp:
                    self.clients.pop(c)
            for s in exs:
                s.close()

    def stop(self):
        self.event.set()
        # keys = []
        with self.lock:
            values = list(self.clients.values())
            self.clients.clear()  # 写这一句是一个好习惯
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
