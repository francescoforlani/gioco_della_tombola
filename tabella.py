# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:22:04 2022
@author: Francesco & Orlando

Il tabellone è creato con una matrice 18x5, in cui per ogni riga verranno assegnati 5 numeri da 1 a 90.
"""


import numpy as np


class tabella:

    def __init__(self):
        self.valori_tab = np.zeros((18, 5), dtype=int)
        for i in range(18):
            self.valori_tab[i] = [j for j in range(5*i + 1, 5*(i+1) + 1)]
        self.valori_daagg = np.zeros((18, 5), dtype=int)    
        self.segno= 0
  
    def aggiungi_numero(self, numeroestratto):
       
        i = (numeroestratto - 1) // 5  # indicatore riga per numero estratto
        j = (numeroestratto - 1) % 5   # indicatore colonna per numero estratto
        z = (numeroestratto - 1) // 15 # indicatore cartella tabellone per numero estratto
        self.valori_daagg[i,j]=1
        self.stampa_riga = self.valori_tab[i]
        self.stampa_cart = self.valori_tab[3*z:3*(z+1)]
        self.stampa_zeri = self.valori_daagg[i]
        
        sommanum_cartella = sum(sum(self.valori_daagg[3*z:3*(z+1)]))
        sommanum_riga = sum(self.valori_daagg[i])
 
        if sommanum_cartella == 15:
            risultato = 'tombola'
        elif sommanum_riga == 5:
            risultato = 'cinquina'
        elif sommanum_riga == 4:
            risultato = 'quaterna'
        elif sommanum_riga == 3:
            risultato = 'terna'
        elif sommanum_riga == 2:
            risultato = 'ambo'
        else:
            risultato = 'nullo'
        return risultato
    
