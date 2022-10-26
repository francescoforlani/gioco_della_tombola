# -*- coding: utf-8 -*-
"""
Modificato on Thu Oct 25 12:15:54 2022
-Aggiunta  libreria Argparse con relativa richiesta. 
-Aggiunta variabile nel ciclo For, [104-115], per ottenere i risultati della tombola una singola volta
 e non per ogni giocatore.
-Eliminazione globals  

??? Come vogliare comportarci con la stringa dei nomi ??? 

@author: Orlando

"""


import sys
import random
from busta import busta
from gruppo_cartelle import gruppo_di_cartelle
from giocatore import giocatore
# from cartella import Cartella 
from argparse import ArgumentParser




parser = ArgumentParser()
parser.add_argument('-g', '--numero_giocatori',
                    help='Numero dei giocatori',
                    type=int, default=3)
parser.add_argument('-n', '--numero_cartelle',
                    help='numero carelle assegnate per giocatore',
                    nargs='*', type=int, default=[2,2,2])



# #inserisci numero giocatori (int<10)
# numero_giocatori = int(input("Ciao! Inserisci il numero di giocatori (numero intero, esempio: 2): "))
# if numero_giocatori > 10:
#     print(f"{numero_giocatori} giocatori sono troppi, il massimo è 10.")
#     sys.exit()

args = parser.parse_args()
numero_giocatori = args.numero_giocatori
numero_cartelle = args.numero_cartelle

#inserisci nomi dei giocatori (lista) e controlla di ricevere tanti nomi quanti sono i giocatori
nomi_giocatori = input(f"Ok siete in {numero_giocatori} giocatori. Inserisci i vostri nomi : ")
nomi_giocatori = nomi_giocatori.split()
for i in range(len(nomi_giocatori)):
    nomi_giocatori[i] = str(nomi_giocatori[i])
    
if len(nomi_giocatori) != numero_giocatori:
    print('Il numero di giocatori non corrisponde alla lunghezza della lista dei nomi.')
    sys.exit()

#inserisci il numero di cartelle per ogni giocatore (max 6) 
cartelle_per_giocatore = [0]*numero_giocatori
for i in range(len(nomi_giocatori)):
    for j in range(len (numero_cartelle)):
        cartelle_per_giocatore[i] = numero_cartelle[j]

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
    lista_giocatori1 = ["giocatore_"+str(i+1)]
    lista_giocatori1 = giocatore(f"{nomi_giocatori[i]}", 
                                                 random.sample(gruppo_cartelle.crea_gruppo_cartelle(), 
                                                               cartelle_per_giocatore[i]))
    lista_giocatori.append(lista_giocatori1)
    print(f"Il giocatore {nomi_giocatori[i]} ha {cartelle_per_giocatore[i]} cartelle.")
    
    
#crea l'oggetto busta da cui estrarre i numeri
busta = busta()
# niente_segno = 0
segno = 0

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
            # if risultato != "niente" and niente_segno == 0:
            #     print(f"{giocatore.nome} ha fatto {risultato} nella cartella {index+1}")
            #     niente_segno = 1          
            # el
            if risultato == "ambo" and segno == 0:
                print(f"{giocatore.nome} ha fatto {risultato} nella cartella {index+1}")
                segno += 1                
            elif risultato == "terna" and segno == 1:
                print(f"{giocatore.nome} ha fatto {risultato} nella cartella {index+1}")
                segno += 1             
            elif risultato == "quaterna" and segno == 2:
                print(f"{giocatore.nome} ha fatto {risultato} nella cartella {index+1}")
                segno += 1               
            elif risultato == "cinquina" and segno == 3:
                print(f"{giocatore.nome} ha fatto {risultato} nella cartella {index+1}")
                segno += 1
            elif risultato == "tombola" and segno == 4:
                print(f"{giocatore.nome} ha fatto {risultato} nella cartella {index+1}")
                segno += 1    
    # se qualcuno ha fatto tombola termina il gioco
    exist_count = lista_risultati_del_turno.count("tombola")
    if exist_count > 0: 
        print("")
        print(f"E' stata fatta tombola da {giocatore.nome}.")
        sys.exit()
        
    print("Premi INVIO per estrarre un nuovo numero.")


        
        
        
        