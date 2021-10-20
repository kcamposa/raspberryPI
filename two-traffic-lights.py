
import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time

buzzer = Buzzer(16)
portList = [23, 24, 25, 13, 19, 26] # verde1, amarillo1, rojo1 ------- verde2, amarillo2, rojo2

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
    # verde 1
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    pushedButton()
    # rojo 2
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(5)  
    pushedButton()
    # amarillo 1
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.LOW)
    # rojo 2 --- parpadeante
    time.sleep(2)
    intermittentLED(24)
    pushedButton()
    # rojo 1
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)
    pushedButton()
    # verde 2
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    time.sleep(5)
    pushedButton()
    # amarillo 2
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    pushedButton()
    # rojo 1 --- parpadeante
    time.sleep(2)
    intermittentLED(19)

def intermittentLED(led):
    for i in range(5):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(led, GPIO.LOW)
        time.sleep(.5)

def pushedButton():
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


setup()
run()