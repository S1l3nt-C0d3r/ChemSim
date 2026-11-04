from tkinter import *
import tkinter

def s1run():
    from src.Virtual_Lab.Cations.Cu import Cu
    from src.Virtual_Lab.Cations.Pb import Pb
    from src.Virtual_Lab.Cations.As import As
    from src.Virtual_Lab.Cations.Fe import Fe
    from src.Virtual_Lab.Cations.Al import Al
    from src.Virtual_Lab.Cations.Zn import Zn
    from src.Virtual_Lab.Cations.Ni import Ni
    from src.Virtual_Lab.Cations.Co import Co
    from src.Virtual_Lab.Cations.Mn import Mn
    from src.Virtual_Lab.Cations.Ba import Ba
    from src.Virtual_Lab.Cations.Sr import Sr
    from src.Virtual_Lab.Cations.Ca import Ca
    from src.Virtual_Lab.Cations.NH4 import NH4
    from src.Virtual_Lab.Cations.Mg import Mg
    import random as r
    from sys import exit
    global a
    from starting import a
    if a == 1:
        obj = Pb()
    elif (a == 2):
        obj = Cu()
    elif (a == 3):
        obj = As()
    elif (a == 4):
        obj = Fe()
    elif (a == 5):
        obj = Al()
    elif (a == 6):
        obj = Zn()
    elif (a == 7):
        obj = Co()
    elif (a == 8):
        obj = Ni()
    elif (a == 9):
        obj = Mn()
    elif (a == 10):
        obj = Ba()
    elif (a == 11):
        obj = Sr()
    elif (a == 12):
        obj = Ca()
    elif (a == 13):
        obj = Mg()
    elif (a == 14):
        obj = NH4()
    win15 = Tk()


    def WetTest4():
        win15.destroy()
        import src.Virtual_Lab.Cations.ppt as ppt
        ppt.pptrun()
    virtualbackground = PhotoImage(file="virtual lab background.png")
    tkinter.Label(win15,image=virtualbackground).pack()
    label1=tkinter.Label(text="Welcome to this Virtual Lab",bg="#46A0EC",fg="white",font="Titillium  20 bold")
    label1.place(x=70,y=10)
    label2=tkinter.Label(text="You have been given a salt. You have to identify the cation present in it",bg="#46A0EC",fg="white",font="Titillium  10 bold")
    label2.place(x=15,y=70)
    label3=tkinter.Label(text="Please perform wet test",bg="#46A0EC",fg="white",font="Titillium  10 bold")
    label3.place(x=167,y=110)
    Wet= tkinter.Button(text="Wet Test",command=WetTest4,bg="#46A0EC",fg="white",height=3,width=15,font="Titilium 20 bold",cursor="hand2")
    Wet.place(x=115,y=200)
    win15.geometry("500x500+500+150")
    win15.resizable(0,0)
    win15.title("Virtual Lab ----> Cation")
    win15.mainloop()
