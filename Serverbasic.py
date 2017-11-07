import socket
s = socket.socket()
host = "192.168.42.2"
port = 54321
s.bind((host, port))

while True:
    file1 = open("connectietest.txt", "w")
    file1.write("python heeft gerunt.")
    file1.close()
    s.listen(2)
    c, addr = s.accept()
    print("connectie van", addr)
    file1 = open("connectietest.txt", "w")
    file1.write("connectie van "+ addr)
    file1.close()
    c.send(b"Er is connectie met de server")
    c.close()