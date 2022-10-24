# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:30:12 2022

@author: Franc
"""


class giocatore:
    
    def __init__(self, nome = "", cartelle = list()):
        # Il giocatore è definito da un nome e da una lista di oggetti di tipo cartella 
        self.nome = nome
        self.cartelle = cartelle
        
    def get_giocatore(self):
        # Metodo che restituisce il nome del giocatore e le sue cartelle
        print(f"{self.nome} {self.cartelle}")
        
    
        
   