# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation

class Pb(cation):
    colour="Colourless"
    fcolour="White"
    gpc="White"
    
    def K2CrO4(s1):
        if "K2CrO4" in s1 :
            return True
        else:
            return False
    def KI(s1):
        if "KI" in s1:
            return True
        else:
            return False

    def boil(self, s1):
        if "boil" in s1.lower():
            return True
        else:
            return False

    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        az=c.am
        if (Pb.KI(az)) or (Pb.K2CrO4(az)):
            c.am = ""
            return True
        elif((not Pb.K2CrO4(az)) and (not Pb.KI(az))):
            c.am=""
            return False

