# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion
class C2O42(anion):
    i=0
    concsul="A colourless odourless gas is evolved"
    @classmethod
    def CaCl2(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("acetic acid" in ax or "CH3COOH" in ax) and ("CaCl2" in ax)and ("salt sol" in ax):
                return True
        else : return False
    @classmethod
    def KMnO4(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("salt" in ax) and ("dil" in ax or "dilute" in ax) and ("HCl" in ax) and ("KMnO4" in ax) :
            return True
        else : return False
        
    @classmethod
    def aniontest(self): 
            import src.Virtual_Lab.Anions.confirmanion as c
            ax=c.yg
            if( (not C2O42.CaCl2(ax)) and (not C2O42.KMnO4(ax))):
                return False
            elif C2O42.CaCl2(ax):
                return True
            elif C2O42.KMnO4(ax):
                return True