import tkinter
from tkinter import *
from tkinter import messagebox
from src.Virtual_Lab.Functional.allclasses import ketone
from src.Virtual_Lab.Functional.allclasses import phenol
from src.Virtual_Lab.Functional.allclasses import COOH
from src.Virtual_Lab.Functional.allclasses import CHO
from src.Virtual_Lab.Functional.allclasses import amine
from src.Virtual_Lab.Functional.allclasses import OH
import random as r
import threading
import pyttsx3 as sound
global tosay
tosay=sound.init()
def thread1():
    global tosay
    tosay.say("Congratulations")
    tosay.runAndWait()
global a
from startfunctional import a
win25 = Tk()
win25.geometry("500x500+500+150")
win25.configure(background="#46A0EC")
win25.resizable(0,0)
win25.title("Guess the Functional Group")
tkinter.Label(text="Guess the Functional Group",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=30)
yt=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
yt.pack(pady=10)
t1 = threading.Thread(target=thread1)
def functionguessy():
    if a==1:
        if(yt.get()=="COOH" or yt.get().lower()=="carboxylic acid"):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            op1["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong answer\nTry again :)")
    if a==2:
        if(yt.get().lower()=="phenol" or yt.get()=="Phenol"):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            op1["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong answer\nTry again :)")
    if a==3:
        if(yt.get()=="CHO" or yt.get().lower()=="aldehyde"):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            op1["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong answer\nTry again :)")
    if a==4:
        if(yt.get().lower()=="ketone" or yt.get()=="Ketone"):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            op1["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong answer\nTry again :)")
    if a==5:
        if(yt.get().lower()=="amine" or yt.get()=="Amine"):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            op1["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong answer\nTry again :)")
    if a==6:
        if(yt.get()=="OH" or yt.get().lower()=="alcohol"):
            tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            op1["state"]="disabled"
            t1.start()
        else:
            messagebox.showinfo("Wrong Answer","Wrong answer\nTry again :)")
op1=tkinter.Button(text="Guess",command=functionguessy,bg="#46A0EC",fg="white",font="Calibri 20 bold",width=10,height=1,cursor="hand2")
op1.pack()