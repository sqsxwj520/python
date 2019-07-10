# IO多路复用，实现TCP版本的群聊
import socket
import threading
import selectors
import logging


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:

    def __init__(self, ip='127.0.0.1', port=9992):
        self.sock = socket.socket()
        self.address = ip, port
        self.event = threading.Event()

        self.selector = selectors.DefaultSelector()

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen()
        self.sock.setblocking(False)

        key = self.selector.register(self.sock, selectors.EVENT_READ, self.accept)  # 只有一个
        logging.info(key)  # 只有一个
        # self.accept_key = key
        # self.accept_fd = key.fd

        threading.Thread(target=self.select, name='select', daemon=True).start()

    def select(self):

        while not self.event.is_set():
            events = self.selector.select()  # 阻塞
            for key, _ in events:
                key.data(key.fileobj)  # select线程

    def accept(self, sock: socket.socket):  # 在select线程中运行的
        new_sock, r_address = sock.accept()
        new_sock.setblocking(False)
        print('~' * 30)

        key = self.selector.register(new_sock, selectors.EVENT_READ, self.rec)  # 有n个
        logging.info(key)

    def rec(self, conn: socket.socket):  # 在select线程中运行的
        data = conn.recv(1024)
        logging.info(data.decode(encoding='cp936'))

        if data.strip() == b'quit' or data.strip() == b'':
            self.selector.unregister(conn)  # 关闭之前，注销,理解为之前的从字典中移除socket对象
            conn.close()
            return

        for key in self.selector.get_map().values():
            s = key.fileobj
            # if key.fileobj is self.sock:  # 方法一
            #     continue
            # if key == self.accept_key:  # 方法二
            #     continue
            # if key.fd == self.accept_fd:  # 方法三
            #     continue
            # msg = 'Your msg = {} form {}'.format(data.decode(encoding='cp936'), conn.getpeername())
            # s.send(msg.encode(encoding='cp936'))
            # print(key.data)
            # print(self.rec)
            # print(1, key.data is self.rec)  # False
            # print(2, key.data == self.rec)  # True
            if key.data == self.rec:  # 方法四
                msg = 'Your msg = {} form {}'.format(data.decode(encoding='cp936'), conn.getpeername())
                s.send(msg.encode(encoding='cp936'))

    def stop(self):  # 在主线程中运行的
        self.event.set()
        fs = set()
        for k in self.selector.get_map().values():
            fs.add(k.fileobj)
        for f in fs:
            self.selector.unregister(f)  # 相当于以前的释放资源
            f.close()
        self.selector.close()


if __name__ == "__main__":
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input(">>>").strip()
        if cmd == 'quit':
            cs.stop()
            break
        logging.info(threading.enumerate())
        logging.info(list(cs.selector.get_map().keys()))
        # for fd, ke in cs.selector.get_map().items():
        #     logging.info(fd)
        #     print(ke)
        #     print()
