import  RPi.GPIO as GPIO
from tkinter import *
import threading
import time
import telepot 
from telepot.loop import MessageLoop

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinTRIG=23
pinECHO=16
vSon=34300

move = 0

GPIO.setup(pinTRIG,GPIO.OUT)
GPIO.setup(pinECHO,GPIO.IN)
GPIO.output(pinTRIG,GPIO.LOW)

def getHour():
    while True:
        hour = time.strftime('%I:%M:%S')
        hourValue.config(text=hour)
        
def getDate():
    while True: 
        date = time.strftime('%d:%m:%y')
        dateValue.config(text=date)

def botfunction(value):
    
    chatID = value['chat']['id']
    command = value['text']      

def SafeZone():
    global move 
    if move == 0:
        print("The zone es is safe.")
    else:
        print("The zone isn't safe. Movement detected some seconds ago.")
        SafeZone_ON_OFF(0)

def SafeZone_ON_OFF(value):
    global move
    move = value

token = '2123194698:AAG1O395gfxg1fcbPbVtXQhQKJq5CeCXhCg'
connBot = telepot.Bot(token)
MessageLoop(connBot, botfunction).run_as_thread()

def getDistance():
    counter = 0
    while True:
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

        distanceValue.config(text=distancia)
        print(str(distancia) + " cm.")
        
        if txtUmbral.get() != "":
            umbral = int(txtUmbral.get())
            print("Umbral ingresado de : " + str(umbral) + " cm.")
            if distancia > 0 and distancia < umbral:
                SafeZone_ON_OFF(1)
                connBot.sendMessage(2003138995, str("Alert!!...Your computer isn't safe, distance: ") + str(distancia) + str(" cm."))
                print("Alert!!...Your computer isn't safe, distance: " + str(distancia) + " cm.")
        else:
            print("No ha ingresado el umbral.")

        counter += 1
        if counter == 60:
            SafeZone()
            counter = 0

# definition window
window = Tk()
window.geometry("300x150")
window.title("Tarea")

frame = Frame(window)
frame.pack()

lbDate = Label(frame, text='Date: ', font=('Helvetica', 14))
dateValue = Label(frame, font=('Helvetica', 14) )
lbHour = Label(frame, text='Hour: ', font=('Helvetica', 14))
hourValue = Label(frame, font=('Helvetica', 14))
lbDistance = Label(frame, text='Distance: ', font=('Helvetica', 14))
distanceValue = Label(frame, font=('Helvetica', 14))
lbUmbral = Label(frame, text='Umbral: ', font=('Helvetica', 14))
lblcm = Label(frame, text='cm', font=('Helvetica', 14))
lblcm2 = Label(frame, text='cm', font=('Helvetica', 14))

boton1 = Button(frame, text='Aceptar', fg='red', height=1 ,width=5, padx=10, command=getDistance)

txtUmbral = Entry(frame, width=4, font=('Helvetica', 14))

lbDate.grid(row=0, column=0)
dateValue.grid(row=0, column=1)
lbHour.grid(row=1, column=0)
hourValue.grid(row=1, column=1)
lbDistance.grid(row=2, column=0)
distanceValue.grid(row=2, column=1)
lblcm.grid(row=2, column=2)
lbUmbral.grid(row=3, column=0)
txtUmbral.grid(row=3, column=1)
lblcm2.grid(row=3, column=2)
boton1.grid(row=3, column=3)

hourThread = threading.Thread(name='Hour', target=getHour, daemon=True)
dateThread = threading.Thread(name='Date', target=getDate, daemon=True)
distanceThread = threading.Thread(name='Distance', target=getDistance, daemon=True)

hourThread.start()
dateThread.start()
distanceThread.start()

window.mainloop()
