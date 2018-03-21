import socket
import ssl
import hashlib
import time

msock = socket.create_connection(('pop.gmail.com', 995))
with ssl.wrap_socket(msock, ssl_version=ssl.PROTOCOL_SSLv23) as sock:
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    sock.sendall(("USER address@gmail.com\n\r").encode())
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    sock.send(("PASS password\n\r").encode())
    data = sock.recv(1024)
    print(data.decode('utf-8'))
