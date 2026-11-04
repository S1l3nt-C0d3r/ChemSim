# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:09:17 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Cations.cation import cation
class Fe(cation):
    colour="Brown"
    fcolour="Gold"
    gpc="Rediish Brown"
    

  
    def K4FeCN6(self,s1):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.dl
        if ("K4FeCN6" in ax):
            return True
        else:
            return False
   
    def KSCN(self,ac):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax = c.dl
        if ("KSCN" in ax ):
            return True
        else:
            return False
    def wettest(self):
        import src.Virtual_Lab.Cations.confirm1 as c
        ax=c.dl
        if( (not Fe.K4FeCN6(ax) )and (not Fe.KSCN(ax))):
            return False
        elif Fe.K4FeCN6(ax): return True
        elif Fe.KSCN(ax): return True
            
            
        
