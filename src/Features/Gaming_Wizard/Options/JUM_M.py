from tkinter import *
from random import *
from tkinter import messagebox
import time
import random


JUM_M_ANSWER = ['lithium','beryllium','sodium','magnesium','aluminium','potassium','calcium','scandium','titanium',
                 'vanadium','chromium','manganese','iron','cobalt','nickel','copper','zinc','gallium','rubidium']


JUM_M_WORD=[]

global x
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

x=0
def listtostring(str):
    str1=""
    return(str1.join(str))
for i in range(len(JUM_M_ANSWER)):
    word=JUM_M_ANSWER[i]
    word0=''
    i=0
    l=list(word)
    random.shuffle(l)
    #print(listtostring(l))
    JUM_M_WORD.append(listtostring(l))



ran_num = randrange(0, (len(JUM_M_WORD)))
jumbled_rand_word = JUM_M_WORD[ran_num]

points = 0


def main():
    def back():
        global points
        fs = dict(database.child("Users").child(str(ap)).get().val())
        if points > fs["g4"]:
            toadd = {"g4": points}
            database.child("Users").child(str(ap)).update(toadd)
        points=0
        my_window.destroy()
        import Gaming_Wizard.main_start as main_start
        main_start.start_main_page()

    def change():
        global ran_num,x
        ran_num = randrange(0, (len(JUM_M_WORD)))
        word.configure(text=JUM_M_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
        x=0

    def cheak():
        global points, ran_num, x
        user_word = get_input.get().lower()
        if user_word == JUM_M_ANSWER[ran_num]:
            if (x==0):        
                points += 5
                score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(JUM_M_WORD)))
            word.configure(text=JUM_M_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
            x=0
            ans["state"]="normal"
        else:
            x=1
            messagebox.showerror("Error", "Incorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points, x
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=JUM_M_ANSWER[ran_num])
            x=1
            ans["state"]="disabled"
        else:
            ans_lab.configure(text='Not enough points')
    def tosend(e):
        cheak() 
    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Unscramble Metals")
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
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#63cdda",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=JUM_M_WORD[ran_num],
        pady=10,
        bg="#63cdda",
        fg="#000000",
        font="Titillium  30 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

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
    ans_lab.pack()
    my_window.bind("<Return>",tosend)
    my_window.mainloop()
