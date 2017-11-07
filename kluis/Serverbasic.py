import RPi.GPIO as GPIO
import socket
import time
s = socket.socket()
host = "192.168.42.1"
port = 54321
s.bind((host, port))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) #groen
GPIO.setup(4, GPIO.OUT) #geel
GPIO.setup(5, GPIO.OUT) #rood
GPIO.setup(13, GPIO.OUT) #buzzer
GPIO.setup(22, GPIO.IN) #knop alarm aan
GPIO.setup(6, GPIO.IN) #knop vals alarm, van geel naar groen
GPIO.setup(19, GPIO.IN) #knop alarm stoppen, van rood naar groen

while True:
    s.listen(2)
    c, addr = s.accept()
    print("connectie van", addr)
    file1 = open("connectietest.txt", "w")
    file1.write("connectie van "+ str(addr))
    file1.close()
    c.send(b"Er is connectie met de server")
    teller_tijd = 0
    teller = 0
    print(c.recv(1024))
    if c.recv(1024) == "test":
        print("doet het")
        while teller_tijd < 5:
            time.sleep(0.5)
            teller_tijd += 0.5
            if GPIO.input(6) == True:
                c.send(b"preAlarmUit")
                #preAlarmUit()
                teller += 1
                break
        if teller == 1:
            c.send(b"geelnaargroen")
        elif teller == 0:
            c.send(b"geelnaarrood")
    c.close()
