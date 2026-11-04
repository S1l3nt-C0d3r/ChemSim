from tkinter import *
from random import *
from tkinter import messagebox
import time
import pandas as p
global x, L1,L2, ran_num
L2=["nil","un","bi","tri","quad","pent","hex","sept","oct","enn"]
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
ran_num = randrange(100,200)

# print(jumbled_rand_word)
points = 0

def genans(b):
    if b==100:
        return "fermium"
    global L2
    a=b
    ans=""
    for i in str(a):
        ans=ans+L2[int(i)]
    ans=ans+"ium"
    ans=ans.replace("nnn","nn")
    ans=ans.replace("ii","i")
    return ans


def main():
    
    def back():
        global points
        fs = dict(database.child("Users").child(str(ap)).get().val())
        if points > fs["g8"]:
            toadd = {"g8": points}
            database.child("Users").child(str(ap)).update(toadd)
        points=0
        my_window.destroy()
        import Gaming_Wizard.main_start as main_start
        main_start.start_main_page()

    def change():
        global ran_num,x
        ran_num = randrange(100,200)
        word.configure(text=ran_num)
        get_input.delete(0, END)
        ans_lab.configure(text="")
        x=0

    def cheak():
        global points, ran_num, x
        #print(x)
        print(ran_num)
        user_word = get_input.get()
        print(ran_num)
        print(genans(ran_num))
        if user_word.strip() == genans(ran_num):
            if (x==0):        
                points += 5
                score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            
            ran_num = randrange(100,200)
            word.configure(text=ran_num)
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
            time.sleep(0.5)
            ans_lab.configure(text=genans(ran_num))
            x=1
            ans["state"]="disabled"
        else:
            ans_lab.configure(text='Not enough points')
    def tosend(e):
        cheak()   
    def openhelpsection():
        popupwindow=Tk()
        popupwindow.title("Information")
        popupwindow.configure(bg="#63cdda")
        popupwindow.geometry("700x700+700+100")
        data = {'Digit Present in Atomic Number': ['0','1','2','3','4','5', '6','7','8', '9'], 'Numerical Root': ["nil","un","bi","tri","quad","pent","hex","sept","oct","enn"]}
        df = p.DataFrame(data) 
        T1=Label(popupwindow,text="1.The name of an element should be derived directly from its atomic number using the following numerical roots ", justify="left",wraplength=500,bg="#63cdda",font="Calibri 14 bold")
        T2=Label(popupwindow,text=df.to_string(index=False),bg="#63cdda",font="Calibri 14 bold",justify="center")
        T3=Label(popupwindow,text="2.The roots should be written together in the order of the digits present in the atomic number and should be terminated by the suffix ‘ium\n3. If ‘enn’ occurs before ‘nil’ the second  ‘n’ of ‘enn’ should be dropped\n4. Similarly the final ‘i’ of ‘bi’ and ‘tri’ should be dropped when they occur before ium.", justify="left",wraplength=500,bg="#63cdda",font="Calibri 14 bold")
        T4=Label(popupwindow,text="Eg. \nAtomic Number-105,  Name- unnilpentium \nAtomic Number-113,  Name- ununtrium",bg="#63cdda",font="Calibri 14 bold",justify="left",wraplength=500)
        T1.pack()
        T2.pack()
        T3.pack()
        T4.pack()
        b_end=Button(popupwindow, text="OK",command=popupwindow.destroy,bg="#63cdda",font="Calibri 15 bold",width=10,height=2)
        b_end.pack(pady=10)
        popupwindow.mainloop()

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Name Me!")
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
        text=ran_num,
        pady=10,
        bg="#63cdda",
        fg="#000000",
        font="Titillium  50 bold"
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
    helpme = PhotoImage(file="info.png")
    helpbtn = Button(
        my_window,
        bg="#63cdda",
        borderwidth=3,
        cursor="hand2",
        image=helpme,
        command=openhelpsection,
    )
    helpbtn.place(x=450, y=15)
    my_window.bind("<Return>",tosend)
    my_window.mainloop()
