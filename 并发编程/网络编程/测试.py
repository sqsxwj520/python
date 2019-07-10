import logging
import socket
import threading
import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(thread)d %(message)s")


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):  # 启动服务
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.clients = {}  # 客户端
        self.event = threading.Event()
        self.lock = threading.Lock()

    def start(self):  # 启动监听
        self.sock.bind(self.addr)  # 绑定
        self.sock.listen()  # 监听
        # accept会阻塞主线程，所以开一个新线程
        threading.Thread(target=self.accept).start()

    def accept(self):  # 多人连接
        while not self.event.is_set():
            sock, client = self.sock.accept()  # 阻塞
            # 准备接收数据，rec是阻塞的，开启新的线程
            f = sock.makefile('rw')  # 支持读写
            with self.lock:
                self.clients[client] = f, sock  # 添加到客户端字典
                threading.Thread(target=self.rec, args=(f, client), name='rec').start()

    def rec(self, f, client):  # 接收客户端数据
        while not self.event.is_set():
            try:
                data = f.readline()  # 阻塞到换行符
            except Exception as e:
                logging.error(e)  # 有任何异常，退出
                data = 'quit'
            msg = data.strip()
        # 客户端退出命令
            if msg == 'quit' or msg == '':
                with self.lock:
                    _, s = self.clients.pop(client)
                    f.close()
                    s.close()
                    logging.info('{} quits'.format(client))
                    break
            msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *client, data)
            logging.info(msg)
            for s in self.clients.values():
                s.write(msg)
                s.flush()

    def stop(self):  # 停止服务
        self.event.set()
        with self.lock:
            for s in self.clients.values():
                s.close()
        self.sock.close()


def main():
    cs = ChatServer()
    cs.start()
    while True:
        cmd = input('>>').strip()
        if cmd == 'quit':
            cs.stop()
            threading.Event().wait(3)
            break
    logging.info(threading.enumerate())  # 用来观察断开后线程的变化


if __name__ == '__main__':
    main()
