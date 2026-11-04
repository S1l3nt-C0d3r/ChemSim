# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Co(cation):
    colour="Varied "
    fcolour="Silver-white"
    gpc="Black"
    i=0
    @classmethod
    def Borax(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.ea
        if ("borax bead" in ax.lower() and "ppt" in ax.lower()):
            return True
        else:
            return False
    @classmethod
    def KNO2(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.ea
        if ("KNO2" in ax and "dil" in ax.lower() and "os" in ax.lower() and "NH4OH" in ax and ("acetic acid" in ax.lower() or "CH3COOH" in ax)):
            return True
        else:
            return False
    @classmethod
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.ea
        if( (not Co.Borax(ax) )and (not Co.KNO2(ax))):
            return False
        elif Co.KNO2(ax):
            return True
        elif Co.Borax(ax):
            return True
            
