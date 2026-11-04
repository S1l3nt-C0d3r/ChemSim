# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Al(cation):
    colour="Colourless"
    fcolour="Colourless"
    gpc="White"
    
    @classmethod
    def CC(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.jb
        if (("Charcoal" in ax or "Cavity" in ax or "CoNO32" in ax) and "PPT" in ax ):
            return True
        else:
            return False
    @classmethod
    def Lake(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.jb
        if ("PPT" in ax and "Blue Litmus" in ax and "NH4OH" in ax and "excess" in ax ):
            return True
        else:
            return False
    @classmethod
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.jb
        if( (not Al.CC(ax) )and (not Al.Lake(ax))):
            return False
        elif Al.CC(ax): return True
        elif Al.Lake(ax): return True

        

