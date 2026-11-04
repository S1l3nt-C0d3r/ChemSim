# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion
class PO43(anion):
    i=0
    @classmethod
    def ammoly(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax=c.yg
        if ("SE" in ax)and ("conc" in ax.lower()) and ("HNO3" in ax)  :
            return True
        else : return False
    @classmethod
    def magnesia(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax=c.yg
        if ("magnesia" in ax.lower()) and (("WE" in ax) or ("neutral" in ax.lower() and "SE" in ax)) and ("magnesia" in ax.lower()):
            return True
        else : return False
        
    @classmethod
    def aniontest(self): 
            import src.Virtual_Lab.Anions.confirmanion as c
            ax=c.yg
            if( (not PO43.ammoly(ax)) and (not PO43.magnesia(ax))):
                return False
            if PO43.ammoly(ax):
                return True
            elif PO43.magnesia(ax):
                return True