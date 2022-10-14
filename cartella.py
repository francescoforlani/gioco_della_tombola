# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:28:57 2022

@author: Franc
"""

import numpy as np
import random
import sys

class gruppo_di_cartelle:
    
    def __init__(self, numero_cartelle = 6):
        self.numero_cartelle = numero_cartelle
        
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
        
        lista_intervalli = [intervallo_colonna_1,intervallo_colonna_2,intervallo_colonna_3,
                            intervallo_colonna_4,intervallo_colonna_5,intervallo_colonna_6,
                            intervallo_colonna_7,intervallo_colonna_8,intervallo_colonna_9]
        
        numeri_rimasti = list(range(1,91))
        
        numeri_cartelle = []
        
        # 2) Assegno ad ogni cartella un numero per ogni intervallo.
        # Dopo questo passaggio le cartelle hanno preso un numero da ogni intervallo.
        
        #for i in range(1, self.numero_cartelle + 1):
        for i in range(1, 7):
            numeri_cartella = []
            for i in range(len(lista_intervalli)):
                n = random.choice(lista_intervalli[i])
                lista_intervalli[i].remove(n)
                numeri_rimasti.remove(n)
                numeri_cartella.append(n)
                
            numeri_cartelle.append(numeri_cartella)
                
        # 3) Assegno randomicamente ad ogni cartella altri 3 numeri facenti parte di 
        # intervalli diversi. Dopo questo passaggio le cartelle hanno preso almeno un numero
        # da ogni intervallo e due numeri da tre intervalli.
        
        #for i in range(1, self.numero_cartelle + 1):
        for i in range(0, 6):
            numeri_cartella = []
            for m in lista_intervalli:
                if len(m) == 0:
                    lista_intervalli.remove(m)
            lista_intervalli_temp = random.sample(lista_intervalli, 3)
            for intervallo in lista_intervalli_temp:            
                n = random.choice(intervallo)
                numeri_cartella.append(n)
                numeri_rimasti.remove(n)
                
                for l in range(len(lista_intervalli)):
                    if n in lista_intervalli[l]:
                        lista_intervalli[l].remove(n)
            
            for numero in numeri_cartella:
                numeri_cartelle[i].append(numero)
                
            numeri_cartelle[i].sort()
                
        # 4) Assegno randomicamente ad ogni cartella gli ultimi 3 numeri da intervalli diversi.
        # Rimangono da assegnare 18 numeri che sono divisi in 6 o più intervalli.
        # Devo far sì che per ogni cartella restino almeno 3 intervalli diversi da poter scegliere 
        # altrimenti, se prendessi 2 numeri dallo stesso intervallo potrei ottenere una cartella con 
        # più di 3 numeri su una colonna (quando il massimo consentito è 3).
        # Per fare ciò, per ogni cartella prendo 3 numeri dai 3 intervalli con più numeri rimasti,
        # fino a quando rimarranno soltanto 3 numeri in 3 intervalli diversi, che verranno 
        # assegnati all'ultima cartella delle 6.
        # Dopo questo passaggio le cartelle hanno da 1 a 3 numeri per intervallo, per un totale
        # di 15 numeri a cartella.
        
        for i in range(0,6):
            numeri_cartella = []
            lista_indici_presi = [100] #numero a caso per non far restituire errore
            #for iterazione in range(0,3):
            numeri_presi = 1
            while numeri_presi < 4: 
                lunghezza_intervalli = []
                for intervallo in lista_intervalli:
                    lunghezza_intervalli.append(len(intervallo))
                max_len = max(lunghezza_intervalli)                
                second_max_len = sorted(lunghezza_intervalli)[-2]
                third_max_len = sorted(lunghezza_intervalli)[-3]
                fourth_max_len = sorted(lunghezza_intervalli)[-4]
                fifth_max_len = sorted(lunghezza_intervalli)[-5]
                sixth_max_len = sorted(lunghezza_intervalli)[-6]
                
                max_index = lunghezza_intervalli.index(max_len)
                lunghezza_intervalli[max_index] = lunghezza_intervalli[max_index] + 0.9
                
                second_max_index = lunghezza_intervalli.index(second_max_len)
                lunghezza_intervalli[second_max_index] = lunghezza_intervalli[second_max_index] + 0.8
                
                third_max_index = lunghezza_intervalli.index(third_max_len)
                lunghezza_intervalli[third_max_index] = lunghezza_intervalli[third_max_index] + 0.7
                
                fourth_max_index = lunghezza_intervalli.index(fourth_max_len)
                lunghezza_intervalli[fourth_max_index] = lunghezza_intervalli[fourth_max_index] + 0.6
                
                fifth_max_index = lunghezza_intervalli.index(fifth_max_len)
                lunghezza_intervalli[fifth_max_index] = lunghezza_intervalli[fifth_max_index] + 0.5
                
                sixth_max_index = lunghezza_intervalli.index(sixth_max_len)
                lunghezza_intervalli[sixth_max_index] = lunghezza_intervalli[sixth_max_index] + 0.4
                
                # Evito che la cartella prenda un numero dallo stesso intervallo di prima
                # tenendo traccia degli intervalli che sono già stati "saccheggiati" di un
                # numero dalla cartella in questione:
                
                if max_index not in lista_indici_presi: 
                    n = random.choice(lista_intervalli[max_index])
                    numeri_cartella.append(n)
                    lista_intervalli[max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(max_index)
                elif second_max_index not in lista_indici_presi:
                    n = random.choice(lista_intervalli[second_max_index])
                    numeri_cartella.append(n)
                    lista_intervalli[second_max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(second_max_index)
                elif third_max_index not in lista_indici_presi:
                    n = random.choice(lista_intervalli[third_max_index])
                    numeri_cartella.append(n)
                    lista_intervalli[third_max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(third_max_index)
                elif fourth_max_index not in lista_indici_presi:
                    n = random.choice(lista_intervalli[fourth_max_index])
                    numeri_cartella.append(n)
                    lista_intervalli[fourth_max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(fourth_max_index)
                elif fifth_max_index not in lista_indici_presi:
                    n = random.choice(lista_intervalli[fifth_max_index])
                    numeri_cartella.append(n)
                    lista_intervalli[fifth_max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(fifth_max_index)
                elif sixth_max_index not in lista_indici_presi:
                    n = random.choice(lista_intervalli[sixth_max_index])
                    numeri_cartella.append(n)
                    lista_intervalli[sixth_max_index].remove(n)
                    numeri_rimasti.remove(n)
                    numeri_presi += 1
                    lista_indici_presi.append(sixth_max_index)
                else:
                    print("errore nel consegnare le cartelle") 
                    sys.exit()
                
        
            for numero in numeri_cartella:
                numeri_cartelle[i].append(numero)
                
            numeri_cartelle[i].sort()
       
        # 5) Adesso le nostre cartelle sono delle semplici liste contenenti ognuna 15 numeri.
        # Per prima cosa rendo la cartella una matrice 3x9 e poi distribuisco al suo interno
        # i 15 numeri, rispettando la corrispondenza tra l'intervallo da cui è stato preso 
        # ogni numero e la rispettiva colonna in cui dovrà stare. Ad esempio il numero 22 
        # dovrà per forza stare nella terza colonna della cartella.
        # Inoltre, devo distribuirli in modo che ce ne siano 5 per riga. (Il vincolo 
        # "minimo 1 numero per colonna e massimo 3 numeri per colonna" è stato già rispettato
        # in quanto sono stati presi da 1 a 3 numeri per intervallo.)
        # Dopo questo passaggio ottengo finalmente 6 cartelle rispettanti i vincoli dati.

        list_of_element_per_row = []
        gruppo_cartelle = []
        for lista_di_numeri in numeri_cartelle:
            cartella = np.zeros((3, 9), int)
            element_per_row = [5, 5, 0, 0, 0, 5, 5] 
            for numero in lista_di_numeri:
                numero_as_string = str(numero)
                if numero_as_string in ["1","2","3","4","5","6","7","8","9"]: 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][0] == 0 and condition:
                            cartella[row][0] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("1") and numero_as_string != "1": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][1] == 0 and condition:
                            cartella[row][1] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("2") and numero_as_string != "2": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][2] == 0 and condition:
                            cartella[row][2] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("3") and numero_as_string != "3": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][3] == 0 and condition:
                            cartella[row][3] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("4") and numero_as_string != "4": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][4] == 0 and condition:
                            cartella[row][4] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("5") and numero_as_string != "5": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][5] == 0 and condition:
                            cartella[row][5] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("6") and numero_as_string != "6": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][6] == 0 and condition:
                            cartella[row][6] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("7") and numero_as_string != "7": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][7] == 0 and condition:
                            cartella[row][7] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string.startswith("8") and numero_as_string != "8": 
                    for row in range(0,3):
                        condition = element_per_row[row+1] >= element_per_row[row+2] <= element_per_row[row+3] and element_per_row[row] >= element_per_row[row+2] <= element_per_row[row+4]
                        if cartella[row][8] == 0 and condition:
                            cartella[row][8] = numero
                            element_per_row[row+2] += 1
                            break
                if numero_as_string == "90":                         
                    cartella[2][8] = numero
                    element_per_row[2+2] += 1
                    break
                
            list_of_element_per_row.append(element_per_row)
                    
            gruppo_cartelle.append(cartella)
                
        for i in range(len(gruppo_cartelle)):
            gruppo_cartelle[i] = gruppo_cartelle[i].tolist()
                
                
        return gruppo_cartelle
                
                
            
            
        
    
    