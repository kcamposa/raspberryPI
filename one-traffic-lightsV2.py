
import RPi.GPIO as GPIO
import time

portList = [23, 24, 25] # verde1, amarillo1, rojo1 

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(portList, GPIO.OUT)

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
    for port in portList:
        [print("ON Green LED ") if port==23 else print("ON Yellow LED") if port==24 else print("ON Red LED")]
        GPIO.output(port, GPIO.HIGH)
        [time.sleep(7) if port==23 else time.sleep(2) if port==24 else time.sleep(5)]
        GPIO.output(port, GPIO.LOW)
        [print("OFF Green LED") if port==23 else print("OFF Yellow LED ") if port==24 else print("OFF Red LED")]

setup()
run()