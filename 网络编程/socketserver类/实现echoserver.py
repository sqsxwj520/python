import socketserver
import threading


class MyHandler(socketserver.BaseRequestHandler):

    def setup(self):  # 注意每一次连接都会创建一个MyHandler实例
        super().setup()
        self.event = threading.Event()  # 不用担心会被覆盖

    def handle(self):
        super().handle()  # 可以不调用，因为父类什么都没做

        while True:
            data = self.request.recv(1024)
            print(data)

            msg = "{}".format(data.decode())
            self.request.send(msg.encode())

    def finish(self):
        super().finish()
        self.event.set()


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandler)

# server.serve_forever()  # 默认阻塞，可以放在线程中
threading.Thread(target=server.serve_forever, name='server_forever').start()

while True:
    cmd = input(">>>").strip()
    if cmd == 'quit':
        server.server_close()
        print('bye')
        break
    print(threading.enumerate())
