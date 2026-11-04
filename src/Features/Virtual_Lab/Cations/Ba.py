# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
import tkinter

from src.Virtual_Lab.Cations.cation import cation


class Ba(cation):
    colour = "White "
    fcolour = "Light Green/Apple Green"
    gpc = "White"
    i = 0

    def K2CrO4(s1):

        if ("K2CrO4" in s1):
            return True
        else:
            return False

    def choose(self):
        print("Do you want to take make your Decision? Y/N")
        a = input()
        if a == 'Y':
            return True
        else:
            return False

    def wettest(self):
        if Ba.K2CrO4():
            return True
        else:
            return False

    def pre(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.ab
        print (ax)
        if ("dil" in ax.lower() and "ppt" in ax.lower() and ("acetic acid" in ax.lower() or "CH3COOH" in ax)):
            return True
        else:
            return False
        
        
    