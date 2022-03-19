import socket

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print("Server listening on port:", port)
s.listen(1)

conn, addr = s.accept()

fileName = conn.recv(1024)

try:
    f = open(fileName, 'rb')
    content = f.read()
    conn.send(content)
    f.close()
except FileNotFoundError:
    conn.send(b"File doesn't exist")

conn.close()
