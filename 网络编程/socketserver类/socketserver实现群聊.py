import socketserver
import threading
import datetime
import logging


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatHandler(socketserver.BaseRequestHandler):
    clients = {}  # 类属性

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.lock = threading.Lock()
        with self.lock:
            self.clients[self.client_address] = self.request

    def handle(self):
        super().handle()  # 可以不调用，因为父类什么都没做
        while not self.event.is_set():
            try:
                data = self.request.recv(1024)  # 接收信息也可能出现异常
            except Exception as e:
                logging.error(e)
                data = b''
            logging.info(data)

            if data.strip() == b'quit' or data.strip() == b'':  # 客户端主动断开，移除self.client_address在finish方法中
                self.request.close()
                break

            msg = "{} [{}:{}] {}".format(datetime.datetime.now(), *self.client_address, data.decode())

            exc = set()
            with self.lock:
                for c, v in self.clients.items():
                    try:
                        v.send(msg.encode())  # 可能出现异常，发送失败，如突然断网了
                    except Exception as e:
                        logging.error(e)
                        exc.add(c)
                for c in exc:
                    self.clients.pop(c)

    def finish(self):
        super().finish()
        with self.lock:
            self.clients.pop(self.client_address)
        self.event.set()


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), ChatHandler)
server.daemon_threads = True
threading.Thread(target=server.serve_forever, name='serve_forever').start()

while True:
    cmd = input('>>>').strip()
    if cmd == 'quit':
        server.server_close()
        print('bye')
        break
    logging.info(threading.enumerate())
