import sys
import tkinter
import winsound
sys.path.insert(1,"D://OneDrive//sarvaarth//School//RFS//Year 11//Chemistry//Srijan//Chemistry Wizard//main_start.py")
from tkinter import *
from random import *
from tkinter import ttk
from tkinter import messagebox
import time
import pandas as p
df=p.read_csv("group.csv")
global x
x=0
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
ANS1 = list(df.loc[:,'Gnew'])
ANS2 = list(df.loc[:,'Gold'])
E_NAME = list(df.loc[:,'Name'])
P_NAME = list(df.loc[:,'Pno'])
ran_num = randrange(0, (len(E_NAME)))

jumbled_rand_word = E_NAME[ran_num]
# print(jumbled_rand_word)
points = 0


def main():
    global t
    
    def back():
        winsound.PlaySound(None,winsound.SND_PURGE)
        global points
        fs = dict(database.child("Users").child(str(ap)).get().val())
        if points > fs["g9"]:
            toadd = {"g9": points}
            database.child("Users").child(str(ap)).update(toadd)
        points=0
        my_window.destroy()
        import Gaming_Wizard.main_start as main_start
        main_start.start_main_page()

    def change():
        global ran_num,x
        ran_num = randrange(0, (len(E_NAME)))
        word.configure(text=E_NAME[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
        x=0

    def cheak():
        global points, ran_num, x, t
        t=setter.get()
        user_word = get_input.get()
        print(ANS1[ran_num])
        print(ANS2[ran_num])
        print(type(P_NAME[ran_num]))
        print(user_word == ANS1[ran_num])
        print(user_word == ANS2[ran_num])
        print(type(t))
        if (user_word.strip() == str(ANS1[ran_num]) or user_word.strip() == ANS2[ran_num]) and int(t)==(P_NAME[ran_num]):
            if (x==0):        
                points += 5
                score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Corrected Answer.. Keep it Up!")
            ran_num = randrange(0, (len(E_NAME)))
            word.configure(text=E_NAME[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
            x=0
            ans["state"]="normal"
        else:
            
            messagebox.showerror("Error", "Incorrect Answer..Try your best!")
            x=1
            
            get_input.delete(0, END)

    def show_answer():
        global points, x
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            tkinter.Label(text=((("Group: "+str(ANS1[ran_num])))+("\nPeriod: "+str(P_NAME[ran_num]))),font="none 15 bold",bg="#63cdda").place(y=580,x=205)
            x=1
            ans["state"]="disabled"
        else:
            ans_lab.configure(text='Not enough points')
    def tosend(e):
        cheak()  
    my_window = Tk()
    my_window.geometry("500x650+500+150")
    my_window.resizable(0, 0)
    my_window.title("What's My Address?")
    my_window.configure(background="#63cdda")
    my_window.iconbitmap(r'quizee_logo_.ico')
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#63cdda',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10,padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#63cdda",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=E_NAME[ran_num],
        pady=10,
        bg="#63cdda",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word.pack()
    tkinter.Label(text="Group:",font="none 15 bold",bg="#63cdda").pack()
    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()
    tkinter.Label(text="Period:",font="none 15 bold",bg="#63cdda").pack()
    setter= StringVar()
    setter.set(P_NAME[0])
    drop =ttk.Combobox(my_window,textvariable=setter,font="Calibri 20 bold",justify="center")
    drop['values']=["1","2","3","4","5","6","7"]
    drop['state']='readonly'
    drop.pack(pady=10,padx=10)
    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#63cdda",
        command=cheak,
    )
    submit.pack(pady=(10,20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#63cdda",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#63cdda",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#63cdda",
        fg="#000000",
        font="Courier 15 bold",
    )
    time = Label(

        pady=10,
        bg="#63cdda",
        fg="#000000",
        font="Titillium  50 bold"
    )
    time.pack()
    ans_lab.pack()
    my_window.bind("<Return>",tosend)
    my_window.mainloop()
