import socket

s = socket.socket()

s.connect(("localhost", 6767))

fileName = input("Enter a file name:")

s.send(fileName.encode())

msg = s.recv(1024)


while msg:
    print("Received: ", msg.decode())
    msg = s.recv(1024)


s.close()
