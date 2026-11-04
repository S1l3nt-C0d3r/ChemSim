# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Cu(cation):
    colour="Blue"
    fcolour="Peacock/Bluish Green"
    gpc="Black"
    i=0
    @classmethod
    def NH4OH(self,ac):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.bc
        if ("NH4OH" in ax) and ("os" in ax.lower()) and ("excess" in ax.lower()):
            return True
        else:
            return False
    @classmethod
    def K4FeCN6(self,ac):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.bh
        if "K4FeCN6" in ax:
            return True
        else:
            return False

    def boil(self, s1):
        if "boil" in s1:
            return True
        else:
            return False
    @classmethod
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.bc
        if( (not Cu.NH4OH(ax))):
             return False
        elif Cu.NH4OH(ax):
            return True


