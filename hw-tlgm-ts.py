import  RPi.GPIO as GPIO
import  time
import telepot 
from telepot.loop import MessageLoop
import urllib.request

RedLED = 20
pinTRIG=23
pinECHO=16
vSon=34300

tokenAPI='R5W8MBF7M6OBOR1M'
URL='https://api.thingspeak.com/update?api_key=%s'%tokenAPI

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(RedLED, GPIO.OUT)
    GPIO.setup(pinTRIG,GPIO.OUT)
    GPIO.setup(pinECHO,GPIO.IN)
    GPIO.output(pinTRIG,GPIO.LOW)

def main():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
            GPIO.cleanup()
            print("Finnish")
    GPIO.cleanup()

def LEDs_ON(led1): 
    GPIO.output(led1, GPIO.HIGH)

def LEDs_OFF(led1):
    GPIO.output(led1, GPIO.LOW)

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
    return distancia

def botfunction(value):
    chatID = value['chat']['id']
    command = value['text']
    print(command)

    if command=='/?':
        connBot.sendMessage(chatID, str("\n OPTIONS: \n /ledON \n /ledOFF \n /Distance"))
    elif command == '/ledON':
        connBot.sendMessage(chatID, str("Red Led is On now. "))
        LEDs_ON(20)
    elif command == '/ledOFF':
        connBot.sendMessage(chatID, str("Red Led is Off now. "))
        LEDs_OFF(20)
    elif command == '/Distance':
        d = distance()
        connBot.sendMessage(chatID, str("Distance: ") + str(d) + str(" cm."))
        if d > 0 and d < 30:
            urllib.request.urlopen(URL+'&field4=%s'%(1))
        else:
            urllib.request.urlopen(URL+'&field4=%s'%(0))
        

token = '2123194698:AAG1O395gfxg1fcbPbVtXQhQKJq5CeCXhCg'
connBot = telepot.Bot(token)
#print(connBot.getMe())
MessageLoop(connBot, botfunction).run_as_thread()



setup()
main()