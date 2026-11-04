# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion
class SO42(anion):
    @classmethod
    def match(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax=c.yg
        if ("salt" in ax.lower()) and ("Na2CO3" in ax) and ("match" in ax.lower()) and ("sodium nitroprusside" in ax.lower()) and "dip" in ax.lower():
            return True
        else : return False

    @classmethod
    def BaCl21(self, ac):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ("BaCl2" in ax) and (("WE" in ax) or ("SE" in ax)):
            return True
        else:
            return False

    @classmethod
    def aniontest(self):
        import src.Virtual_Lab.Anions.confirmanion as c
        ax = c.yg
        if ((not SO42.BaCl21(ax)) and (not SO42.match(ax))):
            return False
        elif SO42.BaCl21(ax):
            return True
        elif SO42.match(ax):
            return True