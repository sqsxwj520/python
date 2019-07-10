import socket
# import time


address = '127.0.0.1', 10001
client = socket.socket(type=socket.SOCK_DGRAM)  # 数据报协议
client.connect(address)  # 会解决本地address和远端地址address
print(1, client)
print(1.5, client)
ms = b'111222333444555'
# client.sendto(ms + b'~~~~~~~', ('127.0.0.1', 10000))
#  会帮你抢一个本地地址和端口（端口是临时的），没有此句，recvfrom会报错
# 可以自己玩，因为它有本地address, 它不会记录远端地址address
client.send(ms)  # 必须和connect配合使用，什么都不解决

print(2, client)
data, info = client.recvfrom(1024)  # 它需要本地address
print(data, info)

# client.connect(address)  # 加了这一句，send就可以用了
# while True:
#     cmd = input(">>>").strip()
#     ms = cmd.encode()
#     # client.sendto(ms, address)
#     client.send(ms)  # 此句必须和connect配合使用
#     client.sendto(ms + b'~~~~~~~', ('127.0.0.1', 10000))
#     client.sendto(ms + b'+++++++', ('127.0.0.1', 10001))
#     data, info = client.recvfrom(1024)  # 比recv安全，可以知道是谁发给你的
#     print(data)
#     msg = "{} from {}".format(data.decode(), *info).encode()
#
#     print('~' * 30)

client.close()
