import tkinter
from tkinter import *
from tkinter import messagebox
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
import threading
import pyttsx3 as sound
global tosay
tosay=sound.init()
def thread1():
    global tosay
    tosay.say("Congratulations")
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()
import random as r
global a
from startanion import a
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
win20 = Tk()
win20.geometry("500x500+500+150")
win20.resizable(0,0)
win20.title("Guess the Anion")
win20.configure(background="#46A0EC")
def thread2():
    global tosay
    tosay.say("Please guess the anion")
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()
t2 = threading.Thread(target=thread2)
t2.start()
tkinter.Label(text="Guess the Anion",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=30)
yh=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
yh.pack(pady=10)
t1 = threading.Thread(target=thread1)
def guessya():
    if a==1:
        yi = yh.get()
        if (yi == "Br-" or yi.lower()=="bromide"):
            tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
            yj["state"] = "disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    if a==2:
        yi = yh.get()
        if ((yi == "(C2O4)-2") or (yi == "(C2O4)2-") or (yi.lower() == "oxalate")):
            tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
            yj["state"] = "disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    if a==3:
        yi = yh.get()
        if ((yi == "CH3COO-" or (yi.lower() == "acetate"))):
            tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
            yj["state"] = "disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    if a==4:
        yi = yh.get()
        if ((yi == "I-") or (yi.lower() == "iodide")):
            tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
            yj["state"] = "disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    elif a==5:
        yi = yh.get()
        if ((yi == "(PO4)3-") or (yi == "(PO4)-3") or (yi.lower() == "phosphate")):
            tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
            yj["state"] = "disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    elif a==6:
        yi = yh.get()
        if ((yi == "(NO2)-1") or (yi == "(NO2)-") or (yi.lower() == "nitrite")):
            tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
            yj["state"] = "disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer", "Wrong Answer\nPlease Try Again :)")
    elif a==7:
        yi=yh.get()
        if((yi=="S2-") or (yi=="S-2")or (yi.lower() == "sulphide")):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
            yj["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    elif a==8:
        yi=yh.get()
        if((yi=="(SO3)2-") or (yi=="(SO3)-2") or (yi.lower() == "sulphite")):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
            yj["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    elif a==9:
        yi=yh.get()
        if((yi=="(SO4)2-") or (yi=="(SO4)-2") or (yi.lower() == "sulphate")):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
            yj["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    elif a==10:
        yi=yh.get()
        if((yi=="Cl-") or (yi.lower() == "chloride")):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
            yj["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    elif a==11:
        yi=yh.get()
        if((yi=="NO3-") or (yi.lower() == "nitrate")):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
            yj["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
    elif a==12:
        yi=yh.get()
        if((yi=="(CO3)2-") or (yi=="(CO3)-2") or (yi.lower() == "carbonate")):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
            yj["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong Answer\nPlease Try Again :)")
yj=tkinter.Button(text="Guess",command=guessya,bg="#46A0EC",fg="white",font="Calibri 20 bold",width=20,height=2,cursor="hand2")
yj.pack(pady=10)