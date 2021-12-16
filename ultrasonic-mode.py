import  RPi.GPIO as GPIO
import  time

pinTRIG=23
pinECHO=16
vSon=34300

ledPorts = [20,21]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 

    GPIO.setup(pinTRIG,GPIO.OUT)
    GPIO.setup(pinECHO,GPIO.IN)

    GPIO.output(pinTRIG,GPIO.LOW)

    GPIO.setup(ledPorts, GPIO.OUT)

def main():
    try:
        while True:
            alertDist = inside()
            alert(alertDist)
    except KeyboardInterrupt:
            GPIO.cleanup()
            print("Fin")
    GPIO.cleanup()

def inside():
    time.sleep(1)
    GPIO.output(pinTRIG,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(pinTRIG,GPIO.LOW)
    while GPIO.input(pinECHO)==0:
            tinicio=time.time()
    while GPIO.input(pinECHO)==1:
            tfin=time.time()
    tvuelo=tfin-tinicio
    distancia=tvuelo*vSon/2
    distancia=round(distancia,2)
    print("La distancia es: ",distancia)
    return distancia

def alert(value):
    
    if value <= 10:
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        time.sleep(1)
        #print("Cuidado muy cerca", valor)
    elif value > 10 and value < 30:
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
        time.sleep(1)
        #print("Esta cerca", valor)
    else:
        #print("Zona segura", valor)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
        time.sleep(1)
    GPIO.output(ledPorts, GPIO.LOW)


setup()
main()
