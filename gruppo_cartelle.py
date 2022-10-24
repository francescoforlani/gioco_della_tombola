# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:28:57 2022

@author: Franc
"""

import numpy as np
import random
import sys
from cartella import Cartella



class gruppo_di_cartelle:
    
    def __init__(self):
        pass
        
    def crea_gruppo_cartelle(self):
        # La creazione di 6 cartelle diverse avviene in 5 passaggi:
            
        # 1) Creo 9 intervalli, i numeri di ogni intervallo potranno essere messi all'interno
        # di una precisa colonna delle cartelle. Ad esempio i numeri dell'intervallo che
        # va da 1 a 9 potranno essere inseriti solo nella prima colonna delle cartelle.
        # C'è quindi una corrispondenza tra intervallo e colonna.
        
        intervallo_colonna_1 = list(range(1, 10))
        intervallo_colonna_2 = list(range(10, 20))
        intervallo_colonna_3 = list(range(20, 30))
        intervallo_colonna_4 = list(range(30, 40))
        intervallo_colonna_5 = list(range(40, 50))
        intervallo_colonna_6 = list(range(50, 60))
        intervallo_colonna_7 = list(range(60, 70))
        intervallo_colonna_8 = list(range(70, 80))
        intervallo_colonna_9 = list(range(80, 91))
        
        lista_intervalli = [intervallo_colonna_1,intervallo_colonna_2,intervallo_colonna_3, # Variabile di tipo lista che contiene i 9 intervalli
                            intervallo_colonna_4,intervallo_colonna_5,intervallo_colonna_6,
                            intervallo_colonna_7,intervallo_colonna_8,intervallo_colonna_9]
        
        numeri_rimasti = list(range(1,91)) # Variabile che mi serve a controllare quali numeri mancano da assegnare
        
        numeri_cartelle = [] # Variabile di tipo lista che mi servirà per contenere 6 liste, queste 6 liste sono composte dai numeri
                             # che mano mano vado ad assegnare alle 6 cartelle del mio gruppo_cartelle.
        
        # 2) Assegno ad ogni cartella un numero per ogni intervallo (cioè colonna)
        # Dopo questo passaggio le cartelle hanno preso un numero da ogni intervallo (quindi avranno un numero per ogni colonna)

        for i in range(1, 7): # Per ognuna delle 6 cartelle del gruppo_cartelle
            numeri_singola_cartella = [] # Creo una variabile di tipo lista che mi serve a contenere i numeri che vado a prendere randomicamente
            for j in range(len(lista_intervalli)): # Per ognuno dei 9 intervalli che abbiamo definito
                n = random.choice(lista_intervalli[j]) # Pesco un numero in modo randomico
                lista_intervalli[j].remove(n) # rimuovo quel numero dall'intervallo da cui l'ho pescato
                numeri_rimasti.remove(n) # lo rimuovo anche dalla variabile che mi controlla i numeri rimasti
                numeri_singola_cartella.append(n) # e lo aggiungo alla lista dei numeri presi
                
            numeri_cartelle.append(numeri_singola_cartella) # aggiungo la lista dei numeri presi. Questa variabile contiene quindi adesso 
                                                            # 6 liste di 9 numeri.
                
        # 3) Assegno randomicamente ad ogni cartella altri 3 numeri facenti parte di 
        # intervalli diversi. Dopo questo passaggio le cartelle hanno preso almeno un numero
        # da ogni intervallo e due numeri da tre intervalli.
        
        for i in range(0, 6): # Per ognuna delle 6 cartelle del gruppo_cartelle
            numeri_singola_cartella = [] # Riazzero la variabile che mi tiene conto dei numeri che vado a prendere randomicamente
            for m in lista_intervalli: # Ciclo che controlla se qualche intervallo è rimasto senza numeri, se lo trova lo elimina dalla lista_intervalli 
                if len(m) == 0:
                    lista_intervalli.remove(m)
            lista_intervalli_temp = random.sample(lista_intervalli, 3) # Creo una variabile che contiene tre intervalli presi in modo randomico
                                                                       # dalla lista intervalli
            for intervallo in lista_intervalli_temp: # Per ognuno dei 3 intervalli presi randomicamente            
                n = random.choice(intervallo) # prendo un numero random
                numeri_singola_cartella.append(n) # lo aggiungo alla lista dei numeri presi
                numeri_rimasti.remove(n) # lo rimuovo dalla variabile che mi controlla i numeri che rimangono
                
                for l in range(len(lista_intervalli)): # Ciclo che serve a rimuovere il numero n anche dall'intervallo da cui è stato preso
                    if n in lista_intervalli[l]:
                        lista_intervalli[l].remove(n)
            
            for numero in numeri_singola_cartella: # Ciclo che aggiunge i numeri presi alla variabile numeri_cartelle che tiene conto dei numeri 
                                                   # di ogni cartella
                numeri_cartelle[i].append(numero)
                
            numeri_cartelle[i].sort() # Metto in ordine crescente i numeri di ogni cartella
                
        # 4) Assegno randomicamente ad ogni cartella gli ultimi 3 numeri da intervalli diversi.
        # Rimangono da assegnare 18 numeri che sono divisi in 6 o più intervalli.
        # Devo far sì che per ogni cartella restino almeno 3 intervalli diversi da poter scegliere 
        # altrimenti, se prendessi 2 numeri dallo stesso intervallo potrei ottenere una cartella con 
        # più di 3 numeri su una colonna (quando il massimo consentito è 3).
        # Per fare ciò, per ogni cartella prendo 3 numeri dai 3 intervalli con più numeri rimasti (cioè i 3 intervalli con lunghezza massima),
        # fino a quando rimarranno soltanto 3 numeri in 3 intervalli diversi, che verranno 
        # assegnati all'ultima cartella delle 6.
        # Dopo questo passaggio le cartelle hanno da 1 a 3 numeri per intervallo, per un totale
        # di 15 numeri a cartella.
        
        for i in range(0,6): # Per ognuna delle 6 cartelle del gruppo_cartelle
            numeri_singola_cartella = [] # Riazzero la variabile che mi tiene conto dei numeri che vado a prendere randomicamente
            lista_indici_presi = [100] # Creo una lista che, tenendo conto degli indici degli intervalli, mi dice da quali intervalli ho già
                                       # pescato un numero. Perchè, come abbiamo detto, per la stessa cartella non posso prendere due numeri 
                                       # dallo stesso intervallo, altrimenti rischio che abbia 4 numeri sulla stessa colonna (quando il limite è 3).
                                       # E' inizializzata con un numero a caso per non restituire errore
            numeri_presi = 0 # Creo variabile che mi tiene conto di quanti numeri ho preso
            while numeri_presi < 3: # Fintanto che ho preso meno di 3 numeri
                lunghezza_intervalli = [] # Creo variabile che mi serve a tenere conto della lunghezza degli intervalli
                for intervallo in lista_intervalli: # Per ogni intervallo di numeri rimasto
                    lunghezza_intervalli.append(len(intervallo)) # aggiungi la sua lunghezza alla variabile appena creata
                max_len = max(lunghezza_intervalli) # prendo la lunghezza massima 
                second_max_len = sorted(lunghezza_intervalli)[-2] # prendo la seconda lunghezza massima 
                third_max_len = sorted(lunghezza_intervalli)[-3] # prendo la terza lunghezza massima 
                
                # A questo punto ho visto quali sono gli intervalli più lunghi, però potrei avere intervalli con la stessa lunghezza e questo mi 
                # porta problemi quando devo pescare un numero da loro. Quindi aggiungo delle quantità alla loro lunghezza in modo da 
                # avere lunghezze tutte diverse. Esempio: [1, 4, 4, 3, 2, 2] --> [1.4, 4.9, 4.8, 3.7, 2.6, 2.5]
                
                max_index = lunghezza_intervalli.index(max_len) # prendo l'indice corrispondente alla unghezza massima
                lunghezza_intervalli[max_index] = lunghezza_intervalli[max_index] + 0.9 
                
                second_max_index = lunghezza_intervalli.index(second_max_len)
                lunghezza_intervalli[second_max_index] = lunghezza_intervalli[second_max_index] + 0.8
                
                third_max_index = lunghezza_intervalli.index(third_max_len)
                lunghezza_intervalli[third_max_index] = lunghezza_intervalli[third_max_index] + 0.7
                
                
                # Ora che ho delle lunghezze tutte diverse, posso iniziare a pescare randomicamente dei numeri a partire dagli intervalli 
                # più lunghi: (da notare che l'intervallo da cui ho pescato un numero nell'iterazione x potrebbe continuare ad essere il più lungo
                # anche nell'iterazione x+1, per questo ho bisogno di tenere conto anche del secondo e del terzo intervallo più lungo)
                
                if max_index not in lista_indici_presi: # Controllo che non ho già preso un numero dall'intervallo più lungo.
                    n = random.choice(lista_intervalli[max_index]) # prendo un numero random
                    numeri_singola_cartella.append(n) # aggiungo il numero alla solita variabile dei numeri presi
                    lista_intervalli[max_index].remove(n) # lo rimuovo dall'intervallo da cui l'ho preso
                    numeri_rimasti.remove(n) # lo rimuovo dalla variabile dei numeri rimasti
                    numeri_presi += 1 # aggiorno il contatore
                    lista_indici_presi.append(max_index) # inserisco l'indice dell'intervallo da cui ho preso il numero all'interno della 
                                                         # variabile lista_indici_presi
                elif second_max_index not in lista_indici_presi: # Controllo che non ho già preso un numero dal secondo intervallo più lungo.
                    n = random.choice(lista_intervalli[second_max_index])
                    numeri_singola_cartella.append(n)
                    lista_intervalli[second_max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(second_max_index)
                elif third_max_index not in lista_indici_presi: # Controllo che non ho già preso un numero dal terzo intervallo più lungo.
                    n = random.choice(lista_intervalli[third_max_index])
                    numeri_singola_cartella.append(n)
                    lista_intervalli[third_max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(third_max_index)
                else:
                    print("errore nel consegnare le cartelle") # via di fuga dal loop
                    sys.exit()
                
        
            for numero in numeri_singola_cartella: # aggiungo i numeri presi alla variabile numeri_cartelle
                numeri_cartelle[i].append(numero)
                
            numeri_cartelle[i].sort() # metto i numeri di ogni cartella in ordine crescente
       
        # 5) Adesso le nostre cartelle sono delle semplici liste contenenti ognuna 15 numeri.
        # Per prima cosa rendo ognuna di queste liste un oggetto di tipo cartella e poi distribuisco al suo interno
        # i 15 numeri, rispettando la corrispondenza tra l'intervallo da cui è stato preso 
        # ogni numero e la rispettiva colonna in cui dovrà stare. Ad esempio il numero 22 
        # dovrà per forza stare nella terza colonna della cartella.
        # Inoltre, devo distribuirli in modo che ce ne siano 5 per riga. (Il vincolo 
        # "minimo 1 numero per colonna e massimo 3 numeri per colonna" è stato già rispettato
        # in quanto sono stati presi da 1 a 3 numeri per intervallo.)
        # Dopo questo passaggio ottengo finalmente 6 cartelle rispettanti i vincoli dati.  


            def posiziona_numero(contatore, cartella, n = int):
                # Funzione che prende in ingresso:
                # - un numero;
                # - un oggetto di tipo cartella (matrice 3x9) in cui dovrò inserire il numero secondo determinate condizioni;
                # - il contatore che mi serve per misurare quanti numeri ho messo in ogni riga della cartella;
                # Restituisce il contatore aggiornato.
                lista_condizioni = [n in range(0,10), n in range(10,20), n in range(20,30), n in range(30,40), n in range(40,50),
                                    n in range(50,60), n in range(60,70), n in range(70,80), n in range(80,90)] # Queste sono le 9 condizioni 
                                                                                                                # relative alle 9 colonne della 
                                                                                                                # cartella.
                for condizione in lista_condizioni: # Scorro le 9 condizioni                 
                    if condizione: # Quando la condizione è soddisfatta allora procedo ad inserire il numero in quella colonna
                        indice_condizione = lista_condizioni.index(condizione) # Prendo l'indice della condizione che corrisponde alla colonna 
                                                                               # della cartella in cui dovrò inserire il numero
                        for row in range(0,3): # Scorro le 3 righe della colonna
                            condition_2 = contatore[row+1] >= contatore[row+2] <= contatore[row+3] and contatore[row] >= contatore[row+2] <= contatore[row+4]
                            # Questa seconda condizione è vera se la riga che prendo in considerazione ha meno numeri o lo stesso numero di numeri delle altre righe
                            # Quindi vado a mettere il numero nella riga che fin'ora ha ricevuto meno numeri.
                            if cartella.caselle[row][indice_condizione] == 0 and condition_2: # Se quest'ultima condizione è vera e la posizione
                                                                                              # non è già occupata da un altro numero
                                cartella.caselle[row][indice_condizione] = n # inserisco il numero nella posizione
                                contatore[row+2] += 1 # aggiorno il contatore
                                break
                    elif n == 90: # condizione specifica per il numero 90
                        cartella.caselle[2][8] = n # che deve essere per forza messo nella casella in basso a destra della cartella
                        contatore[2+2] += 1
                        break
                    
                return contatore              
        

        list_of_element_per_row = [] # Variabile che mi serve a controllare che ogni cartella abbia ricevuto 5 numeri su ogni riga
        gruppo_cartelle = [] # Lista che conterrà le 6 cartelle
        for lista_di_numeri in numeri_cartelle: # Per ognuna delle 6 liste di numeri (che contengono 15 numeri)
            #cartella = np.zeros((3, 9), int)
            cartella = Cartella() # Creo l'oggetto di tipo cartella
            element_per_row = [5, 5, 0, 0, 0, 5, 5]  # Variabile che uso come contatore per misurare (con i tre elementi centrali posti a zero) 
                                                     # quanti numeri andrò a mettere su ogni riga della cartella, gli altri elementi sono messi a 5 in modo
                                                     # che poi la riga non prenda più di 5 numeri                                                                 
            for numero in lista_di_numeri: # Per ogni numero all'interno della lista 
                element_per_row = posiziona_numero(element_per_row, cartella, numero) # Vado a posizionare il numero in modo coerente alle specifiche
                                
                
            list_of_element_per_row.append(element_per_row) # lista di controllo che mi dice quanti numeri ho messo in ogni riga di ogni cartella
                    
            gruppo_cartelle.append(cartella) # Aggiungo la cartella appena creata al gruppo di cartelle
                                
        return gruppo_cartelle
                
                
            
            
        
    
    