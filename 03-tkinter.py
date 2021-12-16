import tkinter as tk

window = tk.Tk()
window.geometry("600x600")

window.title("Ejemplo de programa tkinter")

lb = tk.Label(window,text='Esto es un ejemplo de ventana Tkinter')
lb.pack()

boton1 = tk.Radiobutton(window, text='Aceptar', fg='blue', indicator=1, width=10, padx=20, value=1)
boton1.pack()

boton2 = tk.Radiobutton(window, text='Cancelar', fg='red', indicator=1, width=10, padx=20, value=0)
boton2.pack()


window.mainloop()