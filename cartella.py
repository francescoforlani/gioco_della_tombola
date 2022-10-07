# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:28:57 2022

@author: Franc
"""

import numpy as np
import random

class gruppo_di_cartelle:
    
    def __init__(self, numero_cartelle = 6):
        self.numero_cartelle = numero_cartelle
        
    def crea_gruppo_cartelle(self):
        
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
        
        #assegno ad ogni cartella un numero per ogni colonna
        #for i in range(1, self.numero_cartelle + 1):
        for i in range(1, 7):
            numeri_cartella = []
            for i in range(len(lista_intervalli)):
                n = random.choice(lista_intervalli[i])
                lista_intervalli[i].remove(n)
                numeri_rimasti.remove(n)
                numeri_cartella.append(n)
                
            numeri_cartelle.append(numeri_cartella)
                
        #assegno ad ogni cartella altri 3 numeri in colonne diverse
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
                
        #assegno ad ogni cartella gli ultimi 3 numeri in colonne diverse.
        #Devo far sì che per ogni cartella restino 3 intervalli diversi da poter scegliere 
        #altrimenti potrei ottenere una cartella con più di 3 numeri su una colonna (dove
        #il massimo è 3)
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
                max_index = lunghezza_intervalli.index(max_len)
                second_max_index = lunghezza_intervalli.index(second_max_len)
                third_max_index = lunghezza_intervalli.index(third_max_len)
                
                if max_index not in lista_indici_presi: #evito che prenda un numero
                                                                   #dallo stesso intervallo di prima
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
                
        
            for numero in numeri_cartella:
                numeri_cartelle[i].append(numero)
                
            numeri_cartelle[i].sort()
       
        #adesso ho 15 numeri per ogni cartella e devo distribuirli in modo che ce ne
        #siano 5 per riga e da 1 a 3 per ogni colonna
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
                
                
            
            
        
    
    