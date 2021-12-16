import  time
import  urllib.request
import  random
import  os

tokenAPI='R5W8MBF7M6OBOR1M'
URL='https://api.thingspeak.com/update?api_key=%s'%tokenAPI

date = time.strftime("%d-%m-%y")
clock = time.strftime("%I:%M:%S")
nombre="/home/pi/"+"log"+date+".txt"

if os.path.exists(nombre):
    print ("El archivo existe")
else:
    print ("No existe el archivo")
    archivo=open(nombre,"w")
    archivo.write("Fecha,Hora,Temperatura")
    archivo.close()

def sinRPi():
    dato=random.randrange(10)
    return dato

def obtenerTemp():
    var=open('/sys/class/thermal/thermal_zone0/temp')
    tempCPU=float(var.read())/1000
    return tempCPU

def bitacora(parametro):
    archivo=open(nombre,"a")
    archivo.write(date)
    archivo.write(",")
    archivo.write(clock)
    archivo.write(",")
    Temp=str(parametro)
    archivo.write(Temp)
    archivo.write("\n")
    archivo.close()

try:
    while True:
        dato1=obtenerTemp() #No usar con QEMU
        dato2=sinRPi()
        bitacora(dato1)
        urllib.request.urlopen(URL+'&field1=%s&field2=%s'%(dato1,dato2))
        print ("Los datos enviados son: ", dato1, dato2)
        time.sleep(15)
except KeyboardInterrupt:
    print ('Fin')