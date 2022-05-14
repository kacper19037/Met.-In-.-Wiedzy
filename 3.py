import math as m
import numpy as np
import random as rand

aust=[]
with open('australian.dat','r') as file:
    for line in file:
        aust.append(list(map(lambda x: float(x),line.split() )))
for x in range(6):
    print(aust[x])

#stwórz tablice z nazwami miast np: gdańsk, poznań, warszawa, sosnowiec
miasta=['Gdańsk','Poznań','Warszawa',"Sosnowiec"]
result = list(map(lambda x: x[:3], miasta))

print(result)
#Metryka Euklidesowa
#pierwiastek(Suma(Xi-Yi)^2)
def metryka(l1, l2):
    suma = 0
    for i in range(len(l1)-1):
        suma+=(l1[i]-l2[i])**2
    return m.sqrt(suma)
print("Metryka:",metryka(aust[0],aust[1]))

#Pogrupować względem klasy decyzyjnej
def grupuj(lista):
    grupy = dict()
    for i in lista:
        if i[0] in grupy.keys():
            grupy[i[0]].append(i[1])
        else:
            grupy[i[0]] = [i[1]]
    return grupy

print("Grupowanie:",grupuj(aust))

#K najblizszych sąsiadów
def knn(lista, row, num):
    knn = dict()
    for i in range(len(lista)):
        dist = lista[i][num]
        if dist in knn.keys():
            knn[dist].append(metryka(row, lista[i]))
        else:
            knn[dist]=[metryka(row, lista[i])]      
    return knn

knn1 = knn(aust,[1,1,1,1,1,1,1,1,1,1,1,1,1,1], 14 )
print("K najblizszych sąsiadów: ",knn1[0][:5])


# PD minimalna odległość
def minimalna(slownik):
    klucze = list(slownik.keys())
    klucz = klucze[0]
    ile = 0
    min = slownik[klucze[0]]
    for i in klucze[1:]:
        if min > slownik[i]:
            min = slownik[i]
            klucz = i
            ile=0
        elif min == slownik[i]:
            ile+=1
    if ile > 0:
        return 
    return klucz
#test={1.2:0,1.4:1,1.1:2}
#print("Minimalna odległość",minimalna(test))



def metryka2(l1,l2):
    v1 = np.array(l1)
    v2 = np.array(l2)
    a = v2-v1
    return m.sqrt(np.dot(a, a))

#print(metryka2(aust[0], aust[1]))
