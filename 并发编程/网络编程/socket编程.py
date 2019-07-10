import socket
import datetime
import threading
import logging


FORMAT = "[%(name)s] %(thread)8d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket()
        self.address = ip, port

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen()
        threading.Thread(target=self.accept, name='accept').start()
        # new_sock, client_info = self.sock.accept()
        # threading.Thread(target=self.rec, name='rec', args=(new_sock, client_info)).start()

    def accept(self):
        while True:
            new_sock, client_info = self.sock.accept()
            threading.Thread(target=self.rec, name='rec', args=(new_sock, client_info)).start()

    def rec(self, sock: socket.socket, client):
        while True:
            data = sock.recv(1024)  # 阻塞等待信息
            print(data)  # bytes
            msg = '{:%Y/%m/%d %H:%M:%S} [{}:{}] - {}'.format(datetime.datetime.now(), *client, data.decode())

            sock.send(msg.encode())

    def stop(self):
        self.sock.close()  # 关闭sock，不能再创建新的连接了


cs = ChatServer()
cs.start()
# logging.info(threading.enumerate())
# cs.stop()
while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        cs.stop()
        break
logging.info(threading.enumerate())
