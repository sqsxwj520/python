# TCP server 端开发
import socket
# import time


server = socket.socket()  # TCP 连接 IPv4
ip = '127.0.0.1'  # 本机回环地址，永远指向本机
port = 9999  # 建议使用1000以上; TCP 65536种状态
server.bind((ip, port))  # address,此方法只能绑定一次
server.listen()  # 真正的显示出端口，监听不是阻塞函数
# time.sleep(100)
print(server)
# print(server.accept())  # 默认阻塞，不懂千万不要修改

new_socket, client_info = server.accept()
print(new_socket)
print('new_socket', client_info)
while True:
    # new_socket.send(b'server ack')
    data = new_socket.recv(1024)  # 缺省情况下是阻塞的

    print(data)
    new_socket.send('server ack. data={}'.format(data.decode()))

new_socket.close()

# new2, client2 = server.accept()  # 新的连接，之前的连接已经关闭，并且两次连接可能在不同的进程
# print(new2)
# print('new2', client2)
# data = new2.recv(1024)
# print(data)
# new2.send('server new2 ack. data={}'.format(data.encode()))
# new2.close()

server.close()
