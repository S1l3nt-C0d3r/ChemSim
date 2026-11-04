import tkinter
import threading
import pyttsx3 as sound
from tkinter import *
def srun():

    win2=Tk()
    def openFunctional():
        win2.destroy()
        import src.Virtual_Lab.Functional.SelecterscreenFunctional as SelecterscreenFunctional
    def openAnionFunction():
        win2.destroy()
        import src.Virtual_Lab.Anions.SelecterscreenAnion as SelecterscreenAnion
    def openCationFunction():
        win2.destroy()
        import src.Virtual_Lab.Cations.Selecterscreen as Selecterscreen
        Selecterscreen.ssrun()
    global tosay
    tosay=sound.init()
    def thread1():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        tosay.say("Welcome to Virtual Lab")
        tosay.runAndWait()

    t1 = threading.Thread(target=thread1)
    t1.start()
    virtual=PhotoImage(file="virtual lab.png")
    virtualbackground = PhotoImage(file="virtual lab background.png")
    tkinter.Label(win2,image=virtualbackground).pack()
    tkinter.Label(win2,image=virtual).place(y=10,x=100)
    function = tkinter.Button(text=("Functional Groups"),bg="#46A0EC",fg="White",width=15,borderwidth=1,font=("",18),height=2,command=openFunctional,cursor="hand2")
    function.place(x=140,y=400)
    cation = tkinter.Button(text=("Cation"),bg="#46A0EC",fg="White",width=10,borderwidth=1,font=("",18),height=2,command=openCationFunction,cursor="hand2")
    cation.place(x=45,y=320)
    anion = tkinter.Button(text=("Anion"),bg="#46A0EC",fg="White",width=10,borderwidth=1,font=("",18),height=2,command=openAnionFunction,cursor="hand2")
    anion.place(x=300,y=320)
    win2.geometry("500x500+500+150")
    win2.resizable(0,0)
    win2.title("Virtual Lab")
    win2.mainloop()