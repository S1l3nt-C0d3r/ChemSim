import tkinter
import pandas as p
from tkinter import *
from tkinter import messagebox
import pyttsx3 as sound
import threading
import speech_recognition as sr
r = sr.Recognizer()
import time
import multiprocessing
global tosay
sp=""
tosay=sound.init()
global s_off
s_off=True
def listen():
        with sr.Microphone() as source:
            audio_text = r.listen(source,10,3)
            sp=r.recognize_google(audio_text)
            atomic.insert(0,sp)
def thread1():
    global tosay

    tosay.say("Welcome to Infomania")
    tosay.runAndWait()
    tosay.say("Please Enter or say the Atomic Number for the Element")
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()



def thread2():
    global tosay
    t2 = "Displaying information about", str(threading.current_thread().getName())
    tosay.say(t2)
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()
df=p.read_csv("elementsf.csv",encoding='utf-8')

atno=list(df.loc[:,'AtNo'])
name=list(df.loc[:,'Name'])
sym=list(df.loc[:,'Symbol'])
massno=list(df.loc[:,'MassNo'])
block=list(df.loc[:,'Block'])
his=list(df.loc[:,'History'])
ori=list(df.loc[:,'Origin'])
use=list(df.loc[:,'Uses'])
win26=Tk()
win26.geometry("500x500+500+150")
win26.title("Infomania")
img4=PhotoImage(file="infomania bg.png")
img2=PhotoImage(file="infomania.png")
tkinter.Label(win26,image=img4).pack()
mainscreen = tkinter.Label(win26,image=img2,bg="#f1c40f",font="Calibri 13 bold")
mainscreen.place(x=105,y=30)
global stop_threads
stop_threads = False
t1 = threading.Thread(target=thread1)
t1.start()
txt1="Please Enter the Atomic Number for the Element"
tkinter.Label(text=txt1,bg="#FFC658",font="Calibri 15 bold").place(x=50,y=350)

atomic=tkinter.Entry(width=30,borderwidth=5,justify='center',font="none 13 bold")
print(sp)
atomic.place(x=110,y=390)

def elementinfo():
    global stop_threads, tosay
    stop_threads=True
    if tosay.isBusy():
        print(tosay.isBusy())
        tosay.stop()
    a = atomic.get()
    if a.isalpha():
        messagebox.showinfo("Invalid Input","Please Enter or Say a Number Only.")
    a=int(a)
    win26.destroy()
    win27=Tk()
    win27.title("Infomania")
    win27.geometry("1500x880+10+0")
    win27.configure(background="#f1c40f")
    if (a > 118) and (a not in atno):
        tkinter.Label(text="Element Does Not Exist", bg="#f1c40", font="Calibri 30 bold").pack(pady=150)
    elif (a not in atno):
        tkinter.Label(text="No information found", bg="#f1c40f", font="Calibri 30 bold").pack(pady=150)
    else:
        a = atno.index(a)
        sb=tkinter.Scrollbar(win27)
        sb.pack(side="right",fill="y")
        t=tkinter.Text(win27,bg="#f1c40f",font="Calibri 20 bold",yscrollcommand=sb.set,width=1450,height=900,wrap=WORD)
        t.insert(tkinter.END,( "Name: "+ name[a].title()+"\n"+"Symbol: "+ sym[a].title()+"\n"+"Mass Number: "+ massno[a].replace('lauremipsum','')+"\n"+ "Block: "+ block[a].upper()+"\n"+"\nHistory:"+"\n"+his[a].replace('.lauremipsum', '\n')+"\n"+"Origin: "+"\n"+ori[a].replace('.lauremipsum', '\n')+"\n"+"Uses:"+"\n"+use[a].replace('lauremipsum', '\n')))
        t.tag_config("center",justify="center")
        t.tag_add("center",1.0,"end")
        t.config(state="disabled")
        t.pack()
        sb.config(command= t.yview)
        t2 = threading.Thread(target=thread2, name=name[a])
        t2.start()

        #tkinter.Label(text=("Atomic Number:  "+str(atno[a])),bg,yscrollcommand=sb.set="#f1c40f",font="Calibri 30 bold").pack(anchor="c")
        #tkinter.Label(text=("Name: "+ name[a].title()),bg="#f1c,yscrollcommand=sb.set40f",font="Calibri 20 bold").pack(anchor="c")
        #tkinter.Label(text=("Symbol: "+ sym[a].title()),bg="#f1,yscrollcommand=sb.setc40f",font="Calibri 20 bold").pack(anchor="c")
        #tkinter.Label(text=("Mass Number: "+ massno[a].replace(,yscrollcommand=sb.set'lauremipsum','')),bg="#f1c40f",font="Calibri 20 bold").pack(anchor="c")
        #tkinter.Label(text=("Block: "+ block[a].upper()),bg="#f,yscrollcommand=sb.set1c40f",font="Calibri 20 bold").pack(anchor="c")
        #tkinter.Label(text=("\nHistory:"), bg="#f1c40f",font="C,yscrollcommand=sb.setalibri 15 bold",justify="center",wraplength=1400).pack(anchor="c",padx=10)
        #tkinter.Label(text=(his[a].replace('.lauremipsum', '\n',yscrollcommand=sb.set)),bg="#f1c40f",font="Calibri 15",justify="center",wraplength=1400).pack(anchor="c",padx=10)
        #tkinter.Label(text=("\nOrigin: "), bg="#f1c40f",font="C,yscrollcommand=sb.setalibri 15 bold",justify="center",wraplength=1400).pack(anchor="c",padx=10)
        #tkinter.Label(text=(ori[a].replace('.lauremipsum', '\n',yscrollcommand=sb.set)),bg="#f1c40f",font="Calibri 15",justify="center",wraplength=1400).pack(anchor="c",padx=10)
        #tkinter.Label(text=("Uses:"), bg="#f1c40f",font="Calibr,yscrollcommand=sb.seti 15 bold",justify="center",wraplength=1400).pack(anchor="c",pady=10)
        #tkinter.Label(text=(use[a].replace('lauremipsum', '\n'),yscrollcommand=sb.set),bg="#f1c40f",font="Calibri 15",justify="center",wraplength=1400).pack(anchor="c")
img6=PhotoImage(file="search button.png")
tkinter.Button(text="Search",command=elementinfo,image=img6,borderwidth=0,background="black").place(x=150,y=430)
ag = PhotoImage(file="mic.png")
voice = Button(
    win26,
    bg="#f1c40f",
    cursor="hand2",
    image=ag,
    command=listen,
    state=NORMAL
)
voice.place(x=400,y=389.3)
win26.mainloop()
