# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:30:12 2022

@author: Franc
"""
import numpy as np

class giocatore:
    
    def __init__(self, nome = "", cartelle = list()):
        self.nome = nome
        self.cartelle = cartelle
        
    def get_giocatore(self):
        print(f"{self.nome} {self.cartelle}")
        
    def copri_numero(self, cartella, numero_estratto): #dato il numero estratto verifico se ho vinto qualcosa
        cartella_array = np.array(cartella)
        if numero_estratto not in cartella_array:
            risultato = "non c'è"
        else:
            i, j = np.where(cartella_array == numero_estratto)  # posizione del numero
            cartella_array[i, j] = -1  # segna che il numero è stato estratto
            cartella = cartella_array.tolist()
            risultato_riga = (cartella_array[i] <0).sum()
            risultato_cartella = (cartella_array <0).sum()
            if risultato_cartella == 15:
                risultato = 'tombola'
            elif risultato_riga == 5:
                risultato = 'cinquina'
            elif risultato_riga == 4:
                risultato = 'quaterna'
            elif risultato_riga == 3:
                risultato = 'terna'
            elif risultato_riga == 2:
                risultato = 'ambo'
            else:
                risultato = 'niente'
        return risultato, cartella
        
   