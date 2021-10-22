
#### ---------------------------------------------------------------------------------  TESTING BRANCH ---------------------------------------------------------------------------------

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

    # green 1 and red 2
    LEDs(23, 26)
    time.sleep(5)

    GPIO.output(23, GPIO.LOW) # green 1 off

    # yellow 1, intermittent yellow 1
    GPIO.output(24, GPIO.HIGH)
    time.sleep(2)
    intermittentLED(24)

    GPIO.output(26, GPIO.LOW) # red 2 off

    # red 1 and green 2
    LEDs(25, 13)
    time.sleep(5)

    GPIO.output(13, GPIO.LOW) # green 2 off

    # yellow 2, intermittent yellow 2
    GPIO.output(19, GPIO.HIGH)
    time.sleep(2)
    intermittentLED(19)

def intermittentLED(led):
    for i in range(5):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(led, GPIO.LOW)
        time.sleep(.5)

def pushedButton(): # crosswalk
    if GPIO.input(6) == GPIO.LOW:
        GPIO.output(portList, GPIO.LOW)
        for i in range(5):
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
            time.sleep(.5)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            time.sleep(.5)
        GPIO.output(portList, GPIO.LOW)
        buzzer.beep()
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        time.sleep(7)
        buzzer.off()
        run()

def LEDs(led1, led2):
    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2, GPIO.HIGH)

setup()
run()