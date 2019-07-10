import socket
import logging
import threading


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatClient:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.address = ip, port
        self.client = socket.socket()
        self.event = threading.Event()

    def start(self):
        self.client.connect(self.address)
        self.send('hello python')
        threading.Thread(target=self.rec, name='rec').start()

    def rec(self):
        while not self.event.is_set():
            try:
                data = self.client.recv(1024)
                print(data)
            except Exception as e:
                logging.error(e)
                break

    def send(self, msg: str):
        self.client.send(msg.encode())

    def stop(self):
        self.event.set()
        self.client.close()


cc = ChatClient()
cc.start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        cc.stop()
        break
    logging.info(threading.enumerate())
