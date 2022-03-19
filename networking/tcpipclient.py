import socket

s = socket.socket()

s.connect(("localhost", 4000))

# receive byte data from the socket. k(buffsize) -> maximum # of data at per receive
msg = s.recv(1024)

while msg:
    print("Received: ", msg.decode())
    msg = s.recv(1024)

s.close()
