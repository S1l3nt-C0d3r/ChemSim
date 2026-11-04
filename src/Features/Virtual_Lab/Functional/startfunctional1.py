import tkinter
from tkinter import *
import pyttsx3 as sound
import threading
import speech_recognition as sr
from src.Virtual_Lab.Functional.allclasses import ketone
from src.Virtual_Lab.Functional.allclasses import phenol
from src.Virtual_Lab.Functional.allclasses import COOH
from src.Virtual_Lab.Functional.allclasses import CHO
from src.Virtual_Lab.Functional.allclasses import amine
from src.Virtual_Lab.Functional.allclasses import OH
import random as r
win23=Tk()
win23.geometry("500x500+500+150")
win23.configure(background="#46A0EC")
win23.resizable(0,0)
global tosay
tosay=sound.init()
def confirmatory4():
    win23.destroy()
    import functionalconfirm
label1=tkinter.Label(text="Welcome to this Virtual Lab",bg="#46A0EC",fg="white",font="Titillium  20 bold")
label1.pack(pady=30)
label2=tkinter.Label(text=" You have been given an Organic Compound\n You have to identify the Functional Group present in it",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label2.pack(pady=10)

label3=tkinter.Label(text="Please Perform Confirmatory Test",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label3.pack(pady=10)
yk=tkinter.Button(text="Confirmatory Test",command=confirmatory4,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=20,height=2,cursor="hand2")
yk.pack(pady=10)
win23.title("Virtual Lab ----> Functional Group")