# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:25:19 2022

@author: Franc

"""


import sys
import random
from busta import busta
from gruppo_cartelle import gruppo_di_cartelle
from giocatore import giocatore
from cartella import Cartella




#inserisci numero giocatori (int<10)
numero_giocatori = int(input("Ciao! Inserisci il numero di giocatori (numero intero, esempio: 2): "))
if numero_giocatori > 10:
    print(f"{numero_giocatori} giocatori sono troppi, il massimo è 10.")
    sys.exit()

#inserisci nomi dei giocatori (lista) e controlla di ricevere tanti nomi quanti sono i giocatori
nomi_giocatori = input(f"Ok siete in {numero_giocatori} giocatori. Inserisci i vostri nomi (esempio: Francesco Orlando): ")
nomi_giocatori = nomi_giocatori.split()
for i in range(len(nomi_giocatori)):
    nomi_giocatori[i] = str(nomi_giocatori[i])
    
if len(nomi_giocatori) != numero_giocatori:
    print('Il numero di giocatori non corrisponde alla lunghezza della lista dei nomi.')
    sys.exit()

#inserisci il numero di cartelle per ogni giocatore (max 6) 
cartelle_per_giocatore = [0]*numero_giocatori
for i in range(len(nomi_giocatori)):
    cartelle_per_giocatore[i] = input(f"Quante cartelle per {nomi_giocatori[i]}? Inserisci un numero: ")

for i in range(len(cartelle_per_giocatore)):
    cartelle_per_giocatore[i] = int(cartelle_per_giocatore[i])
    
for i in range(len(cartelle_per_giocatore)):
    if cartelle_per_giocatore[i] > 6:
        print(f"{cartelle_per_giocatore[i]} cartelle sono troppe, il massimo per ogni giocatore è 6.")
        sys.exit()
        

#assegna le cartelle richieste da ogni giocatore
lista_giocatori = []
for i in range(len(nomi_giocatori)):
    gruppo_cartelle = gruppo_di_cartelle()
    globals()["giocatore_"+str(i+1)] = giocatore(f"{nomi_giocatori[i]}", 
                                                 random.sample(gruppo_cartelle.crea_gruppo_cartelle(), 
                                                               cartelle_per_giocatore[i]))
    lista_giocatori.append(globals()["giocatore_"+str(i+1)])
    print("Ecco le cartelle per ogni giocatore:")
    print(vars(globals()["giocatore_"+str(i+1)]))
    
#crea l'oggetto busta da cui estrarre i numeri
busta = busta()

#inizia l'estrazione dei numeri e il controllo delle cartelle man mano che escono i numeri
print("Iniziamo. Premi INVIO per estrarre un numero.")
while True:
    input("")
    numero_estratto = busta.estraggo()
    print(f"il numero estratto è {numero_estratto}")
        
    #aggiorna le cartelle dei giocatori
    lista_risultati_del_turno = []
    for giocatore in lista_giocatori:
        for index in range(len(giocatore.cartelle)):
            risultato = giocatore.cartelle[index].copri_numero(numero_estratto)
            lista_risultati_del_turno.append(risultato)
            if risultato != "niente":
                print(f"{giocatore.nome} ha fatto {risultato} nella cartella {index+1}")
            

    # se qualcuno ha fatto tombola termina il gioco
    exist_count = lista_risultati_del_turno.count("tombola")
    if exist_count > 0: 
        print("")
        print("E' stata fatta tombola. Fine del gioco.")
        sys.exit()
        
    print("Premi INVIO per estrarre un nuovo numero.")

