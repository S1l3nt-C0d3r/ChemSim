import tkinter

class cation():
    colour = None
    fcolour = None
    gpc = None

    @classmethod
    def boil(cls,s1):
        if "boil" in s1:
            return True
        else:
            return False

    def g1g2(self, ac):
        if ("dil" or "dilute" in ac) and ("HCl" in ac):
            return False
        else:
            return False

    def g3g4(self, ac):

        if ("solid" in ac) and ("NH4Cl" in ac) and ("HNO3" in ac):
            return True
        else:
            return False

    def g5(self, ac):
        if (("OS" in ac or "os" in ac) and ("solid" in ac or "Solid" in ac) and "NH4OH" in ac and "(NH4)2CO3" in ac and "NH4Cl" in ac):
            return True
        else:
            return False

    def g0(self, ac):
        if ("NaOH" in ac and "salt" in ac.lower() ):
            return True
        else:
            return False

    def g6(self, ac):
        if ("OS" in ac and "NH4Cl" in ac and "NH4OH" in ac and ("excess Ammonium Phosphate" in ac or "excess (NH4)3PO4" in ac)):
            return True
        else:
            return False

    @classmethod
    def g1(cls, s1):
        if ("dil" or "dilute" in s1) and ("HCl" in s1):
            return True
        else:

            return False

    def g2(cls, s1):
        if ("H2S" in s1):
            return True
        else:
            return False

    def g3(self, ac):

        if ("solid" in ac) and ("NH4Cl" in ac) and ("HNO3" in ac):
            return True
        else:
            return False
            