class Fgroup():

    def FTest(self):
        pass
    def KMnO4(self, ac):
        if ("KMnO4" in ac) and ("dil" in ac):
            return True
        else: return False
    def Bwater(self,ac):
        if ("Bromine" in ac) and ("water" in ac):
            return True
        else: return False        

class COOH(Fgroup):
    @classmethod
    def NaHCO3(self,ac):
        import functionalconfirm as f
        ax=f.yq
        if ("sat" in ax) and ("NaHCO3" in ax):
            return True
        else : return False
    @classmethod
    def C2H5OH(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("C2H5OH" in ax):
            return True
        else: return False
    @classmethod
    def gastest(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("lime water" in ax):
            return True
        else : return False
    @classmethod
    def FTest(self):
        import functionalconfirm as f
        ax = f.yq
        if (not COOH.NaHCO3(ax) and (not COOH.C2H5OH(ax))):
            return False
        if COOH.NaHCO3(ax):
                return True
        elif COOH.C2H5OH(ax)==True:
            return True
class phenol(Fgroup):
    @classmethod
    def NaOH(self,ac):
        import functionalconfirm as f
        ac=f.yq
        if ("dil" in ac) and ("NaOH" in ac):
            return True
        else : return False
    @classmethod
    def FeCl3(self,ac):
        import functionalconfirm as f
        ac = f.yq
        if ("neu" in ac) and ("FeCl3" in ac):
            return True
        else : return False
    @classmethod
    def FTest(self):
        import functionalconfirm as f
        ac=f.yq
        if ((not phenol.NaOH(ac)) and (not phenol.FeCl3(ac))):
            return False
        elif phenol.NaOH(ac):
                return True
        elif phenol.FeCl3(ac):
                return True


class ketone(Fgroup):
    @classmethod
    def Nanitpro(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("sodium nitroprusside" in ax.lower() ):
            return True
        else : return False
    @classmethod
    def DNP24(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("2,4 DNP" in ax ):
            return True
        else : return False
    @classmethod
    def FTest(self):
        import functionalconfirm as f
        ax = f.yq
        if (not ketone.Nanitpro(ax) and not ketone.DNP24(ax)):
            return False
        elif ketone.Nanitpro(ax):
                return True
        elif ketone.DNP24(ax):
                return True
                
class CHO(Fgroup):
    @classmethod
    def schiff(self,ac):
        import functionalconfirm as f
        ax=f.yq
        if ("schiff's" in ax ):
            return True
        else : return False
    @classmethod
    def tollen(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("tollen" in ax ):
            return True
        else : return False
    @classmethod
    def DNP24(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("2,4 DNP" in ax ):
            return True
        else : return False
    @classmethod
    def FTest(self):
        import functionalconfirm as f
        ax = f.yq
        if (not CHO.schiff(ax)) and (not CHO.DNP24(ax)) and not (CHO.tollen(ax)):
            return False
        elif CHO.schiff(ax):
                return True
        elif CHO.tollen(ax):
                return True
        elif CHO.DNP24(ax):
                return True


class amine(Fgroup):
    @classmethod
    def test(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("dil" in ax) and ("HCl" in ax) and ("NaNO2" in ax):
            return True
        else : return False
    @classmethod
    def FTest(self):
        import functionalconfirm as f
        ax = f.yq
        while (not amine.test(ax)):
            return False
        if amine.test(ax): # is understood but still this counter so that in future code can be extented or not ;)
            return True
class OH(Fgroup):
    @classmethod
    def Na(self,ac):
        import functionalconfirm as f
        ax = f.yq
        if ("Na" in ax):
            return True
        else : return False
    @classmethod
    def FTest(self):
        import functionalconfirm as f
        ax = f.yq
        if (not OH.Na(ax)):
            return False
        elif OH.Na(ax):# is understood but still this counter so that in future code can be extented or not ;)
            return True