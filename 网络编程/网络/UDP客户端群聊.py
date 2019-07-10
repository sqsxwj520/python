import socket
import logging
import threading


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatClientUdp:
    def __init__(self, ip='127.0.0.1', port=9999, interval=5):
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.r_address = ip, port
        self.event = threading.Event()
        self.interval = interval

    def start(self):
        self.sock.connect(self.r_address)
        self.send('{} hello'.format(self.sock.getsockname()))
        threading.Thread(target=self.heart_beat, name='heartbeat', daemon=True).start()
        threading.Thread(target=self.rec, name='rec').start()

    def heart_beat(self):
        while not self.event.wait(self.interval):
            # self.sock.send(b'^hb^')  # 发送心跳包，记录最后一次发送的时间，此句比较浪费时间，换成下面的语句
            self.send('^hb^')

    def rec(self):
        while not self.event.is_set():
            data = self.sock.recvfrom(1024)
            logging.info(data)

    def send(self, msg: str):
        self.sock.sendto(msg.encode(), self.r_address)

    def stop(self):
        self.event.set()
        self.send('quit')
        self.sock.close()


ccu = ChatClientUdp()
ccu.start()

while True:
    line = input('>>>').strip()
    if line == 'quit':
        ccu.stop()
        break
    ccu.send(line)
    logging.info(threading.enumerate())
