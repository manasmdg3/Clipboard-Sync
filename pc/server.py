import socket, threading
import copy_paste

HEADERSIZE = 10

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((socket.gethostname(), 2424))

def send(clientsocket):
    while True:
        msg = copy_paste.getFromClipboard()
        msg = f"{len(msg):<{HEADERSIZE}}"+msg
        print(msg)
        clientsocket.send(bytes(msg,"utf-8"))
def receive(clientsocket):
    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = clientsocket.recv(16)
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
                print(full_msg[HEADERSIZE:])
                break

def start():
    conn.listen(1)
    clientsocket, address = conn.accept()
    print(f"Connection from {address} has been established.")
    thread1 = threading.Thread(target=send, args=(clientsocket,))
    thread2 = threading.Thread(target=receive, args=(clientsocket,))
    thread1.start()
    thread2.start()

if __name__ == "__main__":
    start()