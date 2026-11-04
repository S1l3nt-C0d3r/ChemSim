# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion

class CH3COO(anion):
    concsul="Colourless vapour with vinegar smell"
    @classmethod
    def ester(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax=c.yg
        if ("salt" in ax.lower()) and ("CS2" in ax ) and ("conc" in ax.lower()) and ("H2SO4" in ax ) and ("C2H5OH" in ax) :
            return True
        else : return False
    @classmethod
    def oxalic(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("salt" in ax.lower()) and (("oxalic acid" in ax.lower()) or ("(COOH)2" in ax)) and (("H2O" in ax ) or ("water" in ax.lower())) :
            return True
        else : return False
        
    @classmethod
    def aniontest(self):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if( (not CH3COO.ester(ax)) and (not CH3COO.oxalic(ax))):
            return False
        elif CH3COO.ester(ax):
            return True
        elif CH3COO.oxalic(ax):
            return True