import  RPi.GPIO as GPIO
import tkinter as tk
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RedLED = 20
pinTRIG=23
pinECHO=16
vSon=34300

GPIO.setup(20,GPIO.OUT)
GPIO.setup(pinTRIG,GPIO.OUT)
GPIO.setup(pinECHO,GPIO.IN)
GPIO.output(pinTRIG,GPIO.LOW)


def distance():
    GPIO.output(RedLED, GPIO.LOW)
    x = seleccion.get()
    if x == 1: 
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
        print(distancia)
        window.update()
        distance()
        #return distancia
    else:
        # encender un led
        GPIO.output(RedLED, GPIO.HIGH)
        print("Apagado.")

# definition window
window = tk.Tk()
window.geometry("600x600")
window.title("Tarea")

lb = tk.Label(window,text='Esto es un ejemplo de ventana Tkinter')
lb.pack()

seleccion = tk.IntVar()
seleccion.set(0)

boton1 = tk.Radiobutton(window, text='Medir', variable=seleccion,fg='blue', indicator=1, width=10, padx=20, value=1, command=distance)
boton1.pack()
boton2 = tk.Radiobutton(window, text='No medir', variable=seleccion,fg='red', indicator=1, width=10, padx=20, value=0)
boton2.pack()


window.mainloop()

