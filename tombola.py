# -*- coding: utf-8 -*-
"""
Modificato on Thu Oct 25 12:15:54 2022
@author: Francesco & Orlando
"""


import sys
import random
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

pvincite = ['nullo', 'ambo', 'terna', 'quaterna', 'cinquina', 'tombola']



def selezione_vincite(ris_new, ris_old):
    
    if pvincite.index(ris_new) > pvincite.index(ris_old):       
        return True
    else:
        return False


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


for i in range(len(numero_cartelle)):
    if numero_cartelle[i] > 6:
        print(f"{numero_cartelle[i]} cartelle sono troppe, il massimo per ogni giocatore è 6.")
        sys.exit()
        

#assegna le cartelle richieste da ogni giocatore
lista_giocatori = []

    
for i in range(len(nomi_giocatori)):
    gruppo_cartelle = gruppo_di_cartelle()
    lista_giocatori1 = ["giocatore_"+str(i+1)]
    lista_giocatori1 = giocatore(f"{nomi_giocatori[i]}", 
                                                 random.sample(gruppo_cartelle.crea_gruppo_cartelle(), 
                                                               numero_cartelle[i]))
    lista_giocatori.append(lista_giocatori1)
    print(f"Il giocatore {nomi_giocatori[i]} ha {numero_cartelle[i]} cartelle.")
    
    
#crea l'oggetto busta da cui estrarre i numeri
busta = busta()
# creazione oggetto tabellone
tabellone=tabella()
# niente_segno = 0

#Tabellone
print('Tabellone:')
print(tabellone.valori_tab)


#inizia l'estrazione dei numeri e il controllo delle cartelle man mano che escono i numeri
risultato_successivo= 'nullo'
vincitore = ''
giocatore = []
giocotabb=0
print("Iniziamo. Premi INVIO per estrarre un numero.")
while True:
    input("")
    numero_estratto = busta.estraggo()
    print(f"il numero estratto è {numero_estratto}")
    
#aggiorno le vincite del tabellone
    risTest = False
    risultato = tabellone.aggiungi_numero(numero_estratto)
    Test = selezione_vincite(risultato, risultato_successivo)
    if Test:
        risultato_successivo = risultato
        vincitore = 'Il tabellone'
        risTest = True
        giocotabb=0
          
#aggiorno le vincite dei giocatori

    
    for giocatore in lista_giocatori:
        risultato = giocatore.controlla_risultato(numero_estratto)
        Test= selezione_vincite(risultato, risultato_successivo)
        if Test:
            risultato_successivo=risultato  
            vincitore = f'Il giocatore {giocatore.nome}' 
            risTest = True
            giocotabb += 1
            
# rivela vincita
         
    if risultato_successivo == 'tombola':
            print(f'------- {vincitore} ha fatto: {risultato_successivo} ')
            print('Il gioco è terminato')           
            if giocotabb > 0:
              print('dovresti inserire qui la cartella')
              sys.exit()
            else:
              print(f'nella cartella: {tabellone.stampa_cart}')
              sys.exit()
            
    if risTest:
            print()
            print(f'-------- {vincitore} ha fatto: {risultato_successivo} ')
            if giocotabb > 0:
              print('dovrsti inserire qui la cartella')
            else:
              print(f'alla riga: {tabellone.stampa_riga}')
              print(f'alla riga: {tabellone.stampa_zeri}')
              
            
            
            
    print("Premi INVIO per estrarre un nuovo numero.")

        
        
        
        

