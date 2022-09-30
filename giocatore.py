# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:30:12 2022

@author: Franc
"""

class giocatore:
    
    def __init__(self, nome = "", cartelle = list()):
        self.nome = nome
        self.cartelle = cartelle
        
    def get_giocatore(self):
        print(f"{self.nome} {self.cartelle}")