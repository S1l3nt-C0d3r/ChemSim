import tkinter
from tkinter import *
def frun():
 win1=Tk()
 win1.wm_attributes('-transparentcolor', '#ab23ff')
 def openstats():
   win1.destroy()
   import Home.statspage as statspage
   statspage.startstat()
 def openViva():
  win1.destroy()
  import Assess_Thyself.vivastart as vivastart
 def openGame():
  win1.destroy()
  import Gaming_Wizard.main_start as main_start
  main_start.start_main_page()
 def openSalt():
  win1.destroy()
  import src.Virtual_Lab.SaltAnalysis as SaltAnalysis
  SaltAnalysis.srun()
 def openLearn():
  win1.destroy()
  import Infomania.elements as elements
 statsbutton= PhotoImage(file="check_stats.png")
 virtualbutton = PhotoImage(file="virtual lab button.png")
 gamebutton = PhotoImage(file="gaming wizard-1k(button).png")
 infobutton=PhotoImage(file="infomania bu.png")
 background=PhotoImage(file="background13.png")
 vivabutton=PhotoImage(file="Viva Voce-1.png")
 tkinter.Label(image=background).pack()
 game = tkinter.Button(text="Game",command=openGame,image=gamebutton,bg="#E4F0FE",cursor="hand2")
 game.place(x=25,y=100)
 salt = tkinter.Button(text=("Virtual Lab"),bg="#E4F0FE",image=virtualbutton,command=openSalt,cursor="hand2")
 salt.place(x=270,y=100)
 learn = tkinter.Button(text=("InfoMania"),bg="#E4F0FE",image=infobutton,command=openLearn,cursor="hand2")
 learn.place(x=25,y=340)
 viva=tkinter.Button(image=vivabutton,command=openViva,bg="#E4F0FE")
 viva.place(x=270,y=340)
 stats = tkinter.Button(image=statsbutton, bg="#E4F0FE", command=openstats)
 stats.place(x=390, y=10)
 win1.geometry("500x600+500+150")
 win1.resizable(0,0)
 win1.title("ChemSim")
 win1.mainloop()