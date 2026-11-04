

from tkinter import *
from random import *
from tkinter import messagebox
import time
import pandas as p
df=p.read_csv("PHgame.csv")


forPH_WORD= list(df.loc[:,'Name'])



forPH_ANSWER =list(df.loc[:,'pH'])
ran_num = randrange(0, (len(forPH_WORD)))
jumbled_rand_word = forPH_WORD[ran_num]
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
points = 0
global x
x=0

def main():
    def back():
        global points
        fs = dict(database.child("Users").child(str(ap)).get().val())
        if points > fs["g6"]:
            toadd = {"g6": points}
            database.child("Users").child(str(ap)).update(toadd)
        points = 0
        my_window.destroy()
        import Gaming_Wizard.main_start as main_start
        main_start.start_main_page()

    def change():
        global ran_num,x
        ran_num = randrange(0, (len(forPH_WORD)))
        word.configure(text=forPH_WORD[ran_num])
        
        ans_lab.configure(text="")
        x=0

    def GT7():
        global ran_num, points, x
        print(forPH_ANSWER[ran_num])
        if forPH_ANSWER[ran_num]=="pH Greater Than 7":
            if (x==0):        
                points += 5
                score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(forPH_WORD)))
            word.configure(text=forPH_WORD[ran_num])
            
            ans_lab.configure(text="")
            ans["state"]="normal"
            x=0
            
        else:
            x=1
            messagebox.showerror("Error", "Incorrect Answer..Try your best!")

        
    def LT7():
        global ran_num, points, x
        print(forPH_ANSWER[ran_num])
        if forPH_ANSWER[ran_num]=="pH Less Than 7":
            if (x==0):        
                points += 5
                score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(forPH_WORD)))
            word.configure(text=forPH_WORD[ran_num])
            
            ans_lab.configure(text="")
            ans["state"]="normal"
            x=0
        else:
            x=1
            messagebox.showerror("Error", "Incorrect Answer..Try your best!")
        
    def ET7():
        global ran_num, points, x
        print(forPH_ANSWER[ran_num])
        if forPH_ANSWER[ran_num]=="pH Equal to 7":
            if (x==0):        
                points += 5
                score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(forPH_WORD)))
            word.configure(text=forPH_WORD[ran_num])
            
            ans_lab.configure(text="")
            ans["state"]="normal"
            x=0
        else:
            x=1
            messagebox.showerror("Error", "Incorrect Answer..Try your best!")
        
    def show_answer():
        global points,x
        
        if points > 4:
            
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=forPH_ANSWER[ran_num])
            ans["state"]="disabled"
            x=1
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x600+500+150")
    my_window.resizable(0, 0)
    my_window.title("What's My Nature?")
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
        pady=0,
        bg="#63cdda",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=forPH_WORD[ran_num],
        pady=1,
        bg="#63cdda",
        wraplength=400,
        justify="center",
        fg="#000000",
        font="Titillium 25 bold"
    )
    word.pack()


    submit1 = Button(
        text="pH Less Than 7",
        width=18,
        #height=1,
        borderwidth=8,
        fg="#000000",
        bg="#63cdda",
        pady=1,
        font=("", 13),
        command=LT7,
    )
    submit1.pack(pady=(10,20))
    
    submit2 = Button(
        text="pH Greater Than 7",
        width=18,
        #height=1,
        borderwidth=8,
        fg="#000000",
        bg="#63cdda",
        pady=1,
        font=("", 13),
        command=GT7,
    )
    submit2.pack(pady=(10,20))
    
    submit3 = Button(
        text="pH Equal To 7",
        width=18,
        #height=1,
        borderwidth=8,
        fg="#000000",
        bg="#63cdda",
        pady=1,
        font=("", 13),
        command=ET7,
    )
    submit3.pack(pady=(10,20))
    
    change = Button(
        text="Change Word",
        width=18,
        #height=1,
        borderwidth=8,
        fg="#000000",
        bg="#63cdda",
        pady=1,
        font=("", 13),
        command=change,
    )
    change.pack(pady=(10,20))
    
    ans = Button(
        text="Answer",
        width=18,
        #height=1,
        borderwidth=8,
        fg="#000000",
        bg="#63cdda",
        pady=1,
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(10,20))

    ans_lab = Label(
        text="",
        bg="#63cdda",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
