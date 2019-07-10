import socket


client = socket.socket()
ip_address = ('127.0.0.1', 9999)
client.connect(ip_address)  # 直接连接服务器

client.send(b'abc\n')
data = client.recv(1024)  # 阻塞等待

client.close()
