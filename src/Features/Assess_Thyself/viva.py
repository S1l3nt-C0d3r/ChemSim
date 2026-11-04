import tkinter
from tkinter import *
import pyttsx3
import pandas
import random as r
from tkinter import messagebox

import Assess_Thyself.viva as viva

win91=Tk()
bgimg=PhotoImage(file="vivabg.png")
win91.geometry("500x500+500+150")
win91.resizable(0,0)
tkinter.Label(win91,image=bgimg).pack()
df=pandas.read_csv("vivaquestions.csv",encoding="utf-8")
Sr=list(df.loc[:,'Sr.'])
a=r.randrange(0,len(Sr))
ques=list(df.loc[:,'Questions'])
c1=  list(df.loc[:,'Canswer'])[a]
w1=  list(df.loc[:,'W1'])[a]
w2=  list(df.loc[:,'W2'])[a]
w3=  list(df.loc[:,'W3'])[a]
global changer
def correct():
    messagebox.showinfo("Correct!","That's Correct! Very Good!")
    changer=1
    print(changer)
    a = r.randrange(0, len(Sr))
    ques = list(df.loc[:, 'Questions'])
    c1 = list(df.loc[:, 'Canswer'])[a]
    w1 = list(df.loc[:, 'W1'])[a]
    w2 = list(df.loc[:, 'W2'])[a]
    w3 = list(df.loc[:, 'W3'])[a]
    viva.A1.destroy()
    viva.A2.destroy()
    viva.A3.destroy()
    viva.A4.destroy()
    A1 = Button(
        text=c1,
        width=18,
        height=3,
        fg="#000000",
        bg="#E8EDFF",
        pady=1,
        command=correct,
        wraplength=200,
        justify="center",
        font=("Arial bold", 15),
    )
    A2 = Button(
        text=w1,
        width=18,
        height=3,
        fg="#000000",
        bg="#E8EDFF",
        command=wrong,
        wraplength=200,
        justify="center",
        pady=1,
        font=("Arial bold", 15),
    )
    A3 = Button(
        text=w2,
        width=18,
        height=3,
        fg="#000000",
        bg="#E8EDFF",
        command=wrong,
        wraplength=200,
        justify="center",
        pady=1,
        font=("Arial bold", 15),
    )
    A4 = Button(
        text=w3,
        width=18,
        height=3,
        fg="#000000",
        bg="#E8EDFF",
        command=wrong,
        wraplength=200,
        justify="center",
        pady=1,
        font=("Arial bold", 15),
    )
    xy = [(10,230),(260,230),(10,370),(260,370)]
    rnum = r.randrange(0, len(xy))
    x, y = xy[rnum]
    A1.place(x=x, y=y)
    xy.pop(rnum)
    rnum = r.randrange(0, len(xy))
    x, y = xy[rnum]
    A2.place(x=x, y=y)
    xy.pop(rnum)
    rnum = r.randrange(0, len(xy))
    x, y = xy[rnum]
    A3.place(x=x, y=y)
    xy.pop(rnum)
    x, y = xy[0]
    A4.place(x=x, y=y)
    t.config(state="normal")
    t.delete("1.0",END)
    t.insert(END,ques[a])
    t.tag_config("center", justify="center")
    t.tag_add("center", 1.0, "end")
    t.config(state="disabled")
    print(t)

def wrong():
    messagebox.showinfo("Wrong","Wrong Answer... Keep Trying!")
A1 = Button(
    text=c1,
    width=18,
    height=3,
    fg="#000000",
    bg="#E8EDFF",
    pady=1,
    command=correct,
    wraplength=200,
    justify="center",
    font=("Arial bold", 15),
)
A2 = Button(
    text=w1,
    width=18,
    height=3,
    fg="#000000",
    bg="#E8EDFF",
    command=wrong,
    wraplength=200,
    justify="center",
    pady=1,
    font=("Arial bold", 15),
)
A3 = Button(
    text=w2,
    width=18,
    height=3,
    fg="#000000",
    bg="#E8EDFF",
    command=wrong,
    wraplength=200,
    justify="center",
    pady=1,
    font=("Arial bold", 15),
)
A4 = Button(
    text=w3,
    width=18,
    height=3,
    fg="#000000",
    bg="#E8EDFF",
    command=wrong,
    wraplength=200,
    justify="center",
    pady=1,
    font=("Arial bold", 15),
)
xy=[(10,230),(260,230),(10,370),(260,370)]
rnum=r.randrange(0,len(xy))
x,y=xy[rnum]
A1.place(x=x,y=y)
xy.pop(rnum)
rnum=r.randrange(0,len(xy))
x,y=xy[rnum]
A2.place(x=x,y=y)
xy.pop(rnum)
rnum=r.randrange(0,len(xy))
x,y=xy[rnum]
A3.place(x=x,y=y)
xy.pop(rnum)
x,y=xy[0]
A4.place(x=x,y=y)
sb=tkinter.Scrollbar(win91)
sb.pack(side="right",fill="y")
t=tkinter.Text(win91,bg="#E8EDFF",font="Calibri 20 bold",yscrollcommand=sb.set,width=30,height=5,wrap=WORD)
t.insert(tkinter.END,ques[a])
t.tag_config("center",justify="center")
t.tag_add("center",1.0,"end")
t.config(state="disabled")
t.place(x=40,y=10)
sb.config(command= t.yview)