import pyrebase
config={
  "apiKey": "AIzaSyD_U2sGJigAYECFQmOQNdfu5s-Ybh3B5W0",
  "authDomain": "chemsimdb.firebaseapp.com",
  "projectId": "chemsimdb",
  "databaseURL":"https://chemsimdb-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "chemsimdb.appspot.com",
  "messagingSenderId": "862153368955",
  "appId": "1:862153368955:web:0cd213e8dce22ec75d49de",
  "measurementId": "G-PEBEQEN5FC"
        }
firebase=pyrebase.initialize_app(config)
database=firebase.database()
import tkinter
from tkinter import *
import tkinter.messagebox
global ID
global ap
def mainLogin():
    def Login():
        global ap
        win100.destroy()
        def signlog():
            win101=Tk()
            global backimg
            global logbutton
            backimg = PhotoImage(file="background.png")
            tkinter.Label(image=backimg).pack()
            logbutton = PhotoImage(file="LOGIN.png")
            win101.geometry("500x500+500+150")
            win101.configure(bg="#46A0EC")
            win101.resizable(0, 0)
            def logen():
                global ap
                global checklogin
                checklogin=0
                ap=kd.get()
                kp=pd.get()
                try:
                    fs = dict(database.child("Users").child(str(ap)).get().val())
                    print(fs)
                    if kp== fs["Password"]:
                        tkinter.messagebox.showinfo("Welcome",("Welcome", fs["Fname"]))
                        checklogin=1
                    else:
                        tkinter.messagebox.showerror("Incorrect ID", "Incorrect ID entered")
                except:
                    tkinter.messagebox.showerror("Incorrect ID", "Incorrect ID entered")
                if checklogin==1:
                    win101.destroy()
                    Action()
            tkinter.Label(win101,text="Username",bg="#E4F0FE",fg="#303952",font="Calibri 20 bold").place(y=40, x=190)
            kd = tkinter.Entry(win101, font="none 26 bold", borderwidth=5, width=18, justify='center')
            kd.place(y=90, x=80)
            tkinter.Label(win101, text="Password", bg="#E4F0FE", fg="#303952", font="Calibri 20 bold").place(y=160,x=190)
            pd = tkinter.Entry(win101, font="none 26 bold",show='*', borderwidth=5, width=18, justify='center')
            pd.place(y=210,x=80)
            og = tkinter.Button(win101, image=logbutton, command=logen, bg="#E4F0FE", fg="white",font="Calibri 20 bold",cursor="hand2")
            og.place(y=320,x=170)
        signlog()
    def SignUp():
        global checklog
        global backimg
        global signbutton
        checklog=0
        win100.destroy()
        win103 = Tk()
        signbutton = PhotoImage(file="Signup.png")
        backimg = PhotoImage(file="background.png")
        win103.geometry("500x500+500+150")
        win103.configure(bg="#46A0EC")
        win103.resizable(0, 0)
        tkinter.Label(win103,image=backimg).pack()
        tkinter.Label(win103, text="Username", bg="#E4F0FE", fg="#303952", font="Calibri 20 bold").place(y=210,x=190)
        kd = tkinter.Entry(win103, font="none 26 bold", borderwidth=5, width=18, justify='center')
        kd.place(y=250,x=80)
        tkinter.Label(win103, text="Password", bg="#E4F0FE", fg="#303952", font="Calibri 20 bold").place(y=305,x=190)
        pd = tkinter.Entry(win103, font="none 26 bold",show='*', borderwidth=5, width=18, justify='center')
        pd.place(x=80,y=340)
        tkinter.Label(win103, text="First name", bg="#E4F0FE", fg="#303952", font="Calibri 20 bold").place(y=10,x=190)
        fd = tkinter.Entry(win103, font="none 26 bold", borderwidth=5, width=18, justify='center')
        fd.place(x=80,y=55)
        tkinter.Label(win103, text="Last name", bg="#E4F0FE", fg="#303952", font="Calibri 20 bold").place(y=110,x=190)
        gd = tkinter.Entry(win103, font="none 26 bold", borderwidth=5, width=18, justify='center')
        gd.place(x=80,y=155)
        def sign():
            global checklog
            global ap
            ap=kd.get()
            try:
                fs = dict(database.child("Users").child(str(ap)).get().val())
                print(fs)
                tkinter.messagebox.showerror("User exists","User already exists, please try again")
            except:
                toadd = {"ID": ap, "Password": pd.get(), "Fname": fd.get(), "Lname": gd.get(), "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0,
                         "g6": 0, "g7": 0, "g8": 0, "g9": 0}
                database.child("Users").child(str(ap)).set(toadd)
                tkinter.messagebox.showinfo("Success","Sign-up successful. Enjoy Chemsim :)")
                checklog=1
            if checklog==1:
                win103.destroy()
                import main
                main.frun()
        og = tkinter.Button(win103, image=signbutton, command=sign, bg="#E4F0FE", fg="white", font="Calibri 20 bold", cursor="hand2")
        og.place(x=170,y=400)

    def Action():
            import main
            main.frun()
    win100 = Tk()
    win100.geometry("500x500+500+150")
    win100.configure(bg="#46A0EC")
    win100.resizable(0, 0)
    win100.title("Gaming wiard------>login")
    global backimg
    global logbutton
    global signbutton
    backimg=PhotoImage(file="background.png")
    tkinter.Label(image=backimg).pack()
    logbutton=PhotoImage(file="LOGIN.png")
    signbutton=PhotoImage(file="Signup.png")
    label1 = tkinter.Label(text="Welcome to Chemsim", bg="#E4F0FE", fg="#303952", font="Titillium  30 bold")
    label1.place(x=50, y=40)
    login1 = tkinter.Button(text="Login", image=logbutton, bg="#E4F0FE", font="Titillium  20 bold",command=Login)
    login1.place(x=70, y=200)
    sign1 = tkinter.Button(text="Sign up", image=signbutton, bg="#E4F0FE", font="Titillium  20 bold", command=SignUp)
    sign1.place(x=280, y=200)
    win100.mainloop()



