import socket
# import datetime
import logging
# import threading


FORMAT = "%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


client = socket.socket()
address = ('127.0.0.1', 9999)
client.connect(address)

with client:
    for i in range(3):
        data = client.recv(1024)
        print(data)
        msg = b'abc'
        client.send(msg)
