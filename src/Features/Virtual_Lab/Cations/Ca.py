# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Ca(cation):
    colour="Colourless "
    fcolour="Brick Red"
    gpc="White"
    i=0

        
    def Ammox (s1):
        
        if ("ammonium oxalate" in s1.lower() or "(NH4)2C2O4" in s1):
            return True
        else:
            return False
    def wettest(self):
        if Ca.Ammox():
            return True
        else:
            return False
    def pre(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.an
        if ("dil" in ax.lower() and "ppt" in ax.lower() and ("acetic acid" in ax.lower() or "CH3COOH" in ax)):
            return True
        else:
            return False
        
        

