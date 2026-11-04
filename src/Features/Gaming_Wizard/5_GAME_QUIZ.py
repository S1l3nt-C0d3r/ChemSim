from tkinter import *


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
            bg='#e6fff5',
            border=0,
            justify='center',

        )
        sel_btn1 = Button(
            text="Guess The Name!",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Mass-Teria!",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Scramble Non-Metals!",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Scramble Metals!",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Together We Bond!",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="What's my Nature?",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(6),
        )
        sel_btn7 = Button(
            text="Guess the Radical",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        sel_btn8 = Button(
            text="IUPAC",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(8),
        )
        sel_btn9 = Button(
            text="GROUP",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(9),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=6, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=7, column=4, pady=(10, 0), padx=50, )
        sel_btn8.grid(row=8, column=4, pady=(10, 0), padx=50, )
        sel_btn9.grid(row=9, column=4, pady=(10, 0), padx=50, )
    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("700x700+400+100")
    main_window.resizable(0, 0)
    main_window.title("Gaming Wizard")
    main_window.configure(background="#e6fff5")
    main_window.iconbitmap(r'quizee_logo_.ico')

    img0 = PhotoImage(file="quizee_logo1.png")
    img1 = PhotoImage(file="back.png")
    img2 = PhotoImage(file="play.png")
    lab_img = Label(
        main_window,
        image=img0,
        bg='#e6fff5',
    )
    lab_img.place(y=10)

    start_btn = Button(
        main_window,
        bg="#e6fff5",
        borderwidth=10,
        cursor="hand2",
        image=img2,
        command=show_option,
    )
    start_btn.place(x=140, y=250)

    main_window.mainloop()


start_main_page()
