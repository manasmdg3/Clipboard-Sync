import socket, threading
import copy_paste

HEADERSIZE = 10

def receive(conn):
    pass

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((socket.gethostname(), 2424))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = conn.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE].decode('utf-8'))
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")
        msg = b''
        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            conn.send(b"full_msg recvd")
            print(full_msg[HEADERSIZE:])
            break

