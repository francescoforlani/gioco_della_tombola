# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:22:04 2022
@author: Francesco & Orlando
"""

import numpy as np



class Cartella:
    
    
    
    
    def __init__(self):
        # La cartella è rappresentato da una matrice 3x9.
        self.caselle = np.zeros((3, 9), dtype=int)
        
        
    def get_cartella(self):
        # Metodo che fa visualizzare la cartella.
        print(self.caselle)
        
        
    def copri_numero(self, numero_estratto): 
        # Dato il numero estratto, verifico se ho vinto qualcosa (ambo, terna, quaterna, cinquina, tombola)
        # e restituisco il risultato.
        if numero_estratto not in self.caselle: # Se il numero estratto non è presente nella cartella, restituisco "niente"
            return 0
        else: # Se invece il numero è presente nella cartella:
            i, j = np.nonzero(self.caselle == numero_estratto)  # prendo la posizione del numero
            self.caselle[i, j] = -1  # metto -1 al posto del numero
            risultato_riga = -sum(self.caselle[i][np.nonzero(self.caselle[i] < 0)])  # conto quanti numeri ho estratto sulla stessa riga
            risultato_cartella = -sum(self.caselle[np.nonzero(self.caselle < 0)])  # conto quanti numeri ho estratto in tutta la cartella
            if risultato_cartella == 15: # Se ho estratto 15 numeri in tutta la cartella:
                risultato = 6 # restituisco il risultato tombola
            elif risultato_riga == 5: # Se ho estratto 5 numeri sulla stessa riga:
                risultato = 5 # restituisco il risultato cinquina
            elif risultato_riga == 4: # Se ho estratto 4 numeri sulla stessa riga:
                risultato = 4 # restituisco il risultato quaterna
            elif risultato_riga == 3: # Se ho estratto 3 numeri sulla stessa riga:
                risultato = 3 # restituisco il risultato terna
            elif risultato_riga == 2: # Se ho estratto 2 numeri sulla stessa riga:
                risultato = 2 # restituisco il risultato ambo
            else: # Se non ho estratto alcun numero sulla stessa riga:
                risultato = 0 # restituisco il risultato niente
            return risultato