import tkinter
from tkinter import *
from src.Virtual_Lab.Functional.allclasses import ketone
from src.Virtual_Lab.Functional.allclasses import phenol
from src.Virtual_Lab.Functional.allclasses import COOH
from src.Virtual_Lab.Functional.allclasses import CHO
from src.Virtual_Lab.Functional.allclasses import amine
from src.Virtual_Lab.Functional.allclasses import OH
import random as r
import pyttsx3 as sound
import threading
global tosay
tosay=sound.init()
global a
import src.Virtual_Lab.Functional.SelecterscreenFunctional as s
a=s.a
print(a)
if a == 1:
    obj = COOH()
elif (a == 2):
    obj = phenol()
elif (a == 3):
    obj = CHO()
elif (a == 4):
    obj = ketone()
elif (a == 5):
    obj = amine()
elif (a == 6):
    obj = OH()
# elif (a==6): obj=acid()
# elif (a==7): obj=ether() #check
# elif (a==8): obj=alcohol()
def thread1(a):
    global tosay
    if tosay._inLoop:
        tosay.endLoop()
    q = a
    tosay.say(q)
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()

win21=Tk()
win21.geometry("500x500+500+150")
win21.configure(background="#46A0EC")
win21.resizable(0,0)
win21.title("Virtual Lab ----> Functional Group")
label1=tkinter.Label(text="Welcome to this Virtual Lab",bg="#46A0EC",fg="white",font="Titillium  20 bold")
label1.place(x=70,y=10)
label2=tkinter.Label(text=" You have been given an Organic Compound\n You have to identify the Functional Group present in it",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label2.place(x=75,y=50)

t1 = threading.Thread(target=thread1,
                      args=("You have been given an Organic Compound. You have to identify the Functional Group present in it",))
t1.start()
label3=tkinter.Label(text="Would you like to perform unsaturated test or confirmatory test?",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label3.place(x=50,y=90)
t1 = threading.Thread(target=thread1,
                      args=("Would you like to perform unsaturated test or confirmatory test?",))
t1.start()
def Unsatu():
    win21.destroy()
    win22 = Tk()
    win22.geometry("500x500+500+150")
    win22.configure(background="#46A0EC")
    win22.title("Test for Unsaturation")
    win22.resizable(0, 0)
    tkinter.Label(text="Please choose a test",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=(30,10))
    t1 = threading.Thread(target=thread1,
                          args=("Please choose one test",))
    t1.start()

    def Bromine():
        tkinter.Label(text="Brown color decolorises",bg="#46A0EC",fg="white",font="Calibri 15 bold").pack(pady=(10,0))
        t1 = threading.Thread(target=thread1,
                              args=("Brown color decolorises",))
        t1.start()
        yd["state"]="disabled"
    def KMnO4():
        tkinter.Label(text="Pink color Decolorises",bg="#46A0EC",fg="white",font="Calibri 15 bold").pack(pady=(10,0))
        t1 = threading.Thread(target=thread1,
                              args=("Pink color Decolorises",))
        t1.start()
        yc["state"]="disabled"

        global img1
        img1=PhotoImage(file="Bromine water.png")
        tkinter.Label(image=img1).pack(pady=10)
        win22.geometry("500x700")
    def shift1():
        win22.destroy()
        import startfunctional1

    yc = tkinter.Button(text="dil KMnO4", command=KMnO4, bg="#46A0EC", fg="white", font="Titilium 20 bold", width=15,height=2,cursor="hand2")
    yc.pack(pady=10)
    yd = tkinter.Button(text="Bromine water", command=Bromine, bg="#46A0EC", fg="white", font="Titilium 20 bold",width=15, height=2,cursor="hand2")
    yd.pack(pady=10)
    ye = tkinter.Button(text="Back", command=shift1, bg="#46A0EC", fg="white", font="Titilium 20 bold", width=10,height=2,cursor="hand2")
    ye.pack(pady=10)
Dry= tkinter.Button(text="Unsaturated Test",command=Unsatu,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=20,height=2,cursor="hand2")
Dry.place(x=75,y=150)
def confirmatory4():
    win21.destroy()
    import functionalconfirm

Wet= tkinter.Button(text="Confirmatory Test",command=confirmatory4,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=20,height=2,cursor="hand2")
Wet.place(x=75,y=270)
win21.mainloop()