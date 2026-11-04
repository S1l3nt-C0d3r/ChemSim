# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion
global k
class S2(anion):
    dilsul="Rotten egg smelling gas evolved that turns Lead Aceatate paper black"
    @classmethod
    def acetic(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as co
        ac=co.yg
        if ("acetic acid" in ac.lower() or "CH3COOH" in ac) and (("WE" in ac) or ("SE" in ac) and ("Lead Acetate" in ac or "(CH3COO)2Pb" in ac)):
            return True
        else : return False
    @classmethod
    def Nitroprusside(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as co
        ac = co.yg
        if ("sodium nitroprusside" in ac.lower()) and (("WE" in ac) or ("SE" in ac)):
            return True
        else : return False
    @classmethod
    def CdCO3(self,ac):
        import src.Virtual_Lab.Anions.confirmanion as co
        ac = co.yg
        if ("CdCO3" in ac) and (("WE" in ac) or ("SE" in ac)):
            return True
        else : return False
    @classmethod
    def aniontest(self):
            import src.Virtual_Lab.Anions.confirmanion as co
            ac=co.yg
            if( (not S2.acetic(ac)) and (not S2.Nitroprusside(ac)) and (not S2.CdCO3(ac))):
                   return False
            elif S2.acetic(ac):
                return True
            elif S2.Nitroprusside(ac):
                return True
            elif S2.CdCO3(ac):
                return True
            else:
                return False
