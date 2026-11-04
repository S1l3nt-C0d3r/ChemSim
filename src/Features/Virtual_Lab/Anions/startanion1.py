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
from src.Virtual_Lab.Anions.anion import anion
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
win18 = Tk()
win18.geometry("500x500+500+150")
win18.configure(background="#46A0EC")
win18.resizable(0,0)
def confirmatory():
    win18.destroy()
    import src.Virtual_Lab.Anions.confirmanion as confirmanion
label1=tkinter.Label(text="Welcome to this Virtual Lab",bg="#46A0EC",fg="white",font="Titillium  20 bold")
label1.place(x=70,y=10)
label2=tkinter.Label(text="You have been given a salt. You have to identify the cation present in it",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label2.place(x=15,y=70)
label3=tkinter.Label(text="Please Perform Confirmatory Test",bg="#46A0EC",fg="white",font="Titillium  10 bold")
label3.place(x=140,y=110)
Wet= tkinter.Button(text="Confirmatory Test",command=confirmatory,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=20,height=3,cursor="hand2")
Wet.place(x=75,y=200)
win18.title("Virtual Lab ----> Anion")
win18.mainloop()
