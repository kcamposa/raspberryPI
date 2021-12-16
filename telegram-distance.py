import  RPi.GPIO as GPIO
import  time

import telepot 
from telepot.loop import MessageLoop

pinTRIG=23
pinECHO=16
vSon=34300


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 

    GPIO.setup(pinTRIG,GPIO.OUT)
    GPIO.setup(pinECHO,GPIO.IN)
    GPIO.output(pinTRIG,GPIO.LOW)

def main():
    try:
        while True:
            time.sleep(1)
            token = '2123194698:AAG1O395gfxg1fcbPbVtXQhQKJq5CeCXhCg'
            connBot = telepot.Bot(token)
            chatID = 2003138995
            dis = distance()
            connBot.sendMessage(chatID, str("Auto Distance: ") + str(dis) + str(" cm."))
    except KeyboardInterrupt:
            GPIO.cleanup()
            print("Finnish")
    GPIO.cleanup()

def distance():
    time.sleep(1)
    GPIO.output(pinTRIG,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(pinTRIG,GPIO.LOW)
    while GPIO.input(pinECHO)==0:
            tinicio=time.time()
    while GPIO.input(pinECHO)==1:
            tfin=time.time()
    tvuelo=tfin-tinicio
    distancia=tvuelo*vSon/2
    distancia=round(distancia,2)
    print("La distancia es: ",distancia)
    return distancia

def botfunction(value):
    chatID = value['chat']['id']
    command = value['text']

    print(command)

    if command=='/Hellouda':
        connBot.sendMessage(chatID, str("\n opciones: /LedOn \n /ledOff \n "))
    elif command == '/ledon':
        connBot.sendMessage(chatID, str(" Led is On now. "))

token = '2123194698:AAG1O395gfxg1fcbPbVtXQhQKJq5CeCXhCg'
connBot = telepot.Bot(token)
#print(connBot.getMe())
MessageLoop(connBot, botfunction).run_as_thread() 

setup()
main()