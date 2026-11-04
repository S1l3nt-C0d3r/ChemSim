# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion

class NO3(anion):
    concsul=" evolved turns paper dipped in FeSO4 black"
    @classmethod
    def brownring(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("FeSO4" in ax and "conc" in ax.lower() and "H2SO4" in ax and "WE" in ax) or "brown ring" in ax.lower(): #Easter Egg: This code was REALLY HARD!!!
            return True
        else : return False
    @classmethod
    def NO2gas(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if "salt" in ax.lower() and "conc" in ax.lower() and "H2SO4" in ax and ("cu chips" in ax.lower() or "cu turnings" in ax.lower()):
            return True
        else : return False
    @classmethod
    def aniontest(self): 
            import src.Virtual_Lab.Anions.confirmanion as c
            ax=c.yg
            if( (not NO3.brownring(ax)) and (not NO3.NO2gas(ax))) :
                return False
            elif NO3.brownring(ax):
                return True
            elif NO3.NO2gas(ax):
                return True