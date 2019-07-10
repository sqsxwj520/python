import selectors
import socket


s = selectors.DefaultSelector()

server = socket.socket()
server.bind(('127.0.0.1', 9999))
server.listen()

server.setblocking(False)


def accept(conn: socket.socket, msk: int):
    print(msk)
    conn, r_address = conn.accept()
    conn.setblocking(False)
    keys = s.register(conn, selectors.EVENT_READ, rec)
    print(keys)


def rec(conn: socket.socket, msk: int):
    data = conn.recv(1024)
    print(data)
    print(msk)

    msg = 'Your msg {} form {}'.format(data.decode(), conn.getpeername())
    conn.send(msg.encode())


key = s.register(server, selectors.EVENT_READ, accept)
print(key)

while True:
    events = s.select()
    print(events)

    for key, mask in events:
        print(type(key), type(mask))
        key.data(key.fileobj, mask)

server.close()
s.close()
