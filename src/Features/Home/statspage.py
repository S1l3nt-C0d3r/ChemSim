import tkinter
from tkinter import *
import mysql.connector as c
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
global ap
import Services.ConsoleDB as ConsoleDB
from Services.ConsoleDB import ap
global statsimg
def startstat():
    win107=Tk()
    win107.geometry("500x500+500+150")
    win107.resizable(0,0)
    win107.title("ChemSim----> Stats")
    global statsimg
    statsimg = PhotoImage(file="background.png")
    fs= dict(database.child("Users").child(str(ap)).get().val())
    tkinter.Label(win107,image=statsimg).pack()
    ab = tkinter.Label(text=("Welcome "+(fs["Fname"])),bg="#E4F0FE", fg="#303952",font="Calibri 20 bold")
    ab.place(x=160, y=10)
    am=tkinter.Label(text="Let's take a look at your stats!",bg="#E4F0FE", fg="#303952",font="Calibri 20 bold")
    am.place(x=90, y=40)
    tkinter.Label(text="Guess The Name: "+str(fs["g1"]),bg="#E4F0FE", fg="#303952",font="Calibri 11 bold").place(x=20,y=120)
    tkinter.Label(text="Mass-Teria: "+str(fs["g2"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=200, y=120)
    tkinter.Label(text="Scramble(Metals): "+str(fs["g3"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=350, y=120)
    tkinter.Label(text="Scramble(Non-Metals): "+str(fs["g4"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=20, y=220)
    tkinter.Label(text="Together We Bond: "+str(fs["g5"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=200, y=220)
    tkinter.Label(text="What's My Nature: "+str(fs["g6"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=350, y=220)
    tkinter.Label(text="Guess The Radical: "+str(fs["g7"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=20, y=320)
    tkinter.Label(text="Name Me: "+str(fs["g8"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=200, y=320)
    tkinter.Label(text="What's My Address: "+str(fs["g9"]), bg="#E4F0FE", fg="#303952", font="Calibri 11 bold").place(x=350, y=320)
    def back():
        import main
        win107.destroy()
        main.frun()
    backimg = PhotoImage(file="back.png")
    backbutton = tkinter.Button(win107, image=backimg, bg="#E4F0FE", command=back)
    backbutton.place(x=15, y=15)
    win107.mainloop()
startstat()