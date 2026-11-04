import tkinter
from tkinter import ttk
from tkinter import *
import random
import pyttsx3 as sound
import threading
global tosay
win6=Tk()
win6.geometry("500x500+500+150")
tosay=sound.init()
win6.resizable(0,0)
global img1
img1=PhotoImage(file="virtual lab background.png")
tkinter.Label(win6,image=img1).pack()
def randomized():
    global a
    a=random.randint(1,12)
    win6.destroy()
    import startanion
def thread1():
    global tosay
    if tosay._inLoop:
        tosay.endLoop()
    tosay.say("Please choose an anion or press randomly generate")
    tosay.runAndWait()

t1 = threading.Thread(target=thread1)
t1.start()
tkinter.Button(text="Randomly\nGenerated",command=randomized,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=15,height=2,cursor="hand2").place(x=110,y=90)
def selected():
    global a
    if drop.get()=="Br-":
        a=1
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(C2O4)-2":
        a=2
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="CH3COO-":
        a=3
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="I-":
        a=4
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(PO4)-3":
        a=5
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(NO2)-":
        a=6
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(S)-2":
        a=7
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(SO3)-2":
        a=8
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(SO4)-2":
        a=9
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="Cl-":
        a=10
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(NO3)-":
        a=11
        print(a)
        win6.destroy()
        import startanion
    if drop.get()=="(CO3)-2":
        a=12
        print(a)
        win6.destroy()
        import startanion
tkinter.Label(text="OR",bg="#46A0EC", fg="white",font="Titilium 20 bold",cursor="hand2").place(x=220,y=190)
setter= StringVar()
setter.set("Choose an Anion")
drop =ttk.Combobox(win6,textvariable=setter,font="Calibri 20 bold",justify="center",width=25)
drop['values']=["Br-","(C2O4)-2","CH3COO-","I-","(PO4)-3","(NO2)-","(S)-2","(SO3)-2","(SO4)-2","Cl-","(NO3)-","(CO3)-2"]
drop['state']='readonly'
drop.place(y=240,x=65)
tkinter.Button(text="Select Anion",command=selected,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=15,height=2,cursor="hand2").place(y=300,x=110)
def back():
    import main
    win6.destroy()
    main.frun()
backimg = PhotoImage(file="back.png")
backbutton = tkinter.Button(win6, image=backimg, bg="#46A0EC", command=back)
backbutton.place(x=15, y=15)
win6.mainloop()