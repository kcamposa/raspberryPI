import  RPi.GPIO as GPIO
import  time
import urllib.request

tokenAPI='R5W8MBF7M6OBOR1M'
URL='https://api.thingspeak.com/update?api_key=%s'%tokenAPI

def getTemp(): 
    var = open('/sys/class/thermal/thermal_zone0/temp')
    tempCPU = float(var.read())/1000
    print("Temperature: ", tempCPU)
    return tempCPU

def main():
    try:
        while True:
            time.sleep(1)
            data1 = getTemp()
            urllib.request.urlopen(URL+'&field3=%s'%(data1))

    except KeyboardInterrupt:
            GPIO.cleanup()
            print("Finnish")
    GPIO.cleanup()

main()