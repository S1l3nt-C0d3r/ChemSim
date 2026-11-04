import tkinter
from tkinter import *
from tkinter import messagebox
import pandas
def crun():
    import src.Virtual_Lab.Cations.Selecterscreen as s
    counter=s.counter
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
    global tosay
    tosay=sound.init()
    if a==1:     obj=Pb()
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
    win9 = Tk()
    action1 = tkinter.Label(text="Input Action",bg="#46A0EC",fg="white",font="Calibri 20 bold")
    action1.pack(pady=30)
    win9.geometry("500x500+500+150")
    win9.configure(background="#46A0EC")
    win9.resizable(0,0)
    win9.title("Confirmatory Test")
    ad=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
    ad.pack()
    am = ad.get()
    def bonus():
        popupwindow = Tk()
        popupwindow.title("Bonus Question")
        popupwindow.configure(bg="#46A0EC")
        popupwindow.geometry("300x300+100+100")
        if a!=14:
            T1 = Label(popupwindow,
                       text="What is the name of the compound formed in the precipitate? ",
                       justify="left", wraplength=300, fg="white",bg="#46A0EC", font="Calibri 14 bold")
        else:
            T1 = Label(popupwindow,
                       text="What is the name of the compound formed?",
                       justify="left", wraplength=300, bg="#46A0EC",fg="White", font="Calibri 14 bold")
        def thread3():
            global tosay
            if tosay._inLoop:
                tosay.endLoop()
            q = "Name the Compound"
            tosay.say(q)
            tosay.runAndWait()
        t3 = threading.Thread(target=thread3)
        t3.start()


        kd = tkinter.Entry(popupwindow, font="none 26 bold", borderwidth=5,width=10, justify='center')

        def checkanswer():
            b=kd.get()
            global am
            global needed
            if (a==1 and (am=="K2CrO4") and (b.lower()==needed[2] or b==needed[3])):
                ftext = Label(popupwindow,
                              text="Correct",
                              justify="left", wraplength=500, bg="#46A0EC", font="Calibri 14 bold")
                ftext.pack()
                og["state"] = "disabled"

                def thread5():
                    global tosay
                    if tosay._inLoop:
                        tosay.endLoop()
                    q = "Correct Answer"
                    tosay.say(q)
                    tosay.runAndWait()

                t5 = threading.Thread(target=thread5)
                t5.start()
            elif ((b.lower()==needed[0] or b==needed[1])):
                ftext = Label(popupwindow,
                           text="Correct",
                           justify="left", wraplength=500, bg="#46A0EC", font="Calibri 14 bold")
                ftext.pack()
                og["state"]="disabled"
                def thread5():
                    global tosay
                    if tosay._inLoop:
                        tosay.endLoop()
                    q = "Correct Answer"
                    tosay.say(q)
                    tosay.runAndWait()

                t5 = threading.Thread(target=thread5)
                t5.start()



        og = tkinter.Button(popupwindow, text="Submit", command=checkanswer, bg="#46A0EC", fg="white", font="Calibri 20 bold", height=2,
                            width=10, cursor="hand2")
        T1.pack()
        kd.pack()
        og.pack(pady=10)

    global bonusqh
    bonusqh = PhotoImage(file="bonuslogo.png")
    bonusq = Button(
        win9,
        bg="#46A0EC",
        borderwidth=3,
        cursor="hand2",
        image=bonusqh,
        command=bonus,
    )

    def guess():
        win9.destroy()
        import src.Virtual_Lab.Cations.Guesser as Guesser
        Guesser.runM()

    def Hint():
        win92 = Tk()
        win92.geometry("400x500+300+150")
        win92.configure(bg="#46A0EC")
        win92.resizable(0, 0)
        win92.title("Hint")
        df = pandas.read_csv("Cation_confirm(Hints).csv", encoding="utf-8")
        catno = list(df.loc[:, "Sr."])
        catgtest = list(df.loc[:, "CTEST"])
        cattest = list(df.loc[:, "Test"])
        dogtest=list(df.loc[:,"ATEST"])
        dogtest1 = list(df.loc[:, "Additional test"])
        b = catno.index(a)
        print(dogtest1[b])
        def thread4():
            global tosay
            if tosay._inLoop:
                tosay.endLoop()
            q = cattest[a-1].replace("dil.","dilute").replace("H2S","hydrogen sulfide").replace("NH4Cl", "ammonium chloride").replace("HNO3", "nitric acid").replace("NaOH", "sodium hydroxide")
            q=q.replace("NH4OH", "ammonium hydroxide").replace("(NH4)2CO3", "ammonium carbonate",).replace("(NH4)3PO4", "ammonium phosphate").replace("HCl","hydrochloric acid")
            q=q.replace("KI", "potassium iodide").replace("K2CrO4", "potassium chromate").replace("PPT", "precipitate").replace("(NH4)6Mo7O24", "ammonium molybdate")
            q=q.replace("K4FeCN6", "potassium ferro cyanide").replace("CH3COOH", "acetic acid").replace("(NH4)2SO4", "ammonium sulphate").replace("(NH4)2C2O4", "ammonium oxalate").replace("(NH4)3PO4", "ammonium phosphate")
            q=q.replace(" Charcoal Cavity test(Co(NO3)2)", "Perform Charcoal cavity test, that is add cobalt nitrate")
            tosay.say(q)
            tosay.runAndWait()

        t4 = threading.Thread(target=thread4)
        t4.start()
        tkinter.Label(win92, text=catgtest[b] + "\n" + cattest[b]+"\n\n"+dogtest[b]+"\n"+dogtest1[b], bg="#46A0EC", fg="white", font="Calibri 20 bold",
                      wraplength=250, justify="center").pack(pady=10)
    def wettest1():
        def thread6():
            global tosay
            if tosay._inLoop:
                tosay.endLoop()
            q = str(threading.current_thread().getName()).replace("PPT", "precipitate")
            tosay.say(q)
            tosay.runAndWait()

        def thread7():
            global tosay
            if tosay._inLoop:
                tosay.endLoop()
            q = "Please Boil The Solution"
            tosay.say(q)
            tosay.runAndWait()

        if a==1:
            global am, needed
            am=ad.get()
            if obj.wettest()== False:
                messagebox.showinfo("No Change", "No change observed")
            else:
                tkinter.Label(text="Yellow PPT Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Yellow PPT Observed")
                t6.start()
                global img2
                img2=PhotoImage(file="Pb confirmatory.png")
                tkinter.Label(win9,image=img2).pack()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI","PbCrO4","lead chromate"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"]="disabled"
        if a==2:
            global bc
            global bh
            bc = ad.get()
            if obj.wettest() == False:
                messagebox.showinfo("No Change","No change observed")
            elif obj.wettest() and obj.NH4OH(bc)==True:
                tkinter.Label(text="Deep Blue Solution Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Deep Blue Solution Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["Tetrammine copper dinitrate","[Cu(NH3)4][NO3]2"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                fn=tkinter.Label(text="Do you want to do additional test?",bg="#46A0EC", fg="white", font="Calibri 20 bold")
                fn.pack(pady=10)
                af["state"]="disabled"
                def K4():
                    action1.destroy()
                    ad.destroy()
                    af.destroy()
                    oq.destroy()
                    fn.destroy()
                    win9.geometry("500x500")
                    action2 = tkinter.Label(text="Input Action", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                    action2.pack(pady=10)
                    ad1 = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                    ad1.pack()
                    def K4Fe():
                        bh = ad1.get()
                        if bh=="K4FeCN6":
                            tkinter.Label(text="Chocolate Brown PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack()
                            t6 = threading.Thread(target=thread6, name="Chocolate Brown PPT Observed")
                            t6.start()

                            ot["state"] = "disabled"
                        else:
                            messagebox.showinfo("No change","No change observed")
                    ot=tkinter.Button(text="Perform",bg="#46A0EC", fg="white", font="Calibri 20 bold",height=1,width=10,command=K4Fe,cursor="hand2")
                    ot.pack(pady=10)
                oq=tkinter.Button(text="Yes", bg="#46A0EC", fg="white", font="Calibri 20 bold",height=1,width=10,command=K4,cursor="hand2")
                oq.pack(pady=10)
                af["state"] = "disabled"
        if a==3:
            global bl
            bl = ad.get()
            if obj.wettest() == False:
                messagebox.showinfo("No Change", "No change observed")
            elif obj.wettest() and obj.Magnesia(bl) == True:
                tkinter.Label(text="White PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="White PPT Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["x","Mg(NH4)2AsO4"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"]="disabled"
            elif obj.wettest() and obj.NH46Mo7O24(bl) == True:
                tkinter.Label(text="Yellow PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Yellow PPT Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["ammonium asrseno molybdate","(NH4)3AsO4.MoO4)"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"] = "disabled"
        if a==4:
            global dm
            global dl
            dm = ad.get()
            if ("dil" or "dilute" in dm) and ("HCl" in dm)and ("ppt" in dm):
                action1.destroy()
                ad.destroy()
                af.destroy()
                jk = tkinter.Label(text="Input action", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                jk.pack(pady=30)
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack()
                dl = xy.get()
                def wettest2():
                    dl = xy.get()
                    if ("K4FeCN6" in dl) == True:
                        tkinter.Label(text="Dark Blue PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                        t6 = threading.Thread(target=thread6, name="Dark Blue PPT Observed")
                        t6.start()
                        op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC",fg="white", height=1, width=30, font="Calibri 20 bold")
                        needed=["ferric ferrocyanide","Fe4[Fe(CN)6]3"]
                        bonusq.place(x=15,y=15)
                        win9.geometry("500x600")
                        op.pack(pady=10)
                        jl["state"] = "disabled"
                    elif ("KSCN" in dl) == True:
                        tkinter.Label(text="Blood Red PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                        t6 = threading.Thread(target=thread6, name="Blood Red PPT Observed")
                        t6.start()
                        op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                        needed=["Ferric sulphocyanide","Fe(CNS)3"]
                        bonusq.place(x=15,y=15)
                        win9.geometry("500x600")
                        op.pack(pady=10)
                        jl["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change","No change observed")
                jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                jl.pack(pady=10)
            else:
                messagebox.showinfo("No Change", "No change observed")
        if a==5:
            global jb
            jb = ad.get()
            if obj.wettest() == False:
                messagebox.showinfo("No Change", "No change observed")
            elif obj.wettest() and obj.CC(jb) == True:
                tkinter.Label(text="Blue Mass Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Blue Mass Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"] = "disabled"
            elif obj.wettest() and obj.Lake(jb) == True:
                tkinter.Label(text="Blue PPT in Colourless Medium Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Blue PPT in Colourless Medium Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"] = "disabled"
        if a==6:
            global bk
            global bn
            bk = ad.get()
            if ("dil" or "dilute" in bk) and ("HCl" in bk) and ("PPT" in bk):
                action1.destroy()
                ad.destroy()
                af.destroy()
                jk = tkinter.Label(text="Input action", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                jk.pack(pady=30)
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack()
                bn = xy.get()
                def wettest2():
                    bn = xy.get()
                    if ("K4FeCN6" in bn) == True:
                        tkinter.Label(text="Bluish White PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack(pady=10)
                        t6 = threading.Thread(target=thread6, name="Bluish White PPT Observed")
                        t6.start()
                        op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                        needed=["lead iodide","PbI"]
                        bonusq.place(x=15,y=15)
                        win9.geometry("500x600")
                        op.pack(pady=10)
                        jl["state"] = "disabled"
                    elif ("NaOH" in bn) == True:
                        tkinter.Label(text="White PPT Soluble in Excess is Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold",wraplength=400,justify="center").pack(pady=10)
                        t6 = threading.Thread(target=thread6, name="White PPT Soluble in Excess is Observed")
                        t6.start()
                        op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                        needed=["lead iodide","PbI"]
                        bonusq.place(x=15,y=15)
                        win9.geometry("500x600")
                        op.pack(pady=10)
                        jl["state"] = "disabled"
                    else:
                        messagebox.showinfo("No change", "No change observed")

                jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", height=2, width=10,
                                    font="Calibri 20 bold", cursor="hand2")
                jl.pack(pady=10)
            else:
                messagebox.showinfo("No Change", "No change observed")
        if a==7:
            global ea
            ea = ad.get()
            if obj.wettest() == False:
                messagebox.showinfo("No Change", "No change observed")
            elif obj.wettest() and obj.KNO2(ea) == True:
                tkinter.Label(text="Yellow PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Yellow PPT Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"] = "disabled"
            elif obj.wettest() and obj.Borax(ea) == True:
                tkinter.Label(text="Blue Bead Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"] = "disabled"
        if a==8:
            global fa
            fa = ad.get()
            if obj.wettest() == False:
                messagebox.showinfo("No Change", "No change observed")
            elif obj.wettest() and obj.NH4OH(fa) == True:
                tkinter.Label(text="Bright-Red PPT Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Bright-Red PPT Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"] = "disabled"
            elif obj.wettest() and obj.Borax(fa) == True:
                tkinter.Label(text="Brown Bead in Oxidizing Flame. Grey in Reducing Flame", bg="#46A0EC", fg="white", font="Calibri 20 bold",wraplength=400,justify="center").pack()
                t6 = threading.Thread(target=thread6, name="Bright-Red PPT Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"]="disabled"
        if a==9:
            global nk
            global nl
            nk = ad.get()
            if obj.wettest()==False:
                messagebox.showinfo("No Change","No change observed")
            elif obj.wettest() and obj.NaOH(nk)== True:
                action1.destroy()
                ad.destroy()
                af.destroy()
                jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                t7 = threading.Thread(target=thread7)
                t7.start()
                jk.pack(pady=30)
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack(pady=10)
                nl = xy.get()

                def boil1():
                    nl = xy.get()
                    if obj.boil(nl) == True:
                        tkinter.Label(text="Please enter a confirmatory test", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center").pack(pady=30)
                        xy.destroy()
                        jkl.destroy()
                        jk.destroy()
                        xz = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        xz.pack(pady=10)
                        ag = xz.get()
                        def wettest2():
                            ag = xz.get()
                            if ("NaOH" in ag and ("Br" in ag or "bromine" in ag.lower()) and "water" in ag.lower()):
                                tkinter.Label(text="White PPT Turns Grey", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                                t6 = threading.Thread(target=thread6, name="White PPT Turns Grey")
                                t6.start()
                                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC",fg="white", height=1, width=30, font="Calibri 20 bold")
                                needed=["lead iodide","PbI"]
                                bonusq.place(x=15,y=15)
                                win9.geometry("500x600")
                                op.pack(pady=10)
                                jl["state"] = "disabled"
                        jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                        jl.pack(pady=10)
                    elif obj.boil(al) == False:
                        messagebox.showinfo("No Change", "No change observed")

                jkl = tkinter.Button(text="Perform", command=boil1, bg="#46A0EC", fg="white", height=2, width=10,
                                     font="Calibri 20 bold", cursor="hand2")
                jkl.pack(pady=10)
            elif obj.Borax(nk):
                tkinter.Label(text="Pink Bead in Oxiding Flame. Colourless in Reducing Flame", bg="#46A0EC", fg="white", font="Calibri 20 bold",wraplength=400,justify="center").pack(pady=10)
                t6 = threading.Thread(target=thread6, name="Pink Bead in Oxiding Flame. Colourless in Reducing Flame")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
            else:
                messagebox.showinfo("No Change","No change observed")
        if a==10:
            global ab
            global ah
            ab=ad.get()
            if obj.pre()==True:
                action1.destroy()
                ad.destroy()
                af.destroy()
                jk=tkinter.Label(text="Please boil the solution",bg="#46A0EC",fg="white",font="Calibri 20 bold")
                jk.pack(pady=30)
                t7 = threading.Thread(target=thread7)
                t7.start()
                xy = tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
                xy.pack()
                ah = xy.get()
                def boil1():
                    ah=xy.get()
                    if obj.boil(ah)==True:
                        tkinter.Label(text="Please enter a confirmatory test",bg="#46A0EC",fg="white",font="Calibri 20 bold",wraplength=400,justify="center").pack(pady=30)
                        xy.destroy()
                        jkl.destroy()
                        jk.destroy()
                        xz=tkinter.Entry(font="none 26 bold",borderwidth=5,justify='center')
                        xz.pack(pady=10)
                        ag=xz.get()
                        def wettest2():
                            ag=xz.get()
                            global needed
                            if ("K2CrO4" in ag)==True:
                                global img6
                                img6=PhotoImage(file="Ba5b1ppt.gif")
                                tkinter.Label(text="Light Yellow PPT Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack(pady=10)
                                t6 = threading.Thread(target=thread6, name="Light Yellow PPT Observed")
                                t6.start()
                                tkinter.Label(win9,image=img6).pack(pady=10)
                                win9.geometry("500x600")
                                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC",fg="white", height=1, width=30, font="Calibri 20 bold")
                                needed=["barium chromate","BaCrO4"]
                                bonusq.place(x=15,y=15)
                                win9.geometry("500x600")
                                op.pack(pady=10)
                                jl["state"]="disabled"
                            elif ("K2CrO4"in ag)==False:
                                messagebox.showinfo("No Change", "No change observed")
                        jl=tkinter.Button(text="Perform",command=wettest2,bg="#46A0EC",fg="white",height=2,width=10,font="Calibri 20 bold",cursor="hand2")
                        jl.pack(pady=10)
                    elif obj.boil(ah)==False:
                        messagebox.showinfo("No Change"," No Change Observed")
                jkl=tkinter.Button(text="Perform",command=boil1,bg="#46A0EC",fg="white",height=2,width=10,font="Calibri 20 bold",cursor="hand2")
                jkl.pack(pady=10)
            elif obj.pre()==False:
                messagebox.showinfo("No Change", "No change observed")
        if a==11:
            global ak
            global al
            ak = ad.get()
            if obj.pre() == True:
                action1.destroy()
                ad.destroy()
                af.destroy()
                jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                t7 = threading.Thread(target=thread7)
                t7.start()
                jk.pack(pady=30)
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack(pady=10)
                al = xy.get()

                def boil1():
                    al = xy.get()
                    if obj.boil(al) == True:
                        tkinter.Label(text="Please enter a confirmatory test", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center").pack(pady=30)
                        xy.destroy()
                        jkl.destroy()
                        jk.destroy()
                        xz = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        xz.pack(pady=10)
                        ag = xz.get()
                        def wettest2():
                            ag = xz.get()
                            if ("(NH4)2SO4" in ag) == True:
                                tkinter.Label(text="White PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                                t6 = threading.Thread(target=thread6, name="White PPT Observed")
                                t6.start()
                                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC",fg="white", height=1, width=30, font="Calibri 20 bold")
                                needed=["lead iodide","PbI"]
                                bonusq.place(x=15,y=15)
                                win9.geometry("500x600")
                                op.pack(pady=10)
                                jl["state"] = "disabled"
                            elif ("(NH4)2SO4" in ag) == False:
                                messagebox.showinfo("No Change", "No change observed")
                        jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                        jl.pack(pady=10)
                    elif obj.boil(al) == False:
                        messagebox.showinfo("No Change", "No change observed")

                jkl = tkinter.Button(text="Perform", command=boil1, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                jkl.pack(pady=10)
            elif obj.pre() == False:
                messagebox.showinfo("No Change", "No change observed")
        if a==12:
            global an
            global ao
            an = ad.get()
            if obj.pre() == True:
                action1.destroy()
                ad.destroy()
                af.destroy()
                jk = tkinter.Label(text="Please boil the solution", bg="#46A0EC", fg="white", font="Calibri 20 bold")
                t7 = threading.Thread(target=thread7)
                t7.start()
                jk.pack(pady=30)
                xy = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                xy.pack(pady=10)
                ao = xy.get()

                def boil1():
                    ao = xy.get()
                    if obj.boil(ao) == True:
                        tkinter.Label(text="Please enter a confirmatory test", bg="#46A0EC", fg="white",font="Calibri 20 bold", wraplength=400, justify="center").pack(pady=30)
                        xy.destroy()
                        jkl.destroy()
                        jk.destroy()
                        xz = tkinter.Entry(font="none 26 bold", borderwidth=5, justify='center')
                        xz.pack(pady=10)
                        ag = xz.get()
                        def wettest2():
                            ag = xz.get()
                            if ("Ammonium Oxalate" in ag or "(NH4)2C2O4" in ag) == True:
                                tkinter.Label(text="White PPT Observed", bg="#46A0EC", fg="white",font="Calibri 20 bold").pack(pady=10)
                                t6 = threading.Thread(target=thread6, name="White PPT Observed")
                                t6.start()
                                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC",fg="white", height=1, width=30, font="Calibri 20 bold")
                                needed=["lead iodide","PbI"]
                                bonusq.place(x=15,y=15)
                                win9.geometry("500x600")
                                op.pack(pady=10)
                                jl["state"] = "disabled"
                            elif ("Ammonium Oxalate" in ag or "(NH4)2C2O4" in ag) == False:
                                messagebox.showinfo("No Change", "No change observed")
                        jl = tkinter.Button(text="Perform", command=wettest2, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                        jl.pack(pady=10)
                    elif obj.boil(ao) == False:
                        messagebox.showinfo("No Change","No change observed")
                jkl = tkinter.Button(text="Perform", command=boil1, bg="#46A0EC", fg="white", height=2, width=10,font="Calibri 20 bold", cursor="hand2")
                jkl.pack(pady=10)
            elif obj.pre() == False:
                messagebox.showinfo("No Change", "No change observed")
        if a==13:
            global ga
            ga = ad.get()
            if obj.wettest() == False:
                messagebox.showinfo("No Change", "No change observed")
            else:
                tkinter.Label(text="Pink Mass Observed", bg="#46A0EC", fg="white", font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Pink Mass Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"] = "disabled"

        if a==14:
            global aj
            aj=ad.get()
            if obj.wettest()== False:
                messagebox.showinfo("No Change","No change observed")
            else:
                tkinter.Label(text="Brown PPT Observed",bg="#46A0EC",fg="white",font="Calibri 20 bold").pack()
                t6 = threading.Thread(target=thread6, name="Brown PPT Observed")
                t6.start()
                op = tkinter.Button(text="Proceed to guess the cation--->", command=guess, bg="#46A0EC", fg="white",height=1, width=30, font="Calibri 20 bold")
                needed=["lead iodide","PbI"]
                bonusq.place(x=15,y=15)
                win9.geometry("500x600")
                op.pack(pady=10)
                af["state"]="disabled"

    af=tkinter.Button(text="Perform",command=wettest1,bg="#46A0EC",fg="white",height=2,width=10,font="Calibri 20 bold",cursor="hand2")
    af.pack(pady=20)
    global helpme
    if counter==1:
        helpme=PhotoImage(file="Disabled question.png")
        hintbutton = tkinter.Button(bg="#46A0EC", borderwidth=3, cursor="hand2", image=helpme)
        hintbutton.place(x=450, y=15)
    elif counter==0:
        helpme=PhotoImage(file="Hintlogoimg.png")
        hintbutton=tkinter.Button(bg="#46A0EC",borderwidth=3,cursor="hand2",image=helpme,command=Hint)
        hintbutton.place(x=450, y=15)