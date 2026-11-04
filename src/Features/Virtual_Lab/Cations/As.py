# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class As(cation):
    colour="Grey"
    fcolour="Blue"
    gpc="Yellow"
    

    @classmethod
    def Magnesia(self,ac):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.bl
        if ("magnesia" in ax.lower()) and ("os" in ax.lower()):
            return True
        else:
            return False
    @classmethod
    def NH46Mo7O24(self,ac):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.bl
        if ("NH46Mo7O24" in ax ) and ("conc" in ax.lower() or "concentrated" in ax.lower()) and ("HNO3" in ax) :
            return True
        else:
            return False
    @classmethod
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.bl
        if(not As.Magnesia(ax)) and (not As.NH46Mo7O24(ax)):
            return False
        elif As.Magnesia(ax):
            return True
        elif As.NH46Mo7O24(ax):
            return True
        

        
