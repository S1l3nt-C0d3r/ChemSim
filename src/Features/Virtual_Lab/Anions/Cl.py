# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion
class Cl(anion):
    concsul="PPT soluble in NH4OH with AgNO3"
    @classmethod
    def HNO3(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax=c.yg
        if ("conc" in ax.lower()) and ("salt sol" in ax.lower()) and ("HNO3" in ax) and ("AgNO3" in ax):
            return True
        else : return False
    @classmethod
    def MnO2(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("conc" in ax.lower()) and ("H2SO4" in ax) and ("salt" in ax.lower()) and ("MnO2" in ax):
            return True
        else : return False
    @classmethod    
    def K2Cr2O7(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("conc" in ax.lower()) and ("H2SO4" in ax) and (("salt" in ax.lower()) and ("K2Cr2O7" in ax) and ("solid" in ax.lower())):
            return True
        else : return False
    @classmethod   
    def t2(self):
        pass
        
    @classmethod
    def aniontest(self):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if( (not Cl.HNO3(ax)) and (not Cl.MnO2(ax)) and (not Cl.K2Cr2O7(ax))):
                return False
        if Cl.HNO3(ax):
                return True
        elif Cl.MnO2(ax):
                return True
        elif Cl.K2Cr2O7(ax):
                return True
