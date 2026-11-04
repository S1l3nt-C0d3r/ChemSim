# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion
class I(anion):
    concsul="Vapours turn starch paper blue"
    @classmethod
    def HNO3(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("conc" in ax.lower()) and ("salt sol" in ax.lower()) and ("HNO3" in ax) and ("AgNO3" in ax):
            return True
        else : return False
    @classmethod
    def ClWater(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("chlorine water" in ax.lower()) and ("CS2" in ax) and ("dil" in ax.lower()) and ("HCl" in ax) and ("salt sol" in ax.lower()) :
            return True
        else : return False
        
    @classmethod
    def aniontest(self):
            import src.Virtual_Lab.Anions.confirmanion as c
            ax = c.yg
            if( (not I.HNO3(ax)) and (not I.ClWater(ax))):
                return False
            elif I.HNO3(ax):
                return True
            elif I.ClWater(ax):
                return True