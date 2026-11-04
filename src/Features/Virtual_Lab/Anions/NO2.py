# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion

class NO2(anion):
    dilsul=" evolved turns paper dipped in FeSO4 black"
    @classmethod
    def KMnO4(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("acidified" in ax.lower()) and ("WE" in ax) and ("KMnO4" in ax):
            return True
        else : return False
    @classmethod
    def KI(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("KI" in ax and (("WE" in ax) and ("starch" in ax.lower()))):
            return True
        else :
            return False
    @classmethod    
    def FeSO4(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("acetic acid" in ax.lower() or "CH3COOH" in ax) and (("WE" in ax) and ("FeSO4" in ax )):
            return True
        else : return False
    @classmethod
    def aniontest(self): 
            import src.Virtual_Lab.Anions.confirmanion as c
            ax=c.yg
            if( (not NO2.FeSO4(ax)) and (not NO2.KMnO4(ax)) and (not NO2.KI(ax))):
                return False
            elif NO2.FeSO4(ax):
                return True
            elif NO2.KI(ax):
                return True
            elif NO2.KMnO4(ax):
                return True