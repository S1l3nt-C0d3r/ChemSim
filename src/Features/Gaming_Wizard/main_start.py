import winsound
from tkinter import *
import pyttsx3 as sound
import threading
import time
global t
import sys
def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import SYMBOL
            SYMBOL.main()
        elif args == 2:
            from Options import MASSNUM
            MASSNUM.main()
        elif args == 3:
            from Options import JUM_NM
            JUM_NM.main()
        elif args == 4:
            from Options import JUM_M
            JUM_M.main()
        elif args == 5:
            from Options import COMPOUND
            COMPOUND.main()
        elif args == 6:
            from Options import PH
            PH.main()
        elif args == 7:
            from Options import RADICALS
            RADICALS.main()            
        elif args == 8:
            from Options import IUPAC1
            IUPAC1.main()
        elif args == 9:
            from Options import GROUP
            GROUP.main()
    def option():
        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#63cdda',
            border=0,
            justify='center',

        )
        sel_btn1 = Button(
            text="element symbols",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="atomic mass",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="non-metals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(3),
        )
        global img10
        img10 = PhotoImage(file="guessthename.png")
        sel_btn1 = Button(
            image=img10,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(1),
        )
        global img9
        img9 = PhotoImage(file="massteria.png")
        sel_btn2 = Button(
            image=img9,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(2),
        )
        global img8
        img8 = PhotoImage(file="scramblenonmetals.png")
        sel_btn3 = Button(
            image=img8,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(3),
        )
        global img7
        img7 = PhotoImage(file="scramblemetals.png")
        sel_btn4 = Button(
            image=img7,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(4),
        )
        global img6
        img6 = PhotoImage(file="togetherwebond.png")
        sel_btn5 = Button(
            image=img6,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(5),
        )
        global img5
        img5 = PhotoImage(file="What's My Nature-1.png")
        sel_btn6 = Button(
            image=img5,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(6),
        )
        global img4
        img4 = PhotoImage(file="guesstheradical.png")
        sel_btn7 = Button(
            image=img4,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        global img3
        img3=PhotoImage(file="nameme.png")
        sel_btn8 = Button(
            image=img3,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(8),
        )
        global img2
        img2=PhotoImage(file="whatsmyaddress1.png")
        sel_btn9 = Button(
            image=img2,
            fg="#000000",
            bg="#63cdda",
            cursor="hand2",
            command=lambda: start_game(9),
        )


        sel_btn1.grid(row=1, column=1, pady=(50), padx=(55))
        sel_btn2.grid(row=1, column=2, pady=(50), padx=(55))
        sel_btn3.grid(row=1, column=3, pady=(50), padx=(55))
        sel_btn4.grid(row=2, column=1, pady=(50), padx=(55))
        sel_btn5.grid(row=2, column=2, pady=(50), padx=(55))
        sel_btn6.grid(row=2, column=3, pady=(50), padx=(55))
        sel_btn7.grid(row=3, column=1, pady=(50), padx=(55))
        sel_btn8.grid(row=3, column=2, pady=(50), padx=(55))
        sel_btn9.grid(row=3, column=3, pady=(50), padx=(55))
       

    def show_option():
        start_btn.destroy()
        main_window.geometry("800x800+380+50")
        lab_img.destroy()
        option()
    main_window = Tk()

    main_window.geometry("500x700+500+100")
    main_window.resizable(0,0)
    main_window.title("Gaming Wizard")
    main_window.configure(background="#63cdda")
    main_window.iconbitmap(r'quizee_logo_.ico')

    img0 = PhotoImage(file="gaming wizard-1k.png")
    img1 = PhotoImage(file="back.png")
    img2 = PhotoImage(file="play.png")
    lab_img = Label(
        main_window,
        image=img0,
        bg='#63cdda',
    )

    lab_img.place(x=50,y=10)
    global tosay
    sp = ""
    tosay = sound.init()
    def thread1():
        global tosay
        if tosay._inLoop:
            tosay.endLoop()
        tosay.say("Welcome to Gaming Wizard")
        tosay.runAndWait()
        if tosay._inLoop:
            tosay.endLoop()
    t1 = threading.Thread(target=thread1)
    t1.start()
    def music():
        time.sleep(1.4)
        winsound.PlaySound("GameMusic.WAV",winsound.SND_LOOP+winsound.SND_ASYNC)

    t2 = threading.Thread(target=music)
    t2.start()
    start_btn = Button(
        main_window,
        bg="#63cdda",
        borderwidth=10,
        cursor="hand2",
        image=img2,
        command=show_option,
    )
    start_btn.place(x=140, y=430)

    main_window.mainloop()
    if sys.exit():
        winsound.PlaySound(None, winsound.SND_PURGE)
