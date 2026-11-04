import tkinter
from tkinter import *
import pyttsx3 as sound
import threading
global tosay
tosay=sound.init()
tosay.setProperty('rate', 190)
voice = tosay.getProperty('voices')
tosay.setProperty('voice', voice[1].id)
def sayline(a):
    tosay.say(a)
    tosay.runAndWait()
def thread1():
    global tosay
    sayline("Welcome to ChemSim")
    tosay.runAndWait()
win30=Tk()
win30.geometry("500x500+500+150")
win30.title("ChemSim")
def start():
    win30.destroy()
    import Services.ConsoleDB as ConsoleDB
    ConsoleDB.mainLogin()
def tostart(e):
    start()
def mutesound():
    pass
    global tosay
    tosay=""
chemism=PhotoImage(file="My project-1.png")
tkinter.Label(win30,image=chemism).place(x=0,y=0)
chemistry=PhotoImage(file="chemistry button1.png")
tkinter.Button(command=start,image=chemistry,bg="#E4F0FE",borderwidth=0).place(x=170,y=250)
win30.resizable(0,0)
win30.bind("<Return>",tostart)
t1 = threading.Thread(target=thread1)
t1.start()
#mute=tkinter.Button(bg="#46A0EC",fg="white",text="Mute",font="Calibri 10 bold",command=mutesound)
#mute.place(x=15,y=15)
win30.mainloop()
