# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:25:19 2022

@author: Franc

"""


import sys
import random

from busta import busta
#from Tabellone import Tabellone
#from Cartelle import Gruppo_cartelle
from giocatore import giocatore


<<<<<<< HEAD

#inserisci numero giocatori (int<10)
numero_giocatori = int(input("Ciao! Inserisci il numero di giocatori (numero intero, esempio: 2): "))
if numero_giocatori > 10:
    print(f"{numero_giocatori} giocatori sono troppi, il massimo è 10.")
    sys.exit()

#inserisci nomi dei giocatori (lista) e controlla di ricevere tanti nomi quanti sono i giocatori
nomi_giocatori = input("Ok siete in {numero_giocatori} giocatori. Inserisci i vostri nomi (esempio: Francesco Orlando): ")
nomi_giocatori = nomi_giocatori.split()
for i in range(len(nomi_giocatori)):
    nomi_giocatori[i] = str(nomi_giocatori[i])
    
if len(nomi_giocatori) != numero_giocatori:
    print(f'Il numero di giocatori non corrisponde alla lunghezza della lista dei nomi.')
    sys.exit()

#inserisci il numero di cartelle per ogni giocatore (max 6) e controlla di ricevere tanti valori 
#quanti sono i giocatori
cartelle_per_giocatore = [0]*numero_giocatori
for i in range(len(nomi_giocatori)):
    cartelle_per_giocatore[i] = input(f"Quante cartelle per {nomi_giocatori[i]}? Inserisci un numero: ")

for i in range(len(cartelle_per_giocatore)):
    cartelle_per_giocatore[i] = int(cartelle_per_giocatore[i])
    
for i in range(len(cartelle_per_giocatore)):
    if cartelle_per_giocatore[i] > 6:
        print(f"{cartelle_per_giocatore[i]} cartelle sono troppe, il massimo per ogni giocatore è 6.")
        sys.exit()
        
#assegna le cartelle ad ogni giocatore in modo randomico
cartella_di_prova_1 = [[0, 16, 21, 31, 42, 0, 60, 0, 0],
                     [1, 18, 0, 33, 0, 53, 62, 0, 0],
                     [2, 0, 0, 38, 0, 55, 0, 74, 90]]

cartella_di_prova_2 = [[0, 17, 24, 31, 41, 51, 0, 0, 0],
                       [2, 0, 25, 0, 43, 0, 0, 70, 81],
                       [0, 0, 0, 36, 44, 52, 63, 0, 85]]

cartella_di_prova_3 = [[0, 11, 24, 35, 41, 51, 0, 0, 0],
                       [2, 0, 25, 0, 42, 0, 0, 70, 81],
                       [0, 0, 0, 36, 44, 52, 67, 0, 85]]

cartella_di_prova_4 = [[0, 17, 24, 31, 41, 55, 0, 0, 0],
                       [2, 0, 28, 0, 43, 0, 0, 70, 81],
                       [0, 0, 0, 36, 44, 59, 63, 0, 85]]
cartella_di_prova_5 = [[0, 13, 21, 31, 42, 0, 60, 0, 0],
                     [1, 19, 0, 33, 0, 53, 64, 0, 0],
                     [2, 0, 0, 38, 0, 59, 0, 74, 90]]

cartella_di_prova_6 = [[0, 17, 21, 33, 41, 51, 0, 0, 0],
                       [2, 0, 25, 0, 43, 0, 0, 76, 81],
                       [0, 0, 0, 38, 44, 52, 63, 0, 87]]

lista_cartelle_di_prova = [cartella_di_prova_1, cartella_di_prova_2, 
                           cartella_di_prova_3, cartella_di_prova_4,
                           cartella_di_prova_5, cartella_di_prova_6]

for i in range(len(nomi_giocatori)):
    globals()["giocatore_"+str(i+1)] = giocatore(f"{nomi_giocatori[i]}", 
                                                 random.sample(lista_cartelle_di_prova, 
                                                               cartelle_per_giocatore[i]))
    print("Ecco le cartelle per ogni giocatore:")
    print(vars(globals()["giocatore_"+str(i+1)]))
    
#crea l'oggetto busta da cui estrarre i numeri
busta = busta

#inizia l'estrazione dei numeri e il controllo delle cartelle man mano che escono i numeri

=======
print('let's goooo')
>>>>>>> bc099ae2f63af396545401baa7564fe50d95cacc

