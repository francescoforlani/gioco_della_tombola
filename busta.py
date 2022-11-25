# -*- coding: utf-8 -*-
"""
Created  on  Thu Sep 29 15:01:37 2022
@author: Francesco & Orlando
"""



import random




class busta:
    
    
    
    
    
    
    
    def __init__(self, numero_min = 1, numero_max = 91):
        # La busta è definita da un insieme di numeri interi nel range che va dal numero minimo al numero massimo
        self.numero_min = numero_min
        self.numero_max = numero_max
        self.numeri_in_busta = list(range(numero_min, numero_max))
        self.numeri_usciti = list()
        
        
        
        
        
        
    def estraggo(self):
        # Metodo che restituisce un numero preso a caso dalla busta e lo rimuove dalla busta 
        numero_preso = random.choice(self.numeri_in_busta) 
        self.numeri_in_busta.remove(numero_preso)
        self.numeri_usciti.append(numero_preso)
        return numero_preso
        
