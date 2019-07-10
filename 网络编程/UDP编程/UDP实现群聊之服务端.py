import socket
import threading
import datetime
import logging


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServerUdp:

    def __init__(self, ip='127.0.0.1', port=9999, interval=10):
        self.address = ip, port
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.event = threading.Event()
        self.clients = {}
        self.interval = interval
        self.lock = threading.Lock()

    def start(self):
        self.sock.bind(self.address)
        threading.Thread(target=self.rec, name='rec').start()

    def rec(self):
        while not self.event.is_set():
            data, client_info = self.sock.recvfrom(1024)
            current = datetime.datetime.now().timestamp()

            if data.strip() == b'^hb^':  # 就是说线程还活着，重置线程时间，就能收到群聊信息
                # 加入心跳机制
                with self.lock:
                    self.clients[client_info] = current  # 重置当前client_info的时间
                    logging.info('{} hb^^^^^^^^^'.format(client_info))
                    continue

            if data.strip() == b'quit':
                with self.lock:
                    self.clients.pop(client_info)
                    logging.info("{} leaving".format(client_info))
                    continue  # 此处不能是break，break会结束while循环，当前线程也就结束了
            with self.lock:
                self.clients[client_info] = current

            logging.info(data)

            msg = "{:%Y/%m/%d %H:%M:%S} [{}:{}] -{}".format(datetime.datetime.now(), *client_info, data.decode())

            keys = set()  # 有去重效果，比列表要好一些
            with self.lock:
                for m, stamp in self.clients.items():  # 注意字典在遍历的过程中，其长度不能改变
                    if current - stamp > self.interval or current - stamp < 0:
                        keys.add(m)  # 注意不能直接pop
                    else:
                        self.sock.sendto(msg.encode(), m)

                for n in keys:
                    self.clients.pop(n)

    def stop(self):
        self.event.set()
        self.clients.clear()  # 这是一个好习惯
        self.sock.close()


csu = ChatServerUdp()
csu.start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        csu.stop()
        break
    logging.info(threading.enumerate())
