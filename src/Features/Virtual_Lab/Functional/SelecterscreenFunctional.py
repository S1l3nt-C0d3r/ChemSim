import tkinter
from tkinter import ttk
from tkinter import *
import random
import pyttsx3 as sound
import threading
win6=Tk()
win6.geometry("500x500+500+150")
win6.resizable(0,0)
global img1
img1=PhotoImage(file="virtual lab background.png")
tkinter.Label(win6,image=img1).pack()
def randomized():
    global a
    a=random.randint(1,6)
    win6.destroy()
    import startfunctional
tkinter.Button(text="Randomly\nGenerated",command=randomized,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=15,height=2,cursor="hand2").place(x=110,y=90)


global tosay
tosay=sound.init()
def thread1():
    global tosay
    if tosay._inLoop:
        tosay.endLoop()
    tosay.say("Choose a Functional Group or click generate test Randomly")
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()
t1 = threading.Thread(target=thread1)
t1.start()
def selected():
    global a
    if drop.get()=="Carboxylic Acid":
        a=1
        print(a)
        win6.destroy()
        import startfunctional
    if drop.get()=="Phenol":
        a=2
        print(a)
        win6.destroy()
        import startfunctional
    if drop.get()=="Aldehyde":
        a=3
        print(a)
        win6.destroy()
        import startfunctional
    if drop.get()=="Ketone":
        a=4
        print(a)
        win6.destroy()
        import startfunctional
    if drop.get()=="Amine":
        a=5
        print(a)
        win6.destroy()
        import startfunctional
    if drop.get()=="Alcohol":
        a=6
        print(a)
        win6.destroy()
        import startfunctional
tkinter.Label(text="OR",bg="#46A0EC", fg="white",font="Titilium 20 bold",cursor="hand2").place(x=220,y=190)
setter= StringVar()
setter.set("Choose a Functional Group")
drop =ttk.Combobox(win6,textvariable=setter,font="Calibri 20 bold",justify="center",width=25)
drop['values']=["Carboxylic Acid","Phenol","Aldehyde","Ketone","Amine","Alcohol"]
drop['state']='readonly'
drop.place(y=240,x=65)
tkinter.Button(text="Select\nFunctional Group",command=selected,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=15,height=2,cursor="hand2").place(y=300,x=110)


def back():
    import main
    win6.destroy()
    main.frun()
backimg = PhotoImage(file="back.png")
backbutton = tkinter.Button(win6, image=backimg, bg="#46A0EC", command=back)
backbutton.place(x=15, y=15)
win6.mainloop()