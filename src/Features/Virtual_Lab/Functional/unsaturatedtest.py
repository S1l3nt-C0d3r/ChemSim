import tkinter
from tkinter import *
from src.Virtual_Lab.Functional.allclasses import ketone
from src.Virtual_Lab.Functional.allclasses import phenol
from src.Virtual_Lab.Functional.allclasses import COOH
from src.Virtual_Lab.Functional.allclasses import CHO
from src.Virtual_Lab.Functional.allclasses import amine
from src.Virtual_Lab.Functional.allclasses import OH
import random as r

a = r.randint(1, 6)
a = 2
if a == 1:
    obj = COOH()
elif (a == 2):
    obj = phenol()
elif (a == 3):
    obj = CHO()
elif (a == 4):
    obj = ketone()
elif (a == 5):
    obj = amine()
elif (a == 6):
    obj = OH()
win22 = Tk()
tkinter.Label(text="Input an Action").pack()
yl=tkinter.Entry()
yl.pack()
ym=yl.get()
def tester():
    ym=yl.get()
    if (not obj.KMnO4(ym) and (not obj.Bwater(ym))):
        tkinter.Label(text="No Change").pack()
    elif obj.Bwater(ym):
        tkinter.Label(text="Brown colour decolorises").pack()

    elif obj.KMnO4(ym):
        tkinter.Label(text="Pink Colour Decolourises").pack()
yn=tkinter.Button(text="Perform",command=tester)
yn.pack()

