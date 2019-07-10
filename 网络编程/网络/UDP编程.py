import socket
import threading

event = threading.Event()
address = '0.0.0.0', 9999
server = socket.socket(type=socket.SOCK_DGRAM)  # 数据报协议
server.bind(address)  # 只能绑定一次

while not event.is_set():
    data, client_info = server.recvfrom(1024)  # 比recv安全，可以知道是谁发给你的
    print(data)
    # print(server.getpeername())  # 会报错OSError
    msg = "{} from {}-{}".format(data.decode(), *client_info).encode()
    # server.send(msg)  # 会报错，不知道发送给谁
    server.sendto(msg, client_info)

    print('~' * 30)

event.set()
server.close()
