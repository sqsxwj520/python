import socketserver
import threading


class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        super().handle()
        print(self.request)
        print(self.__dict__)
        print(self.server.__dict__)
        # <socket.socket fd=204, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM,
        # proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 52659)>

        print(self.client_address)
        print(self.server)
        # <socketserver.TCPServer object at 0x0000000001EA0828>

        for _ in range(3):
            data = self.request.recv(1024)
            print(data.decode())

            msg = 'server rec msg={}'.format(data.decode())
            self.request.send(msg.encode())

        print(threading.enumerate())
        print(threading.current_thread())
        print()


# server = socketserver.TCPServer(('127.0.0.1', 9999), MyHandler)
server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandler)
# ThreadingTCPServer是异步的，可以同时处理多个连接
print(server)
# <socketserver.TCPServer object at 0x0000000001EA0828>

server.serve_forever()  # 默认阻塞
