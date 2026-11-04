# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class NH4(cation):
    colour="Colourless "
    fcolour="Colourless"
    gpc="Colourless Gas Evolves"# for sake of simplicity
    i=0

        
    def K2HgI4 (s1):
        
        if ("K2HgI4" in s1 or "nessler's reagent" in s1.lower()):
            return True
        else:
            return False

    def boil(self, s1):
        if "boil" in s1.lower():
            return True
        else:
            return False
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.aj
        if NH4.K2HgI4(ax):
            return True
        else:
            return False

