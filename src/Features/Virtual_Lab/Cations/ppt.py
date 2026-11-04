import tkinter
from tkinter import *
from tkinter import messagebox
def pptrun():
    global k
    import pandas
    import src.Virtual_Lab.Cations.Selecterscreen as s
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
    import threading
    import pyttsx3 as sound
    global ac
    if   (a==1): obj=Pb()
    elif (a==2): obj=Cu()
    elif (a==3): obj=As()
    elif (a==4): obj=Fe()
    elif (a==5): obj=Al()
    elif (a==6): obj=Zn()
    elif (a==7): obj=Co()
    elif (a==8): obj=Ni()
    elif (a==9): obj=Mn()
    elif (a==10): obj=Ba()
    elif (a==11): obj=Sr()
    elif (a==12): obj=Ca()
    elif (a==13): obj=Mg()
    elif (a==14): obj=NH4()
    win8 = Tk()
    wetLabel = tkinter.Label(text="You have made a salt solution o.s\nplease type in an action",font="Calibri 20 bold",bg="#46A0EC",fg="white")
    wetLabel.pack(pady=(60,10))
    ab = tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
    ab.pack()
    global tosay
    tosay=sound.init()
    def thread1():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = "You are performing Wet Test","You have made the Original Solution. please type in an action"
        tosay.say(q)
        tosay.runAndWait()
    t1 = threading.Thread(target=thread1)
    t1.start()

    def hint():
        win92 = Tk()
        win92.geometry("300x300+300+150")
        win92.configure(bg="#46A0EC")
        win92.resizable(0, 0)
        win92.title("Hint")
        df = pandas.read_csv("Cation_Hints(Group).csv", encoding="utf-8")
        catno = list(df.loc[:, "Sr."])
        catgtest = list(df.loc[:, "GTest"])
        cattest = list(df.loc[:, "Test"])
        b = catno.index(a)

        def thread4():
            global tosay
            if tosay._inLoop:
                tosay.endLoop()
            q = cattest[a-1].replace("dil.","dilute").replace("H2S","hydrogen sulfide").replace("NH4Cl", "ammonium chloride").replace("HNO3", "nitric acid").replace("NaOH", "sodium hydroxide")
            q=q.replace("NH4OH", "ammonium hydroxide").replace("(NH4)2CO3", "ammonium carbonate",).replace("(NH4)3PO4", "ammonium phosphate").replace("HCl","hydrochloric acid")
            tosay.say(q)
            tosay.runAndWait()

        t4 = threading.Thread(target=thread4)
        t4.start()
        tkinter.Label(win92, text=catgtest[b] + "\n" + cattest[b], bg="#46A0EC",
                      fg="white", font="Calibri 20 bold",
                      wraplength=250, justify="center").pack(pady=10)
    def bonus():
        popupwindow = Tk()
        popupwindow.title("Bonus Question")
        popupwindow.configure(bg="#46A0EC")
        popupwindow.geometry("300x300+100+100")
        if a!=14:
            T1 = Label(popupwindow,
                       text="What is the name of the compound formed in the precipitate? ",
                       justify="center", wraplength=300, bg="#46A0EC", font="Calibri 14 bold",fg="white")
        else:
            T1 = Label(popupwindow,
                       text="What is the name of the compound formed?",
                       justify="left", wraplength=300, bg="#46A0EC", font="Calibri 14 bold",fg="white")
        def thread3():
            global tosay
            if tosay._inLoop:
                tosay.endLoop()
            q = "Name the Compound"
            tosay.say(q)
            tosay.runAndWait()
        t3 = threading.Thread(target=thread3)
        t3.start()

        t1 = threading.Thread(target=thread1)
        kd = tkinter.Entry(popupwindow, font="none 26 bold", borderwidth=5,width=10, justify='center')

        def checkanswer():
            b=kd.get()
            if ((a==1 and (b.lower()=="lead chloride" or b=="PbCl2")) or\
               (a==2 and (b.lower()=="copper sulphide" or b=="CuS")) or\
               (a==3 and (b.lower() == "arsenic sulphide" or b == "As2S3")) or\
               (a==4 and (b.lower() == "ferric hydroxide" or b == "Fe(OH)3")) or\
               (a==5 and (b.lower() == "aluminium" or b.lower() == "aluminum" or b == "Al(OH)3")) or\
               (a==6 and (b.lower() == "zinc sulphide" or b == "ZnS")) or\
               (a==7 and (b.lower() == "cobalt sulphide" or b == "CoS")) or\
               (a==8 and (b.lower() == "nickel" or b == "NiS")) or\
               (a==9 and (b.lower() == "manganese sulphide" or b == "MnS")) or\
               (a==10 and (b.lower() == "barium carbonate" or b == "BaCO3")) or\
               (a==11 and (b.lower() == "strontium carbonate" or b == "SrCO3"))or\
               (a==12 and (b.lower() == "calcium carbonate" or b == "CaCO3")) or\
               (a==13and (b.lower() == "magnesium hydroxide" or b == "Mg(OH)2"))or\
               (a==14 and (b.lower() == "ammonia" or b == "NH3"))):


                ftext = Label(popupwindow,
                           text="Correct",
                           justify="left", wraplength=500,fg="White", bg="#46A0EC", font="Calibri 14 bold")
                ftext.pack()
                og["state"]="disabled"
                def thread4():
                    global tosay
                    if tosay._inLoop:
                        tosay.endLoop()
                    q = "Correct Answer"
                    tosay.say(q)
                    tosay.runAndWait()

                t4 = threading.Thread(target=thread4)
                t4.start()

        og = tkinter.Button(popupwindow, text="Submit", command=checkanswer, bg="#46A0EC", fg="white", font="Calibri 20 bold", height=2,
                            width=10, cursor="hand2")
        T1.pack()
        kd.pack()
        og.pack(pady=10)

    bonusqh = PhotoImage(file="bonuslogo.png")
    bonusq = Button(
        win8,
        bg="#46A0EC",
        borderwidth=3,
        cursor="hand2",
        image=bonusqh,
        command=bonus,
    )
    def thread2():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = obj.gpc + " precipitate Observed", "Please Proceed to the Confirmatory Test"
        tosay.say(q)
        tosay.runAndWait()
    t2 = threading.Thread(target=thread2)
    def thread3():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        q = "No Change Observed"
        tosay.say(q)
        tosay.runAndWait()
    t3 = threading.Thread(target=thread3)
    def action():
        def confirmatory():
            win8.destroy()
            import src.Virtual_Lab.Cations.confirm1 as confirm1
            confirm1.crun()
        ac = ab.get()
        if a == 1:
            if (obj.g1(ac)):
                gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold")
                t2.start()
                gpc1.pack()
                bonusq.place(x=410, y=15)
                confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC",fg="white",font="Calibri 15 bold").pack()
                perform["state"] = "disabled"
                win8.geometry("500x700")
                global img1
                img1 = PhotoImage(file="Pb test img.png")
                az=tkinter.Label(win8,image=img1)
                az.pack(pady=30)
            else:
               messagebox.showinfo("No change","No change observed")
               t3.start()
        elif a == 2 or a == 3:
            if obj.g1(ac):
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                wetLabel1 = tkinter.Label(text="You Have an Acidified OS\nInput Action",font="Calibri 20 bold", bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(60, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def copper():
                    ac1 = ab1.get()
                    if obj.g2(ac1):
                        global img2
                        img2 = PhotoImage(file="Cuppt.png")
                        gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold",wraplength=400, justify="center")
                        t2.start()
                        gpc1.pack()
                        win8.geometry("500x700")
                        az = tkinter.Label(win8, image=img2)
                        az.pack(pady=30)
                        bonusq.place(x=410, y=15)
                        confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory, bg="#46A0EC",fg="white", font="Calibri 15 bold").pack()
                        perform1["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change", "No change observed")
                        t3.start()
                perform1=tkinter.Button(text="Perform", command=copper,bg="#46A0EC",fg="white",height=2,width=10,font="Calibri 20 bold",cursor="hand2")
                perform1.pack(pady=30)
            else:
                messagebox.showinfo("No change", "No change observed")
                t3.start()
        elif a == 4 or a == 5:
            if obj.g1(ac):
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                wetLabel1 = tkinter.Label(text="You Have an Acidified OS\nInput Action", font="Calibri 20 bold",bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(60, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def destroy():
                    xd=ab1.get()
                    if "" in xd:
                        messagebox.showinfo("No change","No change observed")
                        t3.start()
                        wetLabel1.destroy()
                        ab1.destroy()
                        perform1.destroy()
                        wetLabel = tkinter.Label(text="You have made a salt solution o.s\nplease type in an action",font="Calibri 20 bold", bg="#46A0EC", fg="white")
                        wetLabel.pack(pady=(60, 10))
                        ab = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        ab.pack()
                        def next():
                            ac=ab.get()
                            if obj.g3(ac):
                                wetLabel.destroy()
                                ab.destroy()
                                perform.destroy()
                                wetLabel12 = tkinter.Label(text="Please boil the solution", font="Calibri 20 bold", bg="#46A0EC",fg="white")
                                wetLabel12.pack(pady=(60, 10))
                                ab12 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                                ab12.pack()
                                def copper():
                                    ac3= ab12.get()
                                    if obj.boil(ac3):
                                        gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                                        t2.start()
                                        gpc1.pack()
                                        global img3
                                        img3 = PhotoImage(file="Feppt.png")
                                        gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                                        t2.start()
                                        gpc1.pack()
                                        win8.geometry("500x700")
                                        az = tkinter.Label(win8, image=img3)
                                        az.pack(pady=30)
                                        bonusq.place(x=410, y=15)
                                        confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC", fg="white", font="Calibri 15 bold").pack()
                                        perform12["state"] = "disabled"
                                    else:
                                        messagebox.showinfo("No change", "No change observed")
                                        t3.start()

                                perform12 = tkinter.Button(text="Perform", command=copper, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                                perform12.pack(pady=30)
                            else:
                                messagebox.showinfo("No change", "No change observed")
                                t3.start()

                        perform = tkinter.Button(text="Perform", command=next, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                        perform.pack(pady=30)
                perform1 = tkinter.Button(text="Perform", command=destroy, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                perform1.pack(pady=30)
            elif obj.g3(ac):
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                wetLabel1 = tkinter.Label(text="Please boil the solution", font="Calibri 20 bold", bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(60, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def copper():
                    ac1 = ab1.get()
                    if obj.boil(ac1):
                        global img6
                        if a==4:
                            img6 = PhotoImage(file="Feppt.png")
                        elif a==5:
                            img6=PhotoImage(file="Alppt.png")
                        gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                        t2.start()
                        gpc1.pack()
                        win8.geometry("500x700")
                        az = tkinter.Label(win8, image=img6)
                        az.pack(pady=30)
                        bonusq.place(x=410, y=15)
                        confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC", fg="white", font="Calibri 15 bold").pack()
                        perform1["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change", "No change observed")
                        t3.start()
                perform1 = tkinter.Button(text="Perform", command=copper, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                perform1.pack(pady=30)
            else:
                messagebox.showinfo("No change", "No change observed")
                t3.start()
        elif a == 9 or a == 6 or a == 7 or a == 8:
            global ak
            global al
            ak = ab.get()
            if obj.g1(ak):
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                wetLabel1 = tkinter.Label(text="You Have an Acidified OS\nInput Action", font="Calibri 20 bold",bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(60, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def destroy():
                    xd=ab1.get()
                    if "" in xd:
                        messagebox.showinfo("No change","No change observed")
                        t3.start()
                        wetLabel1.destroy()
                        ab1.destroy()
                        perform1.destroy()
                        wetLabel = tkinter.Label(text="You have made a salt solution o.s\nplease type in an action",font="Calibri 20 bold", bg="#46A0EC", fg="white")
                        wetLabel.pack(pady=(60, 10))
                        ab = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        ab.pack()
                        def next():
                            ac=ab.get()
                            if obj.g3g4(ac) == True:
                                wetLabel.destroy()
                                ab.destroy()
                                perform.destroy()
                                jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white",font="Calibri 20 bold")
                                jk.pack(pady=30)
                                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                                xy.pack(pady=10)
                                al = xy.get()
                                def boil1():
                                    al = xy.get()
                                    if obj.boil(al) == True:
                                        tkinter.Label(text="Input action", bg="#46A0EC", fg="white", font="Calibri 20 bold",wraplength=400, justify="center").pack(pady=30)
                                        xy.destroy()
                                        jkl.destroy()
                                        jk.destroy()
                                        xz = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                                        xz.pack(pady=10)
                                        ag = xz.get()
                                        def wettest2():
                                            ag = xz.get()
                                            if (("H2S" in ag) and ("sol" or "solution" in ag)):
                                                global img4
                                                img4 = PhotoImage(file="Coppt.png")
                                                gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC",fg="white", font="Calibri 20 bold", wraplength=400,justify="center")
                                                t2.start()
                                                gpc1.pack()
                                                win8.geometry("500x700")
                                                az = tkinter.Label(win8, image=img4)
                                                az.pack(pady=30)
                                                bonusq.place(x=410, y=15)
                                                confirm = tkinter.Button(text="Proceed to confirmatory test --->",command=confirmatory, bg="#46A0EC", fg="white",font="Calibri 15 bold").pack()
                                                jl["state"] = "disabled"
                                            else:
                                                messagebox.showinfo("No Change", "No Change Observed")

                                        jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white",height=2, width=10, font="Calibri 20 bold", cursor="hand2")
                                        jl.pack(pady=10)
                                    elif obj.boil(al) == False:
                                        messagebox.showinfo("No Change", "No Change Observed")
                                        t3.start()
                                jkl = tkinter.Button(text="Perform", command=boil1, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                                jkl.pack(pady=10)
                            else:
                                messagebox.showinfo("No Change", "No Change Observed")
                                t3.start()
                        perform = tkinter.Button(text="Perform", command=next, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                        perform.pack(pady=30)
                perform1 = tkinter.Button(text="Perform", command=destroy, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                perform1.pack(pady=30)
            elif obj.g3g4(ak) == True:
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                jk.pack(pady=30)
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack(pady=10)
                al = xy.get()
                def boil1():
                    al = xy.get()
                    if obj.boil(al) == True:
                        tkinter.Label(text="Input action", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center").pack(pady=30)
                        xy.destroy()
                        jkl.destroy()
                        jk.destroy()
                        xz = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        xz.pack(pady=10)
                        ag = xz.get()
                        def wettest2():
                            ag = xz.get()
                            if (("H2S" in ag) and ("sol" or "solution"in ag)):
                                global img5
                                img5 = PhotoImage(file="Coppt.png")
                                gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                                t2.start()
                                gpc1.pack()
                                win8.geometry("500x700")
                                az = tkinter.Label(win8, image=img5)
                                az.pack(pady=30)
                                bonusq.place(x=410, y=15)
                                confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC", fg="white", font="Calibri 15 bold").pack()
                                jl["state"] = "disabled"
                            else:
                                messagebox.showinfo("No Change", "No Change Observed")
                        jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                        jl.pack(pady=10)
                    elif obj.boil(al) == False:
                        messagebox.showinfo("No Change", "No Change Observed")

                jkl = tkinter.Button(text="Perform", command=boil1, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                jkl.pack(pady=10)
            else:
                messagebox.showinfo("No change","No change observed")
                t3.start()
        elif a == 10 or a == 11 or a == 12:
            if obj.g1(ac):
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                wetLabel1 = tkinter.Label(text="You Have an Acidified OS\nInput Action", font="Calibri 20 bold",bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(60, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def destroy():
                    xd=ab1.get()
                    if "" in xd:
                        messagebox.showinfo("No change","No change observed")
                        t3.start()
                        wetLabel1.destroy()
                        ab1.destroy()
                        perform1.destroy()
                        wetLabel = tkinter.Label(text="You have made a salt solution o.s\nplease type in an action",font="Calibri 20 bold", bg="#46A0EC", fg="white")
                        wetLabel.pack(pady=(60, 10))
                        ab = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        ab.pack()
                        def next():
                            ac=ab.get()
                            if (obj.g5(ac)):
                                gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                                t2.start()
                                gpc1.pack()
                                global ba
                                ba = PhotoImage(file="Ba ppt.png")
                                tkinter.Label(image=ba).pack(pady=10)
                                bonusq.place(x=410, y=15)
                                confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC", fg="white", font="Calibri 15 bold").pack()
                                perform["state"] = "disabled"
                                win8.geometry("500x700")
                            else:
                                messagebox.showinfo("No change","No change observed")
                                t3.start()
                        perform = tkinter.Button(text="Perform", command=next, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                        perform.pack(pady=30)
                perform1 = tkinter.Button(text="Perform", command=destroy, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                perform1.pack(pady=30)
            elif (obj.g5(ac)):
                gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold",wraplength=400,justify="center")
                t2.start()
                gpc1.pack()
                global ba
                ba=PhotoImage(file="Ba ppt.png")
                tkinter.Label(image=ba).pack(pady=10)
                bonusq.place(x=410, y=15)
                confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC",fg="white",font="Calibri 15 bold").pack()
                perform["state"] = "disabled"
                win8.geometry("500x700")
            else:
                messagebox.showinfo("No change","No change observed")
                t3.start()
        elif a == 13:
            if obj.g1(ac):
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                wetLabel1 = tkinter.Label(text="You Have an Acidified OS\nInput Action", font="Calibri 20 bold",bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(60, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def destroy():
                    xd=ab1.get()
                    if "" in xd:
                        messagebox.showinfo("No change","No change observed")
                        t3.start()
                        wetLabel1.destroy()
                        ab1.destroy()
                        perform1.destroy()
                        wetLabel = tkinter.Label(text="You have made a salt solution o.s\nplease type in an action",font="Calibri 20 bold", bg="#46A0EC", fg="white")
                        wetLabel.pack(pady=(60, 10))
                        ab = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        ab.pack()
                        def next():
                            ac=ab.get()
                            if obj.g6(ac):
                                global img7
                                img7 = PhotoImage(file="Mgppt.png")
                                gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                                t2.start()
                                gpc1.pack()
                                win8.geometry("500x700")
                                az = tkinter.Label(win8, image=img7)
                                az.pack(pady=30)
                                bonusq.place(x=410, y=15)
                                confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC", fg="white", font="Calibri 15 bold").pack()
                                perform["state"] = "disabled"
                            else:
                                messagebox.showinfo("No change","No change observed")
                                t3.start()
                        perform = tkinter.Button(text="Perform", command=next, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                        perform.pack(pady=30)
                perform1 = tkinter.Button(text="Perform", command=destroy, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                perform1.pack(pady=30)
            elif obj.g6(ac):
                global img8
                img8 = PhotoImage(file="Mgppt.png")
                gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold",wraplength=400, justify="center")
                t2.start()
                gpc1.pack()
                win8.geometry("500x700")
                az = tkinter.Label(win8, image=img8)
                az.pack(pady=30)
                bonusq.place(x=410, y=15)
                confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory, bg="#46A0EC",fg="white", font="Calibri 15 bold").pack()
                perform["state"] = "disabled"
            else:
                messagebox.showinfo("No change", "No change observed")
                t3.start()
        elif a == 14:
            if obj.g1(ac):
                wetLabel.destroy()
                ab.destroy()
                perform.destroy()
                wetLabel1 = tkinter.Label(text="You Have an Acidified OS\nInput Action", font="Calibri 20 bold",bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(60, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def destroy():
                    xd=ab1.get()
                    if "" in xd:
                        messagebox.showinfo("No change","No change observed")
                        t3.start()
                        wetLabel1.destroy()
                        ab1.destroy()
                        perform1.destroy()
                        wetLabel = tkinter.Label(text="You have made a salt solution o.s\nplease type in an action",font="Calibri 20 bold", bg="#46A0EC", fg="white")
                        wetLabel.pack(pady=(60, 10))
                        ab = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        ab.pack()
                        def next():
                            ac=ab.get()
                            if obj.g0(ac):
                                perform.destroy()
                                wetLabel.destroy()
                                ab.destroy()
                                wetLabel1 = tkinter.Label(text="Please boil the solution", font="Calibri 20 bold",bg="#46A0EC", fg="white")
                                wetLabel1.pack(pady=(40, 10))
                                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                                ab1.pack()
                                def boiler():
                                    ah1 = ab1.get()
                                    if obj.boil(ah1):
                                        gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                                        t2.start()
                                        gpc1.pack()
                                        global confirm
                                        bonusq.place(x=410, y=15)
                                        confirm = tkinter.Button(text="Proceed to confirmatory test --->",command=confirmatory, bg="#46A0EC", fg="white",font="Calibri 15 bold")
                                        confirm.pack(pady=10)
                                        perform1["state"] = "disabled"
                                    else:
                                        messagebox.showinfo("No change","No change observed")
                                        t3.start()
                                perform1 = tkinter.Button(text="Perform", command=boiler, bg="#46A0EC", fg="white",height=2, width=10, font="Calibri 20 bold", cursor="hand2")
                                perform1.pack(pady=30)
                            else:
                                messagebox.showinfo("No change","No change observed")
                                t3.start()
                        perform = tkinter.Button(text="Perform", command=next, bg="#46A0EC", fg="white", height=2,width=10, font="Calibri 20 bold", cursor="hand2")
                        perform.pack(pady=30)
                perform1 = tkinter.Button(text="Perform", command=destroy, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                perform1.pack(pady=30)
            elif obj.g0(ac):
                perform.destroy()
                wetLabel.destroy()
                ab.destroy()
                wetLabel1 = tkinter.Label(text="Please boil the solution", font="Calibri 20 bold", bg="#46A0EC", fg="white")
                wetLabel1.pack(pady=(40, 10))
                ab1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                ab1.pack()
                def boiler():
                    ah1 = ab1.get()
                    if obj.boil(ah1):
                        gpc1 = tkinter.Label(text=obj.gpc + " PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center")
                        t2.start()
                        gpc1.pack()
                        global confirm
                        bonusq.place(x=410, y=15)
                        confirm = tkinter.Button(text="Proceed to confirmatory test --->", command=confirmatory,bg="#46A0EC", fg="white", font="Calibri 15 bold")
                        confirm.pack(pady=10)
                        perform1["state"] = "disabled"
                perform1 = tkinter.Button(text="Perform", command=boiler, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                perform1.pack(pady=30)
            else:
                messagebox.showinfo("No change", "No change observed")
                t3.start()
        elif (a != 14):
            gpc1 = tkinter.Label(text=obj.gpc+" PPT Observed",bg="#46A0EC",fg="white",font="Calibri 10 bold")
            t2.start()
            gpc1.pack()
            bonusq.place(x=410, y=15)
            confirm = tkinter.Button(text="Proceed to confirmatory test --->",command = confirmatory,bg="#46A0EC",fg="white",font="Calibri 10 bold").pack()
            perform["state"]="disabled"
            k=1
        else:
            gpc1 = tkinter.Label(name=obj.gpc+"PPT Observed")
            t2.start()
            gpc1.pack()

    perform = tkinter.Button(text="Perform", command=action,bg="#46A0EC",fg="white",height=2,width=10,font="Calibri 20 bold",cursor="hand2")
    perform.pack(pady=30)
    global helpme
    if s.counter==1:
        helpme=PhotoImage(file="Disabled question.png")
        hintbutton = tkinter.Button(bg="#46A0EC", borderwidth=3, cursor="hand2", image=helpme)
        hintbutton.place(x=450, y=15)
    elif s.counter==0:
        helpme=PhotoImage(file="Hintlogoimg.png")
        hintbutton=tkinter.Button(bg="#46A0EC",borderwidth=3,cursor="hand2",image=helpme,command=hint)
        hintbutton.place(x=450, y=15)
    win8.geometry("500x500+500+150")
    win8.configure(bg="#46A0EC")
    win8.resizable(0,0)
    win8.title("Wet Test")
    win8.mainloop()