# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:31:22 2022

@author: Sarvaarth
"""
from src.Virtual_Lab.Anions.anion import anion
import random as r
class CO32(anion):
    i=0
    a=0
    dilsul="Gas evolved turns Lime water milky"
    @classmethod
    def dilHCl(self, ac):
        
        if ("dil" in ac.lower() and "HCl" in ac and "sol" in ac.lower()):
            return True
        else : return False
    @classmethod
    def MgSO4(self, ac):
        
        if ("sol" in ac.lower()) and ("MgSO4" in ac):
            return True
        else : return False
    @classmethod
    def aniontest(self): 
            if CO32.i==0:
                CO32.i+=1
                CO32.pre()
            if CO32.a==1:
                CO32.sol()
            elif CO32.a==2:
                CO32.insol()

    @classmethod 
    def pre(self): 
        CO32.a=r.randint(1,2)
        CO32.a=1
        if(CO32.a==1):
            True
        elif CO32.a==2:
            False
    @classmethod        
    def HClinsol(self,ac):
        
        if ("dil" in ac.lower() and "HCl" in ac and "sol" not in ac.lower()):
            return True
        else : return False   
    @classmethod        
    def insol(self):
            ac=input("Action: ")
            while(not CO32.HClinsol(ac)):
                    print("No Change")
                    ac=input("Action: ")
            print("Gas evolves with brisk effervescence")
    
    
        
    @classmethod  
    def sol(self):
        ac=input("Action: ")
        while (not CO32.dilHCl(ac)) and (not CO32.MgSO4(ac)):
                print("No Change")
                ac=input("Action: ")
        if CO32.dilHCl(ac):
            print("Gas evolves with brisk effervescence")
        elif CO32.MgSO4(ac): print ("White PPT")
        else:
            print("No Change")