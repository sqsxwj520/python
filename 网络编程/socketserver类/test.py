import socketserver
import datetime
import threading
import logging

FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatHandler(socketserver.BaseRequestHandler):
    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.lock = threading.Lock()
        with self.lock:
            self.clients[self.client_address] = self.request

    def handle(self):
        while not self.event.is_set():
            data = self.request.recv(1024)

            if data.strip() == b'quit' or data.strip() == b'':
                self.request.close()
                break
            logging.info(data.decode(encoding='cp936'))

            msg = "{} [{}:{}] {}".format(datetime.datetime.now(), *self.client_address, data.decode(encoding='cp936'))

            exc = set()
            with self.lock:
                for c, v in self.clients.items():
                    try:
                        v.send(msg.encode(encoding='cp936'))
                    except Exception as e:
                        logging.error(e)
                        exc.add(c)
                for c in exc:
                    self.clients.pop(c)

    def finish(self):
        super().finish()
        self.event.set()
        with self.lock:
            self.clients.pop(self.client_address)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9998), ChatHandler)
server.daemon_threads = True
threading.Thread(target=server.serve_forever, name='serve_forever').start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        server.server_close()
        break
    logging.info(threading.enumerate())
