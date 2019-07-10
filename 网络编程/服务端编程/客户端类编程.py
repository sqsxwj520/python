import socket
import logging
import threading


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatClient:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.address = ip, port
        self.sock = socket.socket()
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.address)
        self.send('hello server')
        threading.Thread(target=self.rec, name='rec').start()
        threading.Thread(target=self._inner, name='inner').start()

    def rec(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024)  # 阻塞
                print(data)
            except Exception as e:
                logging.error(e)

    def send(self, msg: str):
        self.sock.send(msg.encode())

    @staticmethod
    def _inner():  # 下面的语句不一定非得在主线程中，交互可以在任意线程
        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit':
                cc.stop()
                break

            cc.send(cmd)  # 不写成cc.sock.send()，就是不暴露sock，更方便
            logging.info(threading.enumerate())

    def stop(self):
        self.event.set()
        self.send('quit')
        self.sock.close()


cc = ChatClient()
cc.start()
