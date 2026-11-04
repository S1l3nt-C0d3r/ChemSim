# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Ni(cation):
    colour="green "
    fcolour="Silver-white"
    gpc="Black"
    i=0
    @classmethod
    def Borax(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.fa
        if ("borax bead" in ax.lower() and "ppt" in ax.lower()):
            return True
        else:
            return False
    @classmethod
    def NH4OH(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.fa
        if ("NH4OH" in ax and "dimethyl glyoxime" in ax.lower() and "os" in ax.lower()):
            return True
        else:
            return False
    @classmethod
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.fa
        if( (not Ni.Borax(ax) )and (not Ni.NH4OH(ax))):
            return False
        if Ni.NH4OH(ax):
            return True
        elif Ni.Borax(ax):
            return True
 