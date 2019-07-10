import socket


s = socket.socket()
s.bind(('127.0.0.1', 9999))
s.listen()
s1, info = s.accept()
print(s1.getpeername())  # ('127.0.0.1', 55934)
print(s1.getsockname())  # ('127.0.0.1', 9999)

f = s1.makefile('rw')
data = f.read(10)  # 一次读取10个字节
print(data)
msg = 'server rec {}'.format(data)
f.write(msg)
f.flush()
print(f, s1, sep='\n')

f.close()
s1.close()
s.close()
