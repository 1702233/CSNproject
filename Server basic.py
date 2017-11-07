import socket
s = socket.socket()
host = "145.89.163.69"
port = 54321
s.bind((host, port))

while True:
    s.listen(5)
    c, addr = s.accept()
    print("connectie van", addr)
    c.send(b"Er is connectie met de server")
    c.close()


