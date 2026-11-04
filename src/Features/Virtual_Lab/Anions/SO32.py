# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""

from src.Virtual_Lab.Anions.anion import anion
class SO32(anion):
    dilsul="Gas evolved turns acidified K2Cr2O7 paper green and decolourises KMnO4"
    @classmethod
    def KMNO4(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("acidified" in ax.lower()) and ("salt" in ax.lower()) and ("KMnO4" in ax):
            return True
        else : return False
    @classmethod
    def BaCl2(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax=c.yg
        if ("BaCl2" in ax) and (("WE" in ax) or ("SE" in ax)):
            return True
        else : return False
    @classmethod
    def aniontest(self):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if( (not SO32.BaCl2(ax)) and (not SO32.KMNO4(ax))):
            return False
        elif SO32.BaCl2(ax):
            return True
        elif SO32.KMNO4(ax):
            return True