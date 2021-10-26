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
            input_state=GPIO.input(6)
            if input_state == False:
                ChangingLights()
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Stop running")
    GPIO.cleanup()

def ChangingLights():

    GPIO.output(portList, GPIO.LOW)

    LEDsON(23,26) # green 1 and red 2 ON
    time.sleep(5)

    LEDsOFF(23,0) # green 1 OFF
    LEDsON(24,0) # yellow 1 ON
    time.sleep(2)

    IntermittentLEDs(24,0) # intermittent yellow 1

    LEDsOFF(26,0) # red 2 OFF
    LEDsON(25,13) # red 1 and green 2 ON
    time.sleep(5)

    LEDsOFF(13,0) # green 2 OFF
    LEDsON(19,0) # yellow 2 ON
    time.sleep(2)

    IntermittentLEDs(19,0) # intermittent yellow 2

def Crosswalk(): 
    if GPIO.input(6) == GPIO.LOW:
        GPIO.output(portList, GPIO.LOW)
        IntermittentLEDs(24,19) # intermittent yellow 1 and 2
        GPIO.output(portList, GPIO.LOW)
        #buzzer.beep()
        LEDsON(25,26) # red 1 and 2 on
        time.sleep(7)
        IntermittentLEDs(25,26) # intermittent red 1 and 2
        #buzzer.off()
        run()

def LEDsON(led1, led2): # ON led or leds
    if led1 != 0 and led2 !=0:     
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
    elif led1 != 0 and led2 == 0:
        GPIO.output(led1, GPIO.HIGH)

def LEDsOFF(led1, led2): # OFF led or leds
    if led1 != 0 and led2 !=0:     
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
    elif led1 != 0 and led2 == 0:
        GPIO.output(led1, GPIO.LOW)

def IntermittentLEDs(led1, led2): # ON intermittent led or leds
    if led1 != 0 and led2 !=0:
        for i in range(5):
            LEDsON(led1,led2)
            time.sleep(.5)
            LEDsOFF(led1,led2)
            time.sleep(.5)
    elif led1 != 0 and led2 == 0:
        for i in range(5):
            LEDsON(led1,0)
            time.sleep(.5)
            LEDsOFF(led1,0)
            time.sleep(.5)


def know_state():
    input_state=GPIO.input(6)


setup()
run()