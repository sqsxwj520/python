import socket
import threading
import logging


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatClientUdp:

    def __init__(self, ip='127.0.0.1', port=9999, interval=5):
        self.address = ip, port
        self.client = socket.socket(type=socket.SOCK_DGRAM)
        self.event = threading.Event()
        self.interval = interval

    def start(self):
        self.client.connect(self.address)
        self.send("{} hello".format(self.client.getsockname()))
        threading.Thread(target=self.heart_beat, name='heart_beat', daemon=True).start()
        threading.Thread(target=self.rec, name='rec').start()

    def rec(self):
        while not self.event.is_set():
            data = self.client.recvfrom(1024)
            logging.info(data)

    def heart_beat(self):  # 增加心跳机制,注意另开了一个线程，发送心跳只是告诉服务端线程仍然活着
        while not self.event.wait(self.interval):
            self.send('^hb^')

    def send(self, msg: str):
        self.client.sendto(msg.encode(), self.address)

    def stop(self):
        self.event.set()
        self.send('quit')
        self.client.close()


ccu = ChatClientUdp()
ccu.start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        ccu.stop()
        break
    ccu.send(cmd)
    logging.info(threading.enumerate())
