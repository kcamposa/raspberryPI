
import RPi.GPIO as GPIO
import time

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0

try:
    while True:
        input_state=GPIO.input(6)
        if input_state == False:
            count += 1 
            print("Button was pushed " +str(count)+ " times")
            time.sleep(.3)
        time.sleep(.1)

except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
GPIO.cleanup()