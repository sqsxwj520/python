import socket
import threading
import datetime
import logging


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatClient:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.client = socket.socket()
        self.address = ip, port
        self.event = threading.Event()

    def start(self):
        self.client.connect(self.address)
        self.send("I'm ready.")
        threading.Thread(target=self.rec, name='rec').start()

    def rec(self):
        while not self.event.is_set():
            try:
                data = self.client.recv(1024)  # 此句可能会出现异常，如网络中断
            except Exception as e:
                logging.error(e)
                break

            msg = "{:%Y/%m/%d %H:%M:%S} [{}:{}] {}".format(datetime.datetime.now(), *self.address, data)
            logging.info(msg)

    def send(self, msg: str):
        data = "{}\n".format(msg.strip()).encode()
        self.client.send(data)

    def stop(self):
        self.client.close()
        self.event.wait(3)
        self.event.set()
        logging.info('Client stops')


cc = ChatClient()
cc.start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        cc.stop()
        break
    cc.send(cmd)
