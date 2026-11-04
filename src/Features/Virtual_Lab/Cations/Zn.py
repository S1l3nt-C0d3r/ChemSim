# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Zn(cation):
    colour="Colourless"
    fcolour="Colourless"
    gpc="White"
    

    @classmethod
    def K4FeCN6(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.dk
        if ("K4FeCN6" in ax and ("sol" in ax.lower() or "solution" in ax.lower())):
            return True
        else:
            return False
    @classmethod
    def NaOH(self,ac):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.dk
        if ("NaOH" in ax ):
            return True
        else:
            return False
    @classmethod
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.dk
        if( (not Zn.K4FeCN6(ax) )and (not Zn.NaOH(ax))):
            return False
        elif Zn.K4FeCN6(ax): return True
        elif Zn.NaOH(ax): return True
            
        
    
