import tkinter
from tkinter import *
from src.Virtual_Lab.Anions.Br import Br
from src.Virtual_Lab.Anions.C2O42 import C2O42
from src.Virtual_Lab.Anions.CH3COO import CH3COO
from src.Virtual_Lab.Anions.Cl import Cl
from src.Virtual_Lab.Anions.I import I
from src.Virtual_Lab.Anions.NO2 import NO2
from src.Virtual_Lab.Anions.NO3 import NO3
from src.Virtual_Lab.Anions.PO43 import PO43
from src.Virtual_Lab.Anions.S2 import S2
from SO32 import SO32
from src.Virtual_Lab.Anions.CO32 import CO32
from SO42 import SO42
import pyttsx3 as sound
import threading
global tosay
tosay=sound.init()
from src.Virtual_Lab.Anions.anion import anion
import random as r
global a
import src.Virtual_Lab.Anions.SelecterscreenAnion as s
a=s.a
print(a)
if a==1:     obj=Br()
elif (a==2): obj=C2O42()
elif (a==3): obj=CH3COO()
elif (a==4): obj=I()
elif (a==5): obj=PO43()
elif (a==6): obj=NO2()
elif (a==7): obj=S2()
elif (a==8): obj=SO32()
elif (a==9): obj=SO42()
elif (a==10): obj=Cl()
elif (a==11): obj=NO3()
elif (a==12): obj=CO32()
def thread1(a):
    global tosay
    if tosay._inLoop:
        tosay.endLoop()
    q = a
    tosay.say(q)
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()

win16 = Tk()
win16.geometry("500x500+500+150")
win16.configure(background="#46A0EC")
win16.resizable(0,0)
label1=tkinter.Label(text="Welcome to this Virtual Lab",bg="#46A0EC",fg="white",font="Titillium  20 bold")
label1.place(x=70,y=10)
label2=tkinter.Label(text="You have been given a salt. You have to identify the anion present in it",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label2.place(x=20,y=50)
t1 = threading.Thread(target=thread1,args=("You have been given a salt. You have to identify the anion present in it",))
t1.start()
label3=tkinter.Label(text="Would you like to perform elementary test or confirmatory test?",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label3.place(x=50,y=70)
def confirmatory():
    win16.destroy()
    import src.Virtual_Lab.Anions.confirmanion as confirmanion
def action():
    win16.destroy()
    win17 = Tk()
    win17.geometry("500x600+500+150")
    win17.configure(background="#46A0EC")
    win17.title("Elementary Test")
    win17.resizable(0, 0)
    def dilH2SO4():
        yc["state"]="disabled"
        tkinter.Label(text=(obj.dilsul),bg="#46A0EC",fg="white",font="Calibri 20 bold",wraplength=400).pack()
        t1 = threading.Thread(target=thread1,
                              args=(obj.dilsul,))
        t1.start()
    def concH2SO4():
        yd["state"]="disabled"
        tkinter.Label(text=(obj.concsul),bg="#46A0EC",fg="white",font="Calibri 20 bold",wraplength=400).pack()

        t1 = threading.Thread(target=thread1,
                          args=(obj.concsul,))
        t1.start()
    def shift():
        win17.destroy()
        import startanion1
    tkinter.Label(text="Please choose one test",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=(30,10))
    t1 = threading.Thread(target=thread1,
                          args=("Please choose one test",))
    t1.start()
    yc= tkinter.Button(text="dil H2SO4",command=dilH2SO4,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=10,height=2,cursor="hand2")
    yc.pack(pady=10)
    yd= tkinter.Button(text="conc. H2SO4",command=concH2SO4,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=10,height=2,cursor="hand2")
    yd.pack(pady=10)
    ye=tkinter.Button(text="Back",command=shift,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=10,height=2,cursor="hand2")
    ye.pack(pady=10)

Dry= tkinter.Button(text="Elementary Test",command=action,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=20,height=2,cursor="hand2")
Dry.place(x=75,y=130)
Wet= tkinter.Button(text="Confirmatory Test",command=confirmatory,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=20,height=2,cursor="hand2")
Wet.place(x=75,y=250)
win16.title("Virtual Lab ----> Anion")
win16.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        