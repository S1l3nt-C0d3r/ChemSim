import tkinter
from tkinter import *
import pyttsx3
import pandas
win90=Tk()
bgimg=PhotoImage(file="vivabg.png")
win90.geometry("500x500+500+150")
tkinter.Label(win90,image=bgimg).pack()
def viva():
    win90.destroy()
    import Assess_Thyself.viva as viva
logoimg=PhotoImage(file="vivalogoimg.png")
tkinter.Label(win90,image=logoimg).place(x=100,y=30)
tkinter.Button(text="START",bg="#E8EDFF", fg="black",font="Titilium 20 bold",width=15,height=2,borderwidth=5,cursor="hand2",command=viva).place(x=120,y=380)
win90.mainloop()