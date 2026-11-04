# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Mn(cation):
    colour="Pale Pink"
    fcolour="Yellowish green"
    gpc="Flesh Coloured"
    i=0

    @classmethod
    def Borax(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.nk
        if ("borax bead" in ax.lower() and "group" in ax.lower and "ppt"):
            return True
        else:
            return False
    @classmethod
    def NaOH(self,ac):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.nk
        if ("dil" or "dilute" in ax.lower()) and ("HCl" in ax)and ("ppt" in ax.lower()):
            return True
        else: 
            return False
    @classmethod
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.nk
        if( (not Mn.Borax(ax) )and (not Mn.NaOH(ax))):
            return False
        elif Mn.NaOH(ax):
            return True
        elif Mn.Borax(ax):
            return True
        

