# -*- coding: utf-8 -*-


"""
Created on Fri Oct 21 14:22:04 2022


@author: Orlando

Il tabellone è creato con una matrice 18x5, in cui per ogni riga verranno assegnati 5 numeri da 1 a 90.
"""


import numpy as np



class tabella:

    def __init__(self):
        self.valori_tab = np.zeros((18, 5), dtype=int)
        for i in range(18):
            self.valori_tab[i] = [j for j in range(5*i + 1, 5*(i+1) + 1)]
        self.valori_daagg = np.zeros((18, 5), dtype=int)    

  
    def aggiungi_numero(self, numeroestratto):
       
        i = (numeroestratto - 1) // 5  # indicatore riga per numero estratto
        j = (numeroestratto - 1) % 5   # indicatore colonna per numero estratto
        z = (numeroestratto - 1) // 15 # indicatore cartella tabellone per numero estratto
       
        self.valori_daagg[i,j]=1
        a = 3*z
        b = (3*(z+1))
        self.sommanum_cartella = sum(sum(self.valori_daagg[a:b]))
        self.sommanum_riga = sum(self.valori_daagg[i])
        self.posizione_riga = i
        self.posizione_colonna = z
       
        # if sommanum_riga == 2:
        #     print(f'Il tabellone ha fatto ambo alla riga:  {i}')           
        # elif sommanum_riga == 3:
        #     print(f'Il tabellone ha fatto terno alla riga:  {i}')
        # elif sommanum_riga == 4:
        #     print(f'Il tabellone ha fatto quaterna alla riga:  {i}')        
        # elif sommanum_riga == 5:
        #     print(f'Il tabellone ha fatto cinquina alla riga : {i}')    
        # elif sommanum_cartella == 15:
        #     print(f'Il tabellone ha fatto Tombola nella cartella : {z}')
            
 