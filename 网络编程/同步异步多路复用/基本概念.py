import selectors
import socket


s = selectors.DefaultSelector()  # 1拿到selector

# 准备类文件对象
server = socket.socket()
server.bind(('127.0.0.1', 9997))
server.listen()

# 官方建议采用非阻塞IO
server.setblocking(False)


def accept(sock: socket.socket, mas: int):
    conn, r_address = sock.accept()
    # print(conn)
    # print(r_address)
    print(mas)
    # pass
    conn.setblocking(False)
    key1 = s.register(conn, selectors.EVENT_READ, rec)
    print(key1)


def rec(conn: socket.socket, mas: int):
    print(mas)
    data = conn.recv(1024)
    print(data)

    msg = 'Your msg = {} form {}'.format(data.decode(), conn.getpeername())
    conn.send(msg.encode())


# 2注册关注的类文件对象和其事件们
key = s.register(server, selectors.EVENT_READ, accept)  # socket fileobject
print(key)

while True:
    events = s.select()  # epoll select,默认是阻塞的
    # 当你注册时的文件对象们，这其中的至少一个对象关注的事件就绪了，就不阻塞了
    print(events)  # 获得了就绪的对象们，包括就绪的事件，还会返回data

    for key, mask in events:  # event =>key, mask
        # 每一个event都是某一个被观察的就绪的对象
        print(type(key), type(mask))   # key, mask
        # <class 'selectors.SelectorKey'> <class 'int'>
        print(key.data)
        # <function accept at 0x0000000001EA3A60>
        key.data(key.fileobj, mask)  # mask为掩码

server.close()
s.close()
