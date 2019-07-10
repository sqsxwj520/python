import socketserver
import threading


class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        super().handle()  # 可以不调用，父类的handle什么都没做
        print(self.server)  # 服务
        print(self.request)  # 服务端负责客户端请求的socket对象
        print(self.client_address)  # 客户端地址
        print(self.server)
        print(self.__dict__)
        print(self.server.__dict__)  # 能看到负责accept的socket
        print('*' * 30)

        for i in range(3):
            data = self.request.recv(1024)
            print(data)
            msg = 'server recv msg= {}'.format(data.decode()).encode()
            self.request.send(msg)

        print(threading.enumerate())
        print(threading.current_thread())
        print()


# server = socketserver.TCPServer(('127.0.0.1', 9999), MyHandler)
server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandler)
print(server)

server.serve_forever()  # 永久的提供服务，默认阻塞行为

server.server_close()
