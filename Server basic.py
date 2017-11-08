import socket
import datetime

print("start")
s = socket.socket()
host = ""
port = 54321
s.bind((host, port))

s.listen(2)
c, addr = s.accept()

while True:
    ontvangen = c.recv(1024).decode()
    if ontvangen == "alarm gaat af":
        print("alarm gaat af")
        vandaag = datetime.datetime.today()
        datumtijd = vandaag.strftime("%a %x %X")
        with open("server.txt", "a") as schrijven:
            schrijven.write("{:5} - {:5} {}".format("alarm gaat af", datumtijd, "\n"))
            print(datumtijd)
    if ontvangen == "vals alarm":
        print("vals alarm")
        vandaag = datetime.datetime.today()
        datumtijd = vandaag.strftime("%a %x %X")
        with open("server.txt", "a") as schrijven:
            schrijven.write("{:5} - {:5} {}".format("vals alarm", datumtijd, "\n"))
            print(datumtijd)
    if ontvangen == "alarm":
        print("alarm")
        vandaag = datetime.datetime.today()
        datumtijd = vandaag.strftime("%a %x %X")
        with open("server.txt", "a") as schrijven:
            schrijven.write("{:5} - {:5} {}".format("alarm", datumtijd, "\n"))
            print(datumtijd)
    if ontvangen == "alarm reset":
        print("alarm reset")
        vandaag = datetime.datetime.today()
        datumtijd = vandaag.strftime("%a %x %X")
        with open("server.txt", "a") as schrijven:
            schrijven.write("{:5} - {:5} {}".format("alarm reset", datumtijd, "\n"))
            print(datumtijd)
    if ontvangen == "break":
        break
c.close()
