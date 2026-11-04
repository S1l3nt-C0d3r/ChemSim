import tkinter
import pandas
from tkinter import *
from src.Virtual_Lab.Functional.allclasses import ketone
from src.Virtual_Lab.Functional.allclasses import phenol
from src.Virtual_Lab.Functional.allclasses import COOH
from src.Virtual_Lab.Functional.allclasses import CHO
from src.Virtual_Lab.Functional.allclasses import amine
from src.Virtual_Lab.Functional.allclasses import OH
from tkinter import messagebox
import random as r
import pyttsx3 as sound
import threading
global tosay
tosay=sound.init()
global a
from startfunctional import a
if a == 1:
    obj = COOH()
elif (a == 2):
    obj = phenol()
elif (a == 3):
    obj = CHO()
elif (a == 4):
    obj = ketone()
elif (a == 5):
    obj = amine()
elif (a == 6):
    obj = OH()
win24 = Tk()
win24.geometry("500x500+500+150")
win24.configure(background="#46A0EC")
win24.title("Confirmatory Test")
win24.resizable(0,0)
hello=tkinter.Label(text="Enter Action",bg="#46A0EC",fg="white",font="Calibri 20 bold")
hello.pack(pady=(30,10))
yp=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
yp.pack(pady=10)
yq=yp.get()
def thread2():
    global tosay
    q = "Proceed to Guess Functional Group"
    tosay.say(q)
    tosay.runAndWait()
    if tosay._inLoop:
        tosay.endLoop()

def Hint():
    print(a)
    win92 = Tk()
    win92.geometry("400x500+300+150")
    win92.configure(bg="#46A0EC")
    win92.resizable(0, 0)
    win92.title("Hint")
    df = pandas.read_csv("functional hints.csv", encoding="utf-8")
    catno = list(df.loc[:, "Sr."])
    catgtest = list(df.loc[:, "Functional"])
    cattest = list(df.loc[:, "Ctest"])
    adtest=list(df.loc[:, "AddTest"])
    b = catno.index(a)
    tkinter.Label(win92, text=catgtest[b] + ":"+"\n" + cattest[b],bg="#46A0EC",fg="white", font="Calibri 20 bold",wraplength=350, justify="center").pack(pady=10)
    tkinter.Label(win92, text="Additional Test:", bg="#46A0EC", fg="white", font="Calibri 20 bold", wraplength=350,justify="center").pack(pady=10)
    tkinter.Label(win92, text=adtest[b], bg="#46A0EC", fg="white", font="Calibri 20 bold",wraplength=350, justify="center").pack(pady=10)


def functionguess():
    win24.destroy()
    import functionguesser
def functionaction():
    def thread1(a):
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = a
        tosay.say(q)
        tosay.runAndWait()
        if tosay._inLoop:
            tosay.endLoop()

    global yq
    yq=yp.get()
    if a==1:
        if obj.FTest() and obj.NaHCO3(yq):
            rt=tkinter.Label(text="Effervescence of colourlesss gas",bg="#46A0EC",fg="white",font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1,
                                  args=("Effervescence of colourlesss gas",))
            t1.start()
            rt.pack(pady=10)
            rk=tkinter.Label(text="Do you want to perform tests on the gas?",bg="#46A0EC",fg="white",font="Calibri 20 bold",justify="center",wraplength=400)
            t1 = threading.Thread(target=thread1,
                                  args=("Do you want to perform tests the gas",))
            t1.start()
            rk.pack()
            yr["state"]="disabled"
            ys["state"]="normal"
            def nexttest():
                hello.destroy()
                yp.destroy()
                yr.destroy()
                rt.destroy()
                rk.destroy()
                wrt.destroy()
                rp=tkinter.Label(text="Input action",bg="#46A0EC",fg="white",font="Calibri 20 bold")
                rp.pack(pady=10)
                t1 = threading.Thread(target=thread1,
                                      args=("Input action",))
                t1.start()
                rh=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
                rh.pack(pady=10)
                def action3():
                    wry=rh.get()
                    if "lime water" in wry.lower():
                        tkinter.Label(text="Gas Turns Lime Water Milky",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
                        t1 = threading.Thread(target=thread1,
                                              args=("Gas Turns Lime Water Milky",))
                        t1.start()
                        ark["state"]="disabled"
                    else:
                        messagebox.showinfo("No Change","No change observed")
                ark=tkinter.Button(text="Perform",command=action3, bg="#46A0EC",fg="white", font="Calibri 20 bold", width=10, height=2)
                ark.pack(pady=10)
            wrt=tkinter.Button(text="Yes",command=nexttest, bg="#46A0EC",fg="white", font="Calibri 20 bold", width=10, height=2)
            wrt.pack()
        elif (obj.FTest() == True) and (obj.C2H5OH(yq) == True):
            yp.destroy()
            yr.destroy()
            hello.destroy()
            tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Please boil the solution",))
            t1.start()
            rh = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            rh.pack(pady=10)
            def action3():
                wry = rh.get()
                if "boil" in wry.lower():
                    tkinter.Label(text="Gas Evolved Turns Lime Water Milky", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                    t1 = threading.Thread(target=thread1,
                                          args=("Gas Turns Lime Water Milky",))
                    t1.start()
                    ark["state"]="disabled"
                    ys["state"]="normal"
                else:
                    messagebox.showinfo("No Change", "No change observed")

            ark = tkinter.Button(text="Perform", command=action3, bg="#46A0EC", fg="white", font="Calibri 15 bold",width=40, height=1)
            ark.pack(pady=10)
        else:
            messagebox.showinfo("No Change","No change observed")
    if a==2:
        if(obj.FTest()==True) and (obj.NaOH(yq)==True):
            tkinter.Label(text="Compound Soluble in NaOH",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Compound Soluble in NaOH",))
            t1.start()
            ys["state"]="normal"
            yr["state"]="disabled"
        elif(obj.FTest()==True) and (obj.FeCl3(yq)==True):
            tkinter.Label(text="Blue/Violet Colour Solution",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Blue/Violet Colour Solution",))
            t1.start()
            ys["state"] = "normal"
            global img1
            img1 = PhotoImage(file="Phenol ppt.png")
            win24.geometry("500x700")
            tkinter.Label(image=img1).pack(pady=10)
            yr["state"]="disabled"
        else:
            messagebox.showinfo("No Change","No change observed")
    if a==3:
        if(obj.FTest()==True) and (obj.schiff(yq)==True):
            tkinter.Label(text="Pink Purple Colour Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Pink Purple Colour Observed",))
            t1.start()
            ys["state"]="normal"
            yr["state"]="disabled"
        elif(obj.FTest()==True) and (obj.tollen(yq)==True):
            tkinter.Label(text="Grey Colour Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Grey Colour Observed",))
            t1.start()
            ys["state"] = "normal"
            global img2
            img2=PhotoImage(file="CHO.png")
            win24.geometry("500x700")
            tkinter.Label(image=img2).pack(pady=10)
            yr["state"]="disabled"
        elif (obj.FTest()==True) and (obj.DNP24(yq)==True):
            tkinter.Label(text="Yellow Orange PPT Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Yellow Orange precipitate Observed",))
            t1.start()
            ys["state"] = "normal"
            global img3
            img3=PhotoImage(file="CHO ppt.png")
            win24.geometry("500x700")
            tkinter.Label(image=img3).pack(pady=10)
            yr["state"]="disabled"
        else:
            messagebox.showinfo("No Change","No change observed")
    if a==4:
        if (obj.FTest() == True) and (obj.DNP24(yq) == True):
            tkinter.Label(text="Yellow Orange PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Yellow Orange precipitate Observed",))
            t1.start()
            ys["state"] = "normal"
            global img5
            img5=PhotoImage(file="Ketoneppt.png")
            win24.geometry("500x700")
            tkinter.Label(image=img5).pack(pady=10)
            yr["state"] = "disabled"
        elif (obj.FTest() == True) and (obj.Nanitpro(yq) == True):
            tkinter.Label(text="Blood Red Colouration", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
            t1 = threading.Thread(target=thread1,
                                  args=("Blood Red Colouration",))
            t1.start()
            ys["state"] = "normal"
            global img4
            img4 = PhotoImage(file="Ketone.png")
            win24.geometry("500x700")
            tkinter.Label(image=img4).pack(pady=10)
            yr["state"] = "disabled"
        else:
            messagebox.showinfo("No Change", "No change observed")
    if a==5:
        if (obj.FTest() == True) and (obj.test(yq) == True):
            yp.destroy()
            yr.destroy()
            hello.destroy()
            fk=tkinter.Label(text="Please cool the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1,
                                  args=("Please cool the solution",))
            t1.start()
            fk.pack(pady=10)
            rh = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
            rh.pack(pady=10)
            def action3():
                wry = rh.get()
                if "cool" in wry.lower():
                    tkinter.Label(text="Input Action", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                    ark.destroy()
                    rh.destroy()
                    fk.destroy()
                    rj=tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                    rj.pack(pady=10)
                    def action4():
                        rd=rj.get()
                        if ("B-naphthol" in rd) and ("NaOH" in rd):
                            tkinter.Label(text="Orange Red Dye Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                            t1 = threading.Thread(target=thread1,
                                                  args=("Orange Red Dye Observed",))
                            t1.start()
                            jk["state"]="disabled"
                            global img6
                            img6=PhotoImage(file="Amine.png")
                            win24.geometry("500x700")
                            tkinter.Label(image=img6).pack(pady=10)
                            ys["state"]="normal"
                        else:
                            messagebox.showinfo("No Change","No change observed")
                    jk=tkinter.Button(text="Perform",command=action4,bg="#46A0EC",fg="white",font="Calibri 20 bold",width=10,height=2,cursor="hand2")
                    jk.pack(pady=10)
                else:
                    messagebox.showinfo("No Change", "No change observed")

            ark = tkinter.Button(text="Perform", command=action3, bg="#46A0EC", fg="white", font="Calibri 20 bold",width=10, height=2)
            ark.pack(pady=10)
        else:
            messagebox.showinfo("No Change", "No change observed")
    elif a==6:
        if obj.FTest() and obj.Na(yq):
            rt=tkinter.Label(text="Effervescence of colourlesss gas",bg="#46A0EC",fg="white",font="Calibri 20 bold")
            t1 = threading.Thread(target=thread1,
                                  args=("Effervescence of colourlesss gas",))
            t1.start()
            rt.pack(pady=10)
            rk=tkinter.Label(text="Do you want to perform tests on effervescence?",bg="#46A0EC",fg="white",font="Calibri 20 bold",justify="center",wraplength=400)
            rk.pack()
            t1 = threading.Thread(target=thread1,
                                  args=("Do you want to perform tests on effervescence?",))
            t1.start()
            yr["state"]="disabled"
            ys["state"]="normal"
            def nexttest():
                hello.destroy()
                yp.destroy()
                yr.destroy()
                rt.destroy()
                rk.destroy()
                wrt.destroy()
                rp=tkinter.Label(text="Input action",bg="#46A0EC",fg="white",font="Calibri 20 bold")
                rp.pack(pady=10)
                rh=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
                rh.pack(pady=10)
                def action3():
                    wry=rh.get()
                    if "match" in wry.lower():
                        tkinter.Label(text="Gas Burns With a Pop Sound",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
                        t1 = threading.Thread(target=thread1,
                                              args=("Gas Burns With a Pop Sound",))
                        t1.start()
                        ark["state"]="disabled"
                    else:
                        messagebox.showinfo("No Change","No change observed")
                ark=tkinter.Button(text="Perform",command=action3, bg="#46A0EC",fg="white", font="Calibri 20 bold", width=10, height=2)
                ark.pack(pady=10)
            wrt=tkinter.Button(text="Yes",command=nexttest, bg="#46A0EC",fg="white", font="Calibri 20 bold", width=10, height=2)
            wrt.pack()
        else:
            messagebox.showinfo("No Change","No change observed")
yr=tkinter.Button(text="Perform",command=functionaction,bg="#46A0EC",fg="white",font="Calibri 20 bold",width=10,height=1,cursor="hand2")
yr.pack(pady=10)
ys = tkinter.Button(text="Proceed to Guess Functional Group ---->", command=functionguess, bg="#46A0EC",fg="white", font="Calibri 15 bold", width=40, height=1)
ys.pack(pady=10)
hintimg=PhotoImage(file="Hintlogoimg.png")
hintbutton=tkinter.Button(bg="#46A0EC",borderwidth=3,cursor="hand2",image=hintimg,command=Hint)
hintbutton.place(x=450, y=15)
t2 = threading.Thread(target=thread2)
t2.start()
ys["state"]="disabled"