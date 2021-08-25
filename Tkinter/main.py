import tkinter
from tkinter import *

ventana = tkinter.Tk()

ventana.geometry("200x300")

ventana.title("Actividad Tkinder SSE.") #Titulo

ventana.config(bg="silver") #Color de la ventana

btn = Button(ventana, text="Este es el botón ;)") #Botón

etq = Label(ventana, text = "Esta es \n la ventana del ejercicio \n de Tkinter. \n", bg="blue",font="Times 15") #Etiqueta

etq.pack()
btn.pack()

ventana.mainloop()