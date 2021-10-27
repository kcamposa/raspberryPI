#### ------------------------------------------------  TESTING BRANCH ------------------------------------------------
import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time

sig = 0
buzzer = Buzzer(16)
portList = [23, 24, 25, 13, 19, 26, 22] # green1, yellow1, red1 ------- green2, yellow2, red2

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(portList, GPIO.OUT)

    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # push button
    GPIO.add_event_detect(6, GPIO.RISING, callback=CaptureSignal)

def main():
    try:
        while True:
            ChangingLights()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Stop running")
    GPIO.cleanup()

def ChangingLights():

    GPIO.output(portList, GPIO.LOW)

    LEDs_ON(23,26) # green 1 and red 2 ON
    time.sleep(5)

    LEDs_OFF(23,0) # green 1 OFF
    LEDs_ON(24,0) # yellow 1 ON
    time.sleep(2)

    Intermittent_LEDs(24,0) # intermittent yellow 1

    LEDs_OFF(26,0) # red 2 OFF
    LEDs_ON(25,13) # red 1 and green 2 ON
    activeCrosswalk()
    time.sleep(5)

    LEDs_OFF(13,0) # green 2 OFF
    LEDs_ON(19,0) # yellow 2 ON
    time.sleep(2)
    LEDs_OFF(22,0) # in case button was pushed
    buzzer.off() # in case button was pushed

    Intermittent_LEDs(19,0) # intermittent yellow 2

def CaptureSignal(channel): # capture the signal if the button was pushed
    global sig
    sig = 1

def activeCrosswalk(): # active the crosswalk 
    global sig 
    if sig == 1:
        LEDs_ON(22,0)
        buzzer.beep()
        sig = 0        

def LEDs_ON(led1, led2): # ON led or leds
    if led1 != 0 and led2 !=0:     
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
    elif led1 != 0 and led2 == 0:
        GPIO.output(led1, GPIO.HIGH)

def LEDs_OFF(led1, led2): # OFF led or leds
    if led1 != 0 and led2 !=0:     
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
    elif led1 != 0 and led2 == 0:
        GPIO.output(led1, GPIO.LOW)

def Intermittent_LEDs(led1, led2): # ON intermittent led or leds
    if led1 != 0 and led2 !=0:
        for i in range(5):
            LEDs_ON(led1,led2)
            time.sleep(.5)
            LEDs_OFF(led1,led2)
            time.sleep(.5)
    elif led1 != 0 and led2 == 0:
        for i in range(5):
            LEDs_ON(led1,0)
            time.sleep(.5)
            LEDs_OFF(led1,0)
            time.sleep(.5)


setup()
main()