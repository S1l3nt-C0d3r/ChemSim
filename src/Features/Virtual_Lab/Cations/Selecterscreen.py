import os
import runpy
import tkinter
from tkinter import ttk
from tkinter import *
import random
import pyttsx3 as sound
import threading
def ssrun():
    global tosay
    tosay=sound.init()
    win6=Tk()
    win6.geometry("500x500+500+150")
    win6.resizable(0,0)
    global img1
    img1=PhotoImage(file="virtual lab background.png")
    tkinter.Label(win6,image=img1).pack()
    def thread1():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        tosay.say("Please choose or randomly generate a cation for Analysis")
        tosay.runAndWait()
        if tosay._inLoop:
            tosay.endLoop()
    t1 = threading.Thread(target=thread1)
    t1.start()
    def randomized():
        global a
        global counter
        counter=1
        a=random.randint(1,14)
        win6.destroy()
        import starting
        starting.runM()
    tkinter.Button(text="Randomly\nGenerated",command=randomized,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=15,height=2,cursor="hand2").place(x=110,y=90)
    def selected():
        global a
        global counter
        counter=0
        if drop.get()=="Pb+2":
            a=1
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Cu+2":
            a=2
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="As+2":
            a=3
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Fe+3":
            a=4
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Al+3":
            a=5
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Zn+2":
            a=6
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Co+2":
            a=7
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Ni+2":
            a=8
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Mn+2":
            a=9
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Ba+2":
            a=10
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Sr+2":
            a=11
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Ca+2":
            a=12
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="Mg+2":
            a=13
            print(a)
            win6.destroy()
            import starting
            starting.runM()
        if drop.get()=="NH4+":
            a=14
            print(a)
            win6.destroy()
            import starting
            starting.runM()
    def back():
        import main
        win6.destroy()

        main.frun()
    tkinter.Label(text="OR",bg="#46A0EC", fg="white",font="Titilium 20 bold",cursor="hand2").place(x=220,y=190)
    setter= StringVar()
    setter.set("Choose a Cation")
    drop =ttk.Combobox(win6,textvariable=setter,font="Calibri 20 bold",justify="center",width=25)
    drop['values']=["Pb+2","Cu+2","As+2","Fe+3","Al+3","Zn+2","Co+2","Ni+2","Mn+2","Ba+2","Sr+2","Ca+2","Mg+2","NH4+"]
    drop['state']='readonly'
    drop.place(y=240,x=65)
    tkinter.Button(text="Select Cation",command=selected,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=15,height=2,cursor="hand2").place(y=300,x=110)
    backimg=PhotoImage(file="back.png")
    backbutton=tkinter.Button(win6,image=backimg,bg="#46A0EC",command=back)
    backbutton.place(x=15,y=15)
    win6.mainloop()