import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT) # blue

try:
    while True:

        GPIO.output(22, GPIO.HIGH)
        time.sleep(3)    
        GPIO.output(22, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    print("Finalizado por el usuario")
    GPIO.cleanup()
GPIO.cleanup()

