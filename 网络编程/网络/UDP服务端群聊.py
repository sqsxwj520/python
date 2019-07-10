import socket
import datetime
import logging
import threading


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServerUdp:
    # UDP群聊用的都是同一个socket，所以用字典浪费了，所有的value值都是一样的，列表可以，但是移除的话，效率低，所以考虑用集合
    # 但是添加了过期删除了client的话，集合就不合适了，此时还是要用字典
    def __init__(self, ip='127.0.0.1', port=9999, interval=10):  # 服务端的时间间隔一般是客户端的时间间隔的2到3倍
        self.sock = socket.socket(type=socket.SOCK_DGRAM)  # 数据报文协议
        self.address = ip, port
        self.event = threading.Event()
        # self.clients = set()
        self.clients = {}
        self.interval = interval

    def start(self):
        self.sock.bind(self.address)

        threading.Thread(target=self.rec, name='rec').start()

    def rec(self):
        while not self.event.is_set():
            data, client_info = self.sock.recvfrom(1024)
            current = datetime.datetime.now().timestamp()  # float
            # self.clients.add(client_info)

            if data.strip() == b'^hb^':  # b'^hb^'为自己设计的
                self.clients[client_info] = current
                logging.info('{} hb^^^^^'.format(client_info))
                continue

            if data.strip() == b'quit':
                # self.clients.remove(client_info)  # 注意remove相当于是按照key查找的，因为集合的值可以看做字典的key，所以比列表高效

                self.clients.pop(client_info)  # 客户端主动断开连接，就把该客户的ip从字典中删除
                logging.info("{} leaving".format(client_info))
                continue  # 不能用break，因为总共只有一个线程，break了，while循环结束了

            self.clients[client_info] = current

            # 在该位子遍历字典，删除过期的clients，比较耗时，因为如果一个都没有删除，每次都要遍历字典，会很耗时，可以考虑在发送信息时，
            # 遍历字典判断是否超时

            logging.info(data)
            msg = "{} [{}:{}] {}".format(datetime.datetime.now(), *client_info, data.decode())

            keys = set()
            for c, stamp in self.clients.items():  # 有线程安全问题，解决方法是加锁
                if current - stamp < 0 or current - stamp > self.interval:  # 小于0应该是时间出问题了
                    keys.add(c)  # 不能直接self.clients.pop(c),因为字典在遍历的过程中，其长度不能改变
                else:
                    self.sock.sendto(msg.encode(), c)
            for c in keys:
                self.clients.pop(c)

    def stop(self):
        self.event.set()
        self.clients.clear()
        self.sock.close()


csu = ChatServerUdp()
csu.start()

while True:
    cmd = input('>>>').strip()
    if cmd == 'quit':
        csu.stop()
        break
    logging.info(threading.enumerate())
    logging.info(csu.clients)
