#### ------------------------------------------------  TESTING BRANCH ------------------------------------------------
import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time

buzzer = Buzzer(16)
portList = [23, 24, 25, 13, 19, 26] # green1, yellow1, red1 ------- green2, yellow2, red2

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(portList, GPIO.OUT)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # push button

def run():
    try:
        while True:
            led_virtual_switch()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Stop running")
    GPIO.cleanup()

def led_virtual_switch():
    GPIO.output(portList, GPIO.LOW)

    Crosswalk()
    LEDsON(23,26) # green 1 and red 2 on
    time.sleep(5)

    Crosswalk()
    LEDsOFF(23,0) # green 1 off
    
    Crosswalk()
    LEDsON(24,0) # yellow 1 on
    time.sleep(2)
    IntermittentLED(24) # intermittent yellow 1

    Crosswalk()
    LEDsOFF(26,0) # red 2 off

    Crosswalk()
    LEDsON(25,13) # red 1 and green 2 on
    time.sleep(5)

    LEDsOFF(13,0) # green 2 off

    Crosswalk()
    LEDsON(19,0) # yellow 2 on
    time.sleep(2)
    IntermittentLED(19) # intermittent yellow 2

def IntermittentLED(led):
    for i in range(5):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(led, GPIO.LOW)
        time.sleep(.5)

def Crosswalk(): # crosswalk
    if GPIO.input(6) == GPIO.LOW:
        GPIO.output(portList, GPIO.LOW)
        for i in range(5):
            LEDsON(24,19) # yellow 1 and 2 on intermittent
            time.sleep(.5)
            LEDsOFF(24,19) # yellow 1 and 2 off intermittent
            time.sleep(.5)
        GPIO.output(portList, GPIO.LOW)
        #buzzer.beep()
        LEDsON(25,26) # red 1 and 2 on
        time.sleep(7)
        #buzzer.off()
        run()

def LEDsON(led1, led2):
    if led1 != 0 and led2 !=0:     
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
    elif led1 != 0 and led2 == 0:
        GPIO.output(led1, GPIO.HIGH)

def LEDsOFF(led1, led2):
    if led1 != 0 and led2 !=0:     
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
    elif led1 != 0 and led2 == 0:
        GPIO.output(led1, GPIO.LOW)

setup()
run()