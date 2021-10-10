import socket
import copy_paste

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2424))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")
while True:
    msg = copy_paste.getFromClipboard()
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    print(msg)
    clientsocket.send(bytes(msg,"utf-8"))