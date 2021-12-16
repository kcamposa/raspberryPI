import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT) # buzzer
triggerPIN = 16

try:
    while True:
        GPIO.output(triggerPIN, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(triggerPIN, GPIO.LOW)
        time.sleep(.1)
        GPIO.output(triggerPIN, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(triggerPIN, GPIO.LOW)
        time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stop running")
GPIO.cleanup()