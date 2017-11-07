import socket

s = socket.socket()
host = "145.89.163.69"
port = 54321
s.connect((host, port))
print(s.recv(1024).decode())
s.close()
