import socketserver
import threading


class MyHandler(socketserver.BaseRequestHandler):

    def setup(self):
        super().setup()
        self.event = threading.Event()

    def handle(self):
        super().handle()

        print('*' * 30)

        while True:
            data = self.request.recv(1024)
            print(data)
            msg = 'server rec msg= {}'.format(data.decode()).encode()
            self.request.send(msg)

    def finish(self):
        super().finish()
        self.event.set()


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandler)
print(server)

threading.Thread(target=server.serve_forever, name='server_forever').start()

while True:
    cmd = input('>>>').strip()
    if cmd == 'quit':
        server.server_close()
        print('bye')
        break
    print(threading.enumerate())
