# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Mg(cation):
    colour="Colourless "
    fcolour="Colourless"
    gpc="White"
    i=0

    def CC(s1):
        if (("charcoal" in s1.lower() or "cavity" in s1.lower() or "CoNO32" in s1) and "ppt" in s1.lower() ):
            return True
        else:
            return False
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.ga
        if( (not Mg.CC(ax))):
            return False
        else:
            return True
