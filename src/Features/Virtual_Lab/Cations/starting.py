from tkinter import *
import tkinter
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
    import pyttsx3 as sound
    import threading
    global tosay
    tosay=sound.init()
    global a
    import src.Virtual_Lab.Cations.Selecterscreen as s
    a=s.a
    print(a)
    if a==1:
        obj=Pb()
    elif (a==2):
        obj=Cu()
    elif (a==3):
        obj=As()
    elif (a==4):
        obj=Fe()
    elif (a==5):
        obj=Al()
    elif (a==6):
        obj=Zn()
    elif (a==7):
        obj=Co()
    elif (a==8):
        obj=Ni()
    elif (a==9):
        obj=Mn()
    elif (a==10):
        obj=Ba()
    elif (a==11):
        obj=Sr()
    elif (a==12):
        obj=Ca()
    elif (a==13):
        obj=Mg()
    elif (a==14):
        obj=NH4()
    win3 = Tk()
    def thread2():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = "The Flame Colour is", obj.fcolour
        tosay.say(q)
        tosay.runAndWait()


    def thread1():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = "You are performing Dry Test"
        tosay.say(q)
        tosay.runAndWait()


    def thread3():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = "The Salt Colour is", obj.colour
        tosay.say(q)
        tosay.runAndWait()
    def thread4():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = "Perform Dry or Wet Test"
        tosay.say(q)
        tosay.runAndWait()
    def DryTest():
        t1 = threading.Thread(target=thread1)
        t1.start()
        Dry["state"] = "disabled"
        win3.destroy()
        win4= Tk()
        win4.configure(background="#46A0EC")
        win4.title("Dry Test")
        win4.geometry("500x500+500+150")
        win4.resizable(0, 0)

        def Flame():
            flame["state"] ="disabled"
            label5=tkinter.Label(text="Flame colour is: "+obj.fcolour,bg="#46A0EC",fg="white",font="Titillium  20 bold",wraplength=400,justify="center")
            t2 = threading.Thread(target=thread2)
            t2.start()
            label5.pack()
            if a==1:
                global img8
                img8 = tkinter.PhotoImage(file="Pb flame.png")
                tkinter.Label(image=img8).pack(pady=10)
                win4.geometry("500x700")
            if a == 2:

                global img1
                img1 = PhotoImage(file="Cu flame.png")
                tkinter.Label(image=img1).pack(pady=10)
                win4.geometry("500x700")
            if a == 3:
                global img2
                img2 = PhotoImage(file="As flame.png")
                tkinter.Label(image=img2).pack(pady=10)
                win4.geometry("500x700")
            if a == 4:
                global img4
                img4 = PhotoImage(file="Fe flame.png")
                tkinter.Label(image=img4).pack(pady=10)
                win4.geometry("500x700")
            if a == 5:
                global img5
                img5 = PhotoImage(file="Al flame.png")
                tkinter.Label(image=img5).pack(pady=10)
                win4.geometry("500x700")
            if a == 6:
                global img6
                img6 = PhotoImage(file="Zn flame.png")
                tkinter.Label(image=img6).pack(pady=10)
                win4.geometry("500x700")
            if a == 7:
                global img7
                img7 = PhotoImage(file="Co flame.png")
                tkinter.Label(image=img7).pack(pady=10)
                win4.geometry("500x700")
            if a == 8:
                global img9
                img9 = PhotoImage(file="Ni flame.png")
                tkinter.Label(image=img9).pack(pady=10)
                win4.geometry("500x700")
            if a == 9:
                global img10
                img10 = PhotoImage(file="Mn flame.png")
                tkinter.Label(image=img10).pack(pady=10)
                win4.geometry("500x700")
            if a == 11:
                global img11
                img11 = PhotoImage(file="Sr flame.png")
                tkinter.Label(image=img11).pack(pady=10)
                win4.geometry("500x700")
            if a == 12:
                global img12
                img12 = PhotoImage(file="Ca flame.png")
                tkinter.Label(image=img12).pack(pady=10)
                win4.geometry("500x700")
            if a == 13:
                global img13
                img13 = PhotoImage(file="Mg flame.png")
                tkinter.Label(image=img13).pack(pady=10)
                win4.geometry("500x700")
            elif a==10:
                global img3
                img3=PhotoImage(file="Ba flame.png")
                tkinter.Label(image=img3).pack(pady=10)
                win4.geometry("500x700")
        def Colour():
            colour["state"] = "disabled"
            label6 = tkinter.Label(text="Colour is: "+obj.colour,bg="#46A0EC",fg="white",font="Titillium  20 bold",wraplength=400,justify="center")
            t3 = threading.Thread(target=thread3)
            t3.start()
            label6.pack()
        def Shift():
            win4.destroy()
            import starting1
            starting1.s1run()

        label4 = tkinter.Label(text="You can do two tests\n please choose one",bg="#46A0EC",fg="white",font="Titillium  20 bold",cursor="hand2")
        label4.pack()
        flame = tkinter.Button(text="Flame Test", command=Flame,bg="#46A0EC",fg="white",font="Titillium  20 bold",width=10,height=2,cursor="hand2")
        flame.pack(pady=10)
        colour = tkinter.Button(text="Colour Test", command=Colour,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=10,height=2,cursor="hand2")
        colour.pack(pady=10)
        backbutton = tkinter.Button(text="Back", command=Shift,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=10,height=2,cursor="hand2")
        backbutton.pack(pady=10)
    def WetTest():
        win3.destroy()
        import src.Virtual_Lab.Cations.ppt as ppt
        ppt.pptrun()
    virtualbackground = PhotoImage(file="virtual lab background.png")
    tkinter.Label(win3,image=virtualbackground).pack()
    label1=tkinter.Label(text="Welcome to this Virtual Lab",bg="#46A0EC",fg="white",font="Titillium  20 bold")
    label1.place(x=70,y=10)
    label2=tkinter.Label(text="You have been given a salt. You have to identify the cation present in it",bg="#46A0EC",fg="white",font="Titillium  10 bold")
    label2.place(x=15,y=50)
    label3=tkinter.Label(text="Would you like to perform dry test or wet test?",bg="#46A0EC",fg="white",font="Titillium  10 bold")
    t4 = threading.Thread(target=thread4)
    t4.start()
    label3.place(x=100,y=70)
    Dry= tkinter.Button(text="Dry Test",command=DryTest,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=10,height=2,cursor="hand2")
    Dry.place(x=160,y=130)
    Wet= tkinter.Button(text="Wet Test",command=WetTest,bg="#46A0EC", fg="white",font="Titilium 20 bold",width=10,height=2,cursor="hand2")
    Wet.place(x=160,y=250)
    win3.geometry("500x500+500+150")
    win3.configure(bg="#34495e")
    win3.resizable(0,0)
    win3.title("Virtual Lab ----> Cation")
    win3.mainloop()






            