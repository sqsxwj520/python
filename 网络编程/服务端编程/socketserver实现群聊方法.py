# tcp server 端开发

import socketserver
import threading
import logging
from datetime import datetime


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
        super().handle()
        while not self.event.is_set():

            data = self.request.recv(1024)
            print(data.decode(encoding='cp936'))

            if data.strip() == b'quit' or data.strip() == b'':
                self.request.close()
                break

            msg = "{:%Y/%m/%d %H:%M:%S} [{}:{}] - {}".format(datetime.now(),
                                                             *self.client_address, data.decode(encoding='cp936'))

            with self.lock:
                for v in self.clients.values():
                    v.send(msg.encode(encoding='cp936'))

    def finish(self):
        super().finish()
        with self.lock:
            self.clients.pop(self.client_address)
        self.event.set()


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), ChatHandler)
server.daemon_threads = True
threading.Thread(target=server.serve_forever, name='server_forever').start()

while True:
    cmd = input('>>>').strip()
    if cmd == 'quit':
        server.server_close()
        print('bye')
        break
    print(threading.enumerate())
