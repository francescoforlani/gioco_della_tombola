# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:30:12 2022

@author: Franc
"""


class giocatore:
    
    def __init__(self, nome = "", cartelle = list(), lista_risultati = [0]):
        # Il giocatore è definito da un nome, da una lista di oggetti di tipo cartella e da una lista di 
        # risultati 
        self.nome = nome
        self.cartelle = cartelle
        self.lista_risultati = lista_risultati
        
    def get_giocatore(self):
        # Metodo che fa visualizzare il nome del giocatore e le sue cartelle
        print(f"{self.nome} {self.cartelle}")
        
    def controlla_risultati(self, numero_estratto):
        # Metodo che prende in ingresso il numero estratto, chiama il metodo copri_numero della classe cartella
        # e restituisce il risultato migliore del giocatore, se non l'ha ancora fatto.
        best_risultato = max(self.lista_risultati)
        risultati_del_turno = []
        for index in range(len(self.cartelle)):
            risultato = self.cartelle[index].copri_numero(numero_estratto)
            if risultato > best_risultato:
                self.lista_risultati.append(risultato)                
                best_risultato = risultato            
                if best_risultato == 2:
                    risultato = f"ambo nella cartella numero {index+1}: {self.cartelle[index].caselle}"
                if best_risultato == 3:
                    risultato = f"terna nella cartella numero {index+1}: {self.cartelle[index].caselle}"
                if best_risultato == 4:
                    risultato = f"quaterna nella cartella numero {index+1}: {self.cartelle[index].caselle}"
                if best_risultato == 5:
                    risultato = f"cinquina nella cartella numero {index+1}: {self.cartelle[index].caselle}"
                if best_risultato == 6:
                    risultato = f"tombola nella cartella numero {index+1}: {self.cartelle[index].caselle}"
                risultati_del_turno.append(risultato)
            else:
                risultato = "niente"
                
        return risultati_del_turno
            
                
        
   