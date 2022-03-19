import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket to address(host + port)
s.bind((host, port))
print("Server listening on port:", port)

# enable a server to accept connections. the number (k) specifies the
# number of unaccepted connections that the system will allow before setting
# a new connection.
s.listen(5)

# return new socket object and its address
c, addr = s.accept()

print("Connection from:", str(addr))

# send data to the socket
c.send(b"Hello, how are you")
c.send("bye".encode())
c.close()
