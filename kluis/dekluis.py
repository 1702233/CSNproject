import RPi.GPIO as GPIO
import time
import pygame
import socket

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) #groen
GPIO.setup(4, GPIO.OUT) #geel
GPIO.setup(5, GPIO.OUT) #rood
GPIO.setup(13, GPIO.OUT) #buzzer
GPIO.setup(22, GPIO.IN) #knop alarm aan
GPIO.setup(6, GPIO.IN) #knop vals alarm, van geel naar groen
GPIO.setup(19, GPIO.IN) #knop alarm stoppen, van rood naar groen

def AlarmAan():
    pygame.mixer.init()
    pygame.mixer.music.load("alarmsound.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)


def AlarmUit():
    pygame.mixer.init()
    pygame.mixer.music.load("alarmsound.mp3")
    pygame.mixer.music.stop()

def preAlarmAan():
    pygame.mixer.init()
    pygame.mixer.music.load("alarmgeluid.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)

def preAlarmUit():
    pygame.mixer.init()
    pygame.mixer.music.load("alarmgeluid.mp3")
    pygame.mixer.music.stop()

#def buzzer():
#    GPIO.output(13, GPIO.HIGH)
#    time.sleep(0.5)
#    GPIO.output(13, GPIO.LOW)
#    time.sleep(0.5)
#    GPIO.output(13, GPIO.HIGH)
#    time.sleep(0.5)
#    GPIO.output(13, GPIO.LOW)
#    time.sleep(0.5)

#while True:
#    buzzer()

#connectie
#s = socket.socket()
#host = "169.164.42.1"
#port = 54321
#s.connect((host, port))
#print(s.recv(1024).decode())
#s.send("test")
#s.close()

#HUIS:
GPIO.output(17, GPIO.HIGH)
GPIO.output(4, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
loopcount = 0

while True:
    while True:
        if GPIO.input(22) == True:
            preAlarmAan()
            GPIO.output(17, GPIO.LOW)
            GPIO.output(4, GPIO.HIGH)
            s = socket.socket()
            host = "192.168.42.1"
            port = 54321
            s.connect((host, port))
            ontvangen = s.recv(1024).decode()
            s.send("test")
            if ontvangen == "preAlarmUit":
                preAlarmUit()
            if ontvangen == "geelnaargroen":
                GPIO.output(4, GPIO.LOW)
                GPIO.output(17, GPIO.HIGH)
            if ontvangen == "geelnaarrood":
                AlarmAan()
                GPIO.output(4, GPIO.LOW)
                GPIO.output(5, GPIO.HIGH)
                break
            s.close()


    while True:
        if GPIO.input(19) == True:
            AlarmUit()
            GPIO.output(5, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            break