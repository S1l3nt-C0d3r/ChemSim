import tkinter
import pandas
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
import pyttsx3 as sound
import threading
global tosay
tosay=sound.init()
import random as r
global a
from startanion import a
if   (a==1): obj=Br()
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
win19 = Tk()
win19.geometry("500x500+500+150")
win19.resizable(0,0)
win19.configure(background="#46A0EC")
win19.title("Confirmatory Test")
yu=tkinter.Label(text="Enter action",bg="#46A0EC",fg="white",font="Calibri 20 bold")
yu.pack(pady=30)
yf=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
yf.pack(pady=10)
yg=yf.get()
def g():
    if (obj.aniontest()==True):
        win19.destroy()
        import src.Virtual_Lab.Anions.Guesseranion as Guesseranion
def Hint():
    win92 = Tk()
    win92.geometry("400x500+300+150")
    win92.configure(bg="#46A0EC")
    win92.resizable(0, 0)
    win92.title("Hint")
    df = pandas.read_csv("Anion Hints.csv", encoding="utf-8")
    catno = list(df.loc[:, "Sr."])
    catgtest = list(df.loc[:, "Anion"])
    cattest = list(df.loc[:, "Ctest"])
    adtest=list(df.loc[:,"AddTest"])
    b = catno.index(a)
    tkinter.Label(win92, text=catgtest[b] + ":"+"\n" + cattest[b],bg="#46A0EC",fg="white", font="Calibri 20 bold",wraplength=350, justify="center").pack(pady=10)
    tkinter.Label(win92, text="Additional Test:", bg="#46A0EC", fg="white", font="Calibri 20 bold", wraplength=350,
                  justify="center").pack(pady=10)
    tkinter.Label(win92, text=adtest[b], bg="#46A0EC", fg="white", font="Calibri 20 bold", wraplength=350,
                  justify="center").pack(pady=10)


def confirmatory2():
    def thread1(a):
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = a
        tosay.say(q)
        tosay.runAndWait()
        if tosay._inLoop:
            tosay.endLoop()

    global yg
    yg=yf.get()
    if a==1:
        if((obj.aniontest()==True) and (obj.HNO3(yg)==True)):
            tkinter.Label(text="Pale Yellow ppt partly soluble in NH4OH",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Pale Yellow precipitate partly soluble in ammoninum hydroxide",))
            t1.start()
            op["state"]="normal"
            kh["state"]="disabled"
        elif ((obj.aniontest() == True) and (obj.ClWater(yg) == True)):
                yf.destroy()
                kh.destroy()
                yu.destroy()
                jk = tkinter.Label(text="Please shake the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                jk.pack(pady=30)
                t1 = threading.Thread(target=thread1,
                                      args=("Please shake the solution",))
                t1.start()
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack()
                bn = xy.get()
                def wettest2():
                    bn = xy.get()
                    if ("shake" in bn) == True:
                        tkinter.Label(text="Orange Colour in CS2 Layer", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                        t1 = threading.Thread(target=thread1,
                                              args=("Orange Colour in carbon disulphide Layer",))
                        t1.start()
                        op["state"] = "normal"
                        jl["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change", "No change observed")
                jl=tkinter.Button(text="Perform",command=wettest2,bg="#46A0EC",fg="white",font="Calibri 20 bold",width=10,height=1,cursor="hand2")
                jl.pack(pady=10)
        else:
            messagebox.showinfo("No Change","No change observed")
            print("GH")
    elif a==2:
        if ((obj.aniontest()==True) and (obj.CaCl2(yg)==True)):
            tkinter.Label(text="White PPT Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("White precipitate Observed",))
            t1.start()
            op["state"]="normal"
            kh["state"] = "disabled"
        elif((obj.aniontest())==True and (obj.KMnO4(yg)==True)):
            tkinter.Label(text="Pink Colour is Discharged",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Pink Colour is Discharged",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        else:
            messagebox.showinfo("No Change","No change observed")
    elif a==3:
        if ((obj.aniontest() == True) and (obj.ester(yg) == True)):
            yf.destroy()
            kh.destroy()
            yu.destroy()
            jk = tkinter.Label(text="Please heat the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1,
                                  args=("Please heat the solution",))
            t1.start()
            jk.pack(pady=30)
            xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            xy.pack()
            bn = xy.get()
            def wettest2():
                bn = xy.get()
                if ("heat" in bn) == True:
                    tkinter.Label(text="Fruity smell detected", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                    t1 = threading.Thread(target=thread1,
                                          args=("Fruity smell detected",))
                    t1.start()
                    op["state"] = "normal"
                    jl["state"] = "disabled"
                else:
                    messagebox.showinfo("No change", "No change observed")

            jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",width=10, height=1, cursor="hand2")
            jl.pack(pady=10)

        elif ((obj.aniontest() == True) and (obj.oxalic(yg) == True)):
            yf.destroy()
            kh.destroy()
            yu.destroy()
            jk = tkinter.Label(text="Please rub the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1,
                                  args=("Please rub the solution",))
            t1.start()
            jk.pack(pady=30)
            xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            xy.pack()
            bn = xy.get()

            def wettest2():
                bn = xy.get()
                if ("rub" in bn) == True:
                    tkinter.Label(text="Smell of Vinegar detected", bg="#46A0EC", fg="white",
                                  font="Calibri 20 bold").pack(pady=10)
                    t1 = threading.Thread(target=thread1,
                                          args=("Smell of Vinegar detected",))
                    t1.start()
                    op["state"] = "normal"
                    jl["state"] = "disabled"
                else:
                    messagebox.showinfo("No change", "No change observed")

            jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",
                                width=10, height=1, cursor="hand2")
            jl.pack(pady=10)
        else:
            messagebox.showinfo("No Change", "No change observed")
            print("GH")
    elif a==4:
            if ((obj.aniontest() == True) and (obj.HNO3(yg) == True)):
                tkinter.Label(text="Pale Yellow PPT Insoluble in NH4OH", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                t1 = threading.Thread(target=thread1,
                                      args=("Pale Yellow precipitate Insoluble in ammonium hydroxide",))
                t1.start()
                op["state"] = "normal"
                kh["state"] = "disabled"
            elif ((obj.aniontest() == True) and (obj.ClWater(yg) == True)):
                yf.destroy()
                kh.destroy()
                yu.destroy()
                jk = tkinter.Label(text="Please shake the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                jk.pack(pady=30)
                t1 = threading.Thread(target=thread1,
                                      args=("Please shake the solution",))
                t1.start()
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack()
                bn = xy.get()
                def wettest2():
                    bn = xy.get()
                    if ("shake" in bn) == True:
                        tkinter.Label(text="Violet Colour in CS2 Layer", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                        t1 = threading.Thread(target=thread1,
                                              args=("Violet Colour in carbon disulphide Layer",))
                        t1.start()
                        op["state"] = "normal"
                        jl["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change", "No change observed")
                jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",width=10, height=1, cursor="hand2")
                jl.pack(pady=10)
            else:
                messagebox.showinfo("No Change", "No change observed")
    elif a==5:
        if ((obj.aniontest() == True) and (obj.magnesia(yg)) == True):
            tkinter.Label(text="White PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("White precipitate observed",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        elif ((obj.aniontest() == True) and (obj.ammoly(yg) == True)):
            yf.destroy()
            kh.destroy()
            yu.destroy()
            jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1,
                                  args=("Please boil the solution",))
            t1.start()
            jk.pack(pady=30)
            xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            xy.pack()
            bn = xy.get()

            def wettest2():
                bn = xy.get()
                if ("boil" in bn) == True:
                    tkinter.Label(text="Yellow PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                    t1 = threading.Thread(target=thread1,
                                          args=("Yellow precipitate observed",))
                    t1.start()
                    op["state"] = "normal"
                    jl["state"] = "disabled"
                else:
                    messagebox.showinfo("No change", "No change observed")

            jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",
                                width=10, height=1, cursor="hand2")
            jl.pack(pady=10)
        else:
            messagebox.showinfo("No Change", "No change observed")
    elif a==6:
        if ((obj.aniontest()==True) and (obj.KI(yg)==True)):
            tkinter.Label(text="Blue Colouration Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Blue Colouration Observed",))
            t1.start()
            op["state"]="normal"
            kh["state"] = "disabled"
        elif((obj.aniontest())==True and (obj.KMnO4(yg)==True)):
            tkinter.Label(text="Pink Colour Disappears",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Pink Colour Disappears",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        elif ((obj.aniontest()) == True and (obj.FeSO4(yg) == True)):
            tkinter.Label(text="Dark Brown or Black Colour Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Dark Brown or Black Colour Observed",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        else:
            messagebox.showinfo("No Change","No change observed")
    elif a==7:
        if ((obj.aniontest()==True) and (obj.acetic(yg)==True)):
            tkinter.Label(text="Black PPT",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Black precipitate observed",))
            t1.start()
            op["state"]="normal"
            kh["state"] = "disabled"
        elif((obj.aniontest())==True and (obj.Nitroprusside(yg)==True)):
            tkinter.Label(text="Violet or Purple Colourlation",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Violet or Purple Colourlation",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        elif((obj.aniontest())==True and (obj.CdCO3(yg)==True)):
            tkinter.Label(text="Yellow PPT observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Yellow precipitate observed",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        else:
            messagebox.showinfo("No Change","No change observed")
    elif a==8:
            if ((obj.aniontest() == True) and (obj.KMNO4(yg) == True)):
                tkinter.Label(text="Pink Colour Disappears", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                t1 = threading.Thread(target=thread1,
                                      args=("Pink Colour Disappears",))
                t1.start()
                op["state"] = "normal"
                kh["state"] = "disabled"
            elif ((obj.aniontest() == True) and (obj.BaCl2(yg) == True)):
                yf.destroy()
                kh.destroy()
                yu.destroy()
                tkinter.Label(text="White PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                t1 = threading.Thread(target=thread1,
                                      args=("White precipitate observed",))
                t1.start()
                jk = tkinter.Label(text="Please add dil. HCl to the PPT", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                jk.pack(pady=30)
                t1 = threading.Thread(target=thread1,
                                      args=("Please add dilute hydrochloric acid to the precipitate",))
                t1.start()
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack()
                bn = xy.get()
                def wettest2():
                    bn = xy.get()
                    if (("dil" in bn) or ("dilute" in bn)) and ("HCl" in bn) == True:
                        tkinter.Label(text="PPT dissolves", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                        t1 = threading.Thread(target=thread1,
                                              args=("precipitate dissolves",))
                        t1.start()
                        op["state"] = "normal"
                        jl["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change", "No change observed")
                jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",width=10, height=1, cursor="hand2")
                jl.pack(pady=10)
            else:
                messagebox.showinfo("No Change", "No change observed")
                print("GH")
    elif a==9:
            if ((obj.aniontest() == True) and (obj.match(yg) == True)):
                tkinter.Label(text="Purple Straks Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                t1 = threading.Thread(target=thread1,
                                      args=("Purple Straks Observed",))
                t1.start()
                op["state"] = "normal"
                kh["state"] = "disabled"
            elif ((obj.aniontest() == True) and (obj.BaCl21(yg) == True)):
                yf.destroy()
                kh.destroy()
                yu.destroy()
                tkinter.Label(text="White PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                t1 = threading.Thread(target=thread1,
                                      args=("Purple precipitate Observed",))
                t1.start()
                jk = tkinter.Label(text="Please add dil. HCl to the PPT", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                t1 = threading.Thread(target=thread1,
                                      args=("Please add dil. HCl to the precipitate",))
                t1.start()
                jk.pack(pady=30)
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack()
                bn = xy.get()
                def wettest2():
                    bn = xy.get()
                    if (("dil" in bn) or ("dilute" in bn)) and ("HCl" in bn) == True:
                        tkinter.Label(text="PPT is Insoluble", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                        t1 = threading.Thread(target=thread1,
                                              args=("precipitate is Insoluble",))
                        t1.start()
                        op["state"] = "normal"
                        jl["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change", "No change observed")
                jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",width=10, height=1, cursor="hand2")
                jl.pack(pady=10)
            else:
                messagebox.showinfo("No Change", "No change observed")
                print("GH")
    elif a==10:
        if ((obj.aniontest() == True) and (obj.HNO3(yg) == True)):
            tkinter.Label(text="White ppt soluble in NH4OH", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("White precipitate soluble in ammonium hydroxide",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        elif ((obj.aniontest() == True) and (obj.MnO2(yg) == True)):
            yf.destroy()
            kh.destroy()
            yu.destroy()
            jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1,args=("Please boil the solution",))
            t1.start()
            jk.pack(pady=30)
            xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            xy.pack()
            bn = xy.get()

            def wettest2():
                bn = xy.get()
                if ("boil" in bn) == True:
                    tkinter.Label(text="Greenish Yellow Gas Evolves", bg="#46A0EC", fg="white",
                                  font="Calibri 20 bold").pack(pady=10)
                    t1 = threading.Thread(target=thread1,args=("Greenish Yellow Gas Evolves",))
                    t1.start()
                    op["state"] = "normal"
                    jl["state"] = "disabled"
                else:
                    messagebox.showinfo("No change", "No change observed")

            jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",
                                width=10, height=1, cursor="hand2")
            jl.pack(pady=10)
        elif ((obj.aniontest() == True) and (obj.K2Cr2O7(yg) == True)):
            yf.destroy()
            kh.destroy()
            yu.destroy()
            jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1, args=("Please boil the solution",))
            t1.start()
            jk.pack(pady=30)
            xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            xy.pack()
            bn = xy.get()

            def wettest2():
                bn = xy.get()
                if ("boil" in bn) == True:
                    kf = tkinter.Label(text="Red Vapours Evolved", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                    t1 = threading.Thread(target=thread1,
                                          args=("Red Vapours Evolved",))
                    t1.start()
                    kf.pack(pady=10)
                    kk = tkinter.Label(text="Do you want to perform test on vapours?", bg="#46A0EC", fg="white",
                                       font="Calibri 20 bold")
                    kk.pack(pady=10)
                    t1 = threading.Thread(target=thread1,
                                          args=("Do you want to perform test on vapours?",))
                    t1.start()
                    op["state"] = "normal"
                    jl["state"] = "disabled"
                    def sometest():
                        kf.destroy()
                        kk.destroy()
                        kh.destroy()
                        yes.destroy()
                        yu.destroy()
                        yf.destroy()
                        jk2 = tkinter.Label(text="Input Action", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                        jk2.pack(pady=30)
                        t1 = threading.Thread(target=thread1,
                                              args=("Input Action",))
                        t1.start()
                        xy2 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        xy2.pack()
                        bn2 = xy2.get()

                        def sometest2():
                            bn2 = xy2.get()
                            if ("NaOH" in bn2):
                                jk2.destroy()
                                xy2.destroy()
                                yu.destroy()
                                perform6.destroy()
                                jk = tkinter.Label(text="Yellow Solution Observed\nInput Action", bg="#46A0EC",
                                                   fg="white", font="Calibri 20 bold")
                                jk.pack(pady=30)
                                t1 = threading.Thread(target=thread1,
                                                      args=("Yellow Solution Observed. Input Action",))
                                t1.start()
                                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                                xy.pack()
                                bn = xy.get()

                                def wettest2():
                                    bn = xy.get()
                                    if ("acetic acid" in bn or "CH3COOH" in bn) and (
                                            "Lead Acetate" in bn or "(CH3COO)2Pb" in bn):
                                        tkinter.Label(text="Yellow PPT Observed", bg="#46A0EC", fg="white",
                                                      font="Calibri 20 bold").pack(pady=10)
                                        t1 = threading.Thread(target=thread1,
                                                              args=("Yellow precipitate Observed",))
                                        t1.start()
                                        op["state"] = "normal"
                                        jl["state"] = "disabled"
                                    else:
                                        messagebox.showinfo("No change", "No change observed")

                                jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white",
                                                    font="Calibri 20 bold", width=10, height=1, cursor="hand2")
                                jl.pack(pady=10)
                            else:
                                messagebox.showinfo("No Change", "No change observed")

                        perform6 = tkinter.Button(text="Perform", command=sometest2, bg="#46A0EC", fg="white",
                                                  font="Calibri 20 bold", width=10, height=1, cursor="hand2")
                        perform6.pack(pady=10)

                yes = tkinter.Button(text="Yes", command=sometest, bg="#46A0EC", fg="white", font="Calibri 20 bold",
                                     width=10, height=1, cursor="hand2")
                yes.pack(pady=10)

        else:
            messagebox.showinfo("No Change", "No change observed")
    elif a == 11:
        if ((obj.aniontest() == True) and (obj.brownring(yg) == True)):
            tkinter.Label(text="Brown Ring at the Junction of the 2 Liquids", bg="#46A0EC", fg="white",
                          font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Brown Ring at the Junction of the 2 Liquids",))
            t1.start()
            op["state"] = "normal"
            kh["state"] = "disabled"
        elif ((obj.aniontest()) == True and (obj.NO2gas(yg) == True)):
            yf.destroy()
            kh.destroy()
            yu.destroy()
            jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1, args=("Please boil the solution",))
            t1.start()
            jk.pack(pady=30)
            xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            xy.pack()
            bn = xy.get()

            def wettest2():
                bn = xy.get()
                if ("boil" in bn) == True:
                    tkinter.Label(text="Reddish Brown Gas Evolved", bg="#46A0EC", fg="white",
                                  font="Calibri 20 bold").pack(
                        pady=10)
                    t1 = threading.Thread(target=thread1,
                                          args=("Reddish Brown Gas Evolved",))
                    t1.start()
                    op["state"] = "normal"
                    jl["state"] = "disabled"

            jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", font="Calibri 20 bold",width=10, height=1, cursor="hand2")
            jl.pack(pady=10)
        else:
            messagebox.showinfo("No Change", "No change observed")
    elif a==12:
        pass
kh=tkinter.Button(text="Perform",command=confirmatory2,bg="#46A0EC",fg="white",font="Calibri 20 bold",width=10,height=1,cursor="hand2")
kh.pack(pady=10)
op = tkinter.Button(text="Proceed to Guess Anion ---->", command=g, bg="#46A0EC", fg="white", font="Calibri 15 bold",width=30, height=1)
op.pack(pady=10)
op["state"]="disabled"
hintimg=PhotoImage(file="Hintlogoimg.png")
hintbutton=tkinter.Button(bg="#46A0EC",borderwidth=3,cursor="hand2",image=hintimg,command=Hint)
hintbutton.place(x=450, y=15)