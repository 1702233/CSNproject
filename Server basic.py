import socket
s = socket.socket()
host = ""
port = "54321"
s.bind((host, port))

while True:
    s.listen(4)
    c, addr = s.accept()
    print("connectie van", addr)
    c.send("Er is connectie met de server")
    c.close()


