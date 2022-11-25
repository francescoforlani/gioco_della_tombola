# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:30:12 2022
@author: Francesco & Orlando
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
        
        
    def controlla_risultato(self, numero_estratto):
        # Metodo che prende in ingresso il numero estratto, chiama il metodo copri_numero della classe cartella
        # e restituisce il risultato migliore del giocatore, se non l'ha ancora fatto. 
        best_risultato = max(self.lista_risultati)
        for index in range(len(self.cartelle)):
            risultato = self.cartelle[index].copri_numero(numero_estratto)
            if risultato > best_risultato:
                self.lista_risultati.append(risultato)
                best_risultato = risultato            
                if best_risultato == 2 : 
                    return "ambo" 
                if best_risultato == 3 :
                    return "terna"
                if best_risultato == 4 :
                    return "quaterna"
                if best_risultato == 5:
                    return "cinquina"
                if best_risultato == 6:
                    return "tombola"
            else:
                return "nullo"
                
                #         if best_risultato == 2 : 
                #     risultato = 'ambo' 
                # elif best_risultato == 3 :
                #     risultato = 'terna'
                # elif best_risultato == 4 :
                #     risultato = 'quaterna'
                # elif best_risultato == 5:
                #   risultato = 'cinquina'
                # elif best_risultato == 6:
                #     risultato = 'tombola'
                # else:
                #     risultato ='nullo'
                    
                # return risultato 
   