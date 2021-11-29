import  RPi.GPIO as GPIO
import  time
import telepot 
from telepot.loop import MessageLoop
import urllib.request

RedLED = 20
PIR_PIN = 18

pinTRIG=23
pinECHO=16
vSon=34300

sig = 0
move = 0

tokenAPI='R5W8MBF7M6OBOR1M'
URL='https://api.thingspeak.com/update?api_key=%s'%tokenAPI


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(RedLED, GPIO.OUT)
    GPIO.setup(pinTRIG,GPIO.OUT)
    GPIO.setup(pinECHO,GPIO.IN)
    GPIO.output(pinTRIG,GPIO.LOW)
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motionON)

def main():
    try:
        while True:
            time.sleep(60)
            SafeZone()
    except KeyboardInterrupt:
            GPIO.cleanup()
            print("Finnish")
    GPIO.cleanup()

def LED_ON(led1): 
    GPIO.output(led1, GPIO.HIGH)

def LED_OFF(led1):
    GPIO.output(led1, GPIO.LOW)

def SafeZone():
    global move 
    if move == 0:
        connBot.sendMessage(2003138995, str("The zone es is safe. "))
        print("The zone es is safe.")
    else:
        connBot.sendMessage(2003138995, str("The zone isn't safe. Movement detected some seconds ago."))
        print("The zone isn't safe. Movement detected some seconds ago.")
        motionOFF()

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
def alarmON():
    global sig
    sig = 1
    LED_ON(RedLED)
    print("Alarm is ON now.")
    connBot.sendMessage(2003138995, str("Alarm is ON now. "))
    urllib.request.urlopen(URL+'&field5=%s'%(1))

def alarmOFF():
    global sig
    sig = 0
    LED_OFF(RedLED)
    print("Alarm is OFF now.")
    connBot.sendMessage(2003138995, str("Alarm is OFF now. "))
    urllib.request.urlopen(URL+'&field5=%s'%(0))

def motionON(channel):
    global move
    move = 1
    d = distance()
    if d > 0 and d < 50:
        connBot.sendMessage(2003138995, str("Alert!!...Your computer isn't save, distance: ") + str(d) + str(" cm."))
        print("Alert!!...Your computer isn't save, distance: ", d)

    print("Alert!!...Movement detected in your room.")    

def motionOFF():
    global move
    move = 0

def botfunction(value):
    
    chatID = value['chat']['id']
    command = value['text']
    print(command)

    if command=='/?':
        connBot.sendMessage(chatID, str("\n OPTIONS: \n /alarmON \n /alarmOFF \n /Distance"))
    elif command == '/alarmON':
        alarmON()
    elif command == '/alarmOFF':
        alarmOFF()
    elif command == '/Distance':
        if sig == 1:
            d = distance()
            if d > 0 and d < 50:
                connBot.sendMessage(2003138995, str("Alert!!...Your computer isn't save, distance: ") + str(d) + str(" cm."))
            else:
                connBot.sendMessage(2003138995, str("Alert!!...Your computer is save, distance: ") + str(d) + str(" cm."))
            motionOFF()
        else:
            connBot.sendMessage(chatID, str("Sorry, the alarm is OFF."))     

token = '2123194698:AAG1O395gfxg1fcbPbVtXQhQKJq5CeCXhCg'
connBot = telepot.Bot(token)
MessageLoop(connBot, botfunction).run_as_thread()


setup()
main()