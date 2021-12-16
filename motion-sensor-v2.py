import RPi.GPIO as GPIO
import time

PIR_PIN = 18
move = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motionON)

def main():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Stop running")
    GPIO.cleanup()


def motionON(channel):
    global move
    move = 1 # variable global que cambia a 1 si detecta movimiento
    print("Se ha detectado un movimiento.")
    motionOFF()

def motionOFF():
    global move
    move = 0 # variable global que cambia a 0 para devolverla al estado antiguo y que vuelva a detectar movimiento
    print("Se ha reseteado el estado de la variable del movimiento.")

setup()
main()