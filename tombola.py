# -*- coding: utf-8 -*-
"""
Modificato on Thu Oct 25 12:15:54 2022
-Aggiunta  libreria Argparse con relativa richiesta. 
-Aggiunta variabile nel ciclo For, [104-115], per ottenere i risultati della tombola una singola volta
 e non per ogni giocatore.
-Eliminazione globals  

@author: Orlando

"""


import sys
import random
import math
from busta import busta
from gruppo_cartelle import gruppo_di_cartelle
from giocatore import giocatore
# from cartella import Cartella 
from argparse import ArgumentParser
from tabella import tabella 


parser = ArgumentParser()

parser.add_argument('-g', '--numero_giocatori',
                    help='Numero dei giocatori',
                    type=int, default=3)
parser.add_argument('-n', '--numero_cartelle',
                    help='numero carelle assegnate per giocatore',
                    nargs='*', type=int, default=[3,2,1])
parser.add_argument('-f', '--nomi_giocatori',
                    help='nomi dei giocatori',
                    action="store_true",
                    default=['primo','secondo','terzo'])




args = parser.parse_args()
numero_giocatori = args.numero_giocatori
numero_cartelle = args.numero_cartelle
nomi_giocatori = args.nomi_giocatori


# Controllo dati inseriti 
    
if len(nomi_giocatori) != numero_giocatori:
    print('Il numero di giocatori non corrisponde alla lunghezza della lista dei nomi.')
    sys.exit()

if numero_giocatori > 10:
    print(f"{numero_giocatori} giocatori sono troppi, il massimo è 10.")
    sys.exit()    

if  numero_giocatori != len(numero_cartelle):
    print('Il numero di giocatori non corrisponde al numero di cartelle assegnate.')
    sys.exit()    

numero_cartelle_totali = 0
for i in range(len(numero_cartelle)):
    numero_cartelle_totali = numero_cartelle_totali + numero_cartelle[i]
    if numero_cartelle[i] > 6:
        print(f"{numero_cartelle[i]} cartelle sono troppe, il massimo per ogni giocatore è 6.")
        sys.exit()
        

#assegna le cartelle richieste da ogni giocatore
lista_giocatori = []


gruppo_cartelle = gruppo_di_cartelle() # Creo l'oggetto gruppo_cartelle
cartelle_da_dividere = []
numero_gruppi_cartelle = math.ceil(numero_cartelle_totali/6) # Trovo quanti gruppi di cartelle devo generare
for i in range(numero_gruppi_cartelle):
    singolo_gruppo = gruppo_cartelle.crea_gruppo_cartelle() # Genero le cartelle necessarie
    for cartella in singolo_gruppo:
        cartelle_da_dividere.append(cartella) # E preparo la lista con tutte le cartelle che andranno date ai giocatori
        
for i in range(len(nomi_giocatori)):
    player = giocatore(f"{nomi_giocatori[i]}", random.sample(cartelle_da_dividere, numero_cartelle[i])) # Creo i giocatori
                                                                                                        # con il loro nome
                                                                                                        # e le loro cartelle
    lista_giocatori.append(player) # Aggiungo i giocatori alla lista_giocatori
    print(f"Il giocatore {nomi_giocatori[i]} ha {numero_cartelle[i]} cartelle.")
    
    
#crea l'oggetto busta da cui estrarre i numeri
busta = busta()
# creazione oggetto tabellone
tabellone=tabella()
# niente_segno = 0
segno = 0

#Tabellone
p = tabellone.valori_tab
print('Tabellone:')
print(f'{p}')

#inizia l'estrazione dei numeri e il controllo delle cartelle man mano che escono i numeri
print("Iniziamo. Premi INVIO per estrarre un numero.")
while True:
    input("")
    numero_estratto = busta.estraggo()
    print(f"il numero estratto è {numero_estratto}")
# agg Tabellone


    tabellone.aggiungi_numero(numero_estratto)
    sommrg = tabellone.sommanum_riga
    sommct = tabellone.sommanum_cartella
    b = tabellone.posizione_riga
    g = tabellone.posizione_colonna
    if sommrg == 2 and segno == 0:
            print(f'Il tabellone ha fatto ambo alla riga:  {b+1}')
            print(p[b])
            segno += 1
    elif sommrg == 3 and segno == 1:
            print(f'Il tabellone ha fatto terno alla riga:  {b+1}')
            print(p[b])
            segno += 1
    elif sommrg == 4 and segno == 2:
            print(f'Il tabellone ha fatto quaterna alla riga:  {b+1}')
            print(p[b])
            segno += 1
    elif sommrg == 5 and segno == 3:
            print(f'Il tabellone ha fatto cinquina alla riga : {b+1}')
            print(p[b])
            segno += 1
    elif sommct == 15 :
            print(f'Il tabellone ha fatto Tombola nella cartella : {g+1}')
            print(p[3*g:3*(g+1)])
            sys.exit()
            
#aggiorna le cartelle dei giocatori

    for giocatore in lista_giocatori:
        risultati_giocatore = giocatore.controlla_risultati(numero_estratto)
        for risultato in risultati_giocatore:
            if risultato != "niente":
                print(f"{giocatore.nome} ha fatto {risultato}")
                

            

    # se qualcuno ha fatto tombola termina il gioco
            if risultato.startswith('tombola'): 
                print("")
                print(f"E' stata fatta tombola da {giocatore.nome}")
                sys.exit()
        
    print("Premi INVIO per estrarre un nuovo numero.")

        
        
        
        

