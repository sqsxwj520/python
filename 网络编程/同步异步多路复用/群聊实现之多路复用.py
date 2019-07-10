import selectors
import threading
import socket
import logging


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:

    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket()
        self.address = ip, port
        self.event = threading.Event()

        self.selector = selectors.DefaultSelector()

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen()

        self.sock.setblocking(False)

        key = self.selector.register(self.sock, selectors.EVENT_READ, self.accept)  # 只有一个
        logging.info(key)
        self.accept_key = key
        self.accept_fd = key.fd

        threading.Thread(target=self.select, name='select', daemon=True).start()

    def select(self):
        while not self.event.is_set():
            events = self.selector.select()
            for k, mask in events:  # k.data为self.accept,self.rec
                k.data(k.fileobj, mask)   # 回调函数

    def accept(self, sock: socket.socket, mask):  # 在select线程中运行
        new_sock, address = sock.accept()
        new_sock.setblocking(False)
        print(mask, '++++++++++')
        logging.info('~~~~~~~~~~~~')

        key = self.selector.register(new_sock, selectors.EVENT_READ, self.rec)  # 有很多个
        logging.info(key)

    def rec(self, client: socket.socket, mask):  # 在select线程中运行
        print(mask, '------------')
        data = client.recv(1024)
        logging.info(data.decode(encoding='cp936'))
        if data.strip() == b'quit' or data.strip() == b'':  # 客户端主动断开
            self.selector.unregister(client)
            client.close()
            return  # 不能是break

        msg = " Your msg = {} from {} ".format(data.decode(encoding='cp936'), client.getpeername())

        for v in self.selector.get_map().values():
            s = v.fileobj
            # if s is self.sock:  # 方法一，注意不给服务端的new_sock发信息，而是给client发送信息
            #     continue
            # if v is self.accept_key:  # 方法二
            #     continue
            if v.fd is self.accept_fd:  # 方法三
                continue
            s.send(msg.encode(encoding='cp936'))

            # if v.data == self.rec:  # 方法四，注意此处的等号不能换成is，否则就得不到像要的结果
            #     s.send(msg.encode(encoding='cp936'))

    def stop(self):  # 在主线程中运行，可能存在线程安全问题，主线程在遍历，工作线程即有遍历又有增删
        self.event.set()

        fs = set()
        for v in self.selector.get_map().values():
            fs.add(v.fileobj)
        for f in fs:
            self.selector.unregister(f)
            f.close()

        self.selector.close()


cs = ChatServer()
cs.start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        cs.stop()
        break

    logging.info(threading.enumerate())
    logging.info(cs.selector.get_map().items())
    for kd, va in cs.selector.get_map().items():
        print(kd)
        print(va)
        print()
