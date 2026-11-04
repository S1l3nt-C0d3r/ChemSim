from tkinter import *
import tkinter
from tkinter import messagebox
def runM():
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
    import threading
    import pyttsx3 as sound
    global tosay
    tosay=sound.init()
    def thread1():
        global tosay
        tosay.say("Congratulations")
        tosay.runAndWait()
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
    win10= Tk()
    tkinter.Label(text="Please guess the cation",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=30)
    def thread2():
        global tosay
        tosay.say("Please guess the cation")
        tosay.runAndWait()
        if tosay._inLoop:
            tosay.endLoop()
    t2 = threading.Thread(target=thread2)
    t2.start()
    win10.geometry("500x500+500+150")
    win10.configure(background="#46A0EC")
    win10.resizable(0,0)
    win10.title("Guess the Cation")
    kd=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
    kd.pack(pady=10)
    t1 = threading.Thread(target=thread1)

    def guessy():
        if a==1:
            h = kd.get()
            if (h=="Pb+2")or (h=="Pb") or (h=="Lead") or (h=="lead"):
                tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
                og["state"]="disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer","Wrong Answer!\nTry again :)")
        if a==2:
            h = kd.get()
            if (h == "Cu+2") or (h == "Copper cation") or (h == "copper cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==3:
            h = kd.get()
            if (h == "As+3") or (h == "Arsenic cation") or (h == "arsenic cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==4:
            h = kd.get()
            if (h == "Fe+3") or (h == "Iron(3) cation") or (h == "iron(3) cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==5:
            h = kd.get()
            if (h == "Al+3") or (h == "Aluminium cation") or (h == "aluminium cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==6:
            h = kd.get()
            if (h == "Zn+2") or (h == "Zinc cation") or (h == "zinc cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==7:
            h = kd.get()
            if (h == "Co+2") or (h == "Cobalt cation") or (h == "cobalt cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==8:
            h = kd.get()
            if (h == "Ni+2") or (h == "Nickle cation") or (h == "nickle cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==9:
            h = kd.get()
            if (h == "Mn+2") or (h == "Manganese cation") or (h == "manganese cation"):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==10:
            h=kd.get()
            if((h=="Ba+2") or (h=="Barium cation")or (h=="barium cation")or (h=="Barium Cation")or (h=="barium Cation")):
                tkinter.Label(text="Correct Answer!",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer","Wrong Answer!\nTry again :)")
        if a==11:
            h = kd.get()
            if ((h == "Strontium cation") or (h == "Sr+2")):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer","Wrong Answer!\nTry again :)")
        if a==12:
            h = kd.get()
            if ((h == "Calcium cation") or (h == "Ca+2")):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")

        if a==13:
            h = kd.get()
            if ((h == "Magnesium cation") or (h == "Mg+2")):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer", "Wrong Answer!\nTry again :)")
        if a==14:
            h=kd.get()
            if((h=="NH4+1") or (h=="NH4+")):
                tkinter.Label(text="Correct Answer!", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                og["state"] = "disabled"
                t1.start()
            else:
                messagebox.showinfo("Wrong Answer","Wrong Answer!\nTry again :)")
    def back():
        import main
        win10.destroy()
        main.frun()
    og=tkinter.Button(text="Guess",command=guessy,bg="#46A0EC",fg="white",font="Calibri 20 bold",height=2,width=10,cursor="hand2")
    og.pack(pady=10)
    global backimg
    backimg = PhotoImage(file="back.png")
    backbutton = tkinter.Button(win10, image=backimg, bg="#46A0EC", command=back)
    backbutton.place(x=15, y=15)
