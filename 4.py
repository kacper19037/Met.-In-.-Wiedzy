import math as m
import numpy as np
# W oparciu o operacje wektorowe proszę napisać funkcję do obliczania średniej arytmetycznej oraz wariancji i odchylenia standardowego

aust = []
with open("australian.dat","r") as file:
    aust = [list(map(lambda i: float(i),line.split())) for line in file]
    
def srednia_aryt(lista):
    suma = 0
    for i in lista:
        suma+=i
    return float(suma/len(lista))

def wariancja(lista):
    srednia = srednia_aryt(lista)
    suma= 0
    for i in lista:
        suma+= (i - srednia)**2
    return float(suma/len(lista))

def odchylenie_stand(lista):
    return m.sqrt(wariancja(lista))



aust2 = [x[:14] for x in aust]
print("Średnia arytmetyczna: ",srednia_aryt(aust2[0]))
print("Wariancja: ",wariancja(aust2[0]))
print("odchylenie stand: ",odchylenie_stand(aust2[0]))
#według wykładu
def srednia_arytm2(lista):
    ones = np.ones((len(lista),1))
    l1=np.array(lista)
    return float(1/len(l1))*np.dot(l1,ones)[0]

def wariancja2(lista):
    srednia=srednia_aryt(lista)
    l1=np.array(lista)
    a=l1-srednia
    return float(np.dot(a, a)/(float(len(lista))))
def odchylenie_stand2(lista):
    return m.sqrt(wariancja2(lista))
print("=========według wykładu=======")
print("Średnia Arytmetyczna: ",srednia_arytm2(aust2[0]))
print("Wariancja: ",wariancja2(aust2[0]))
print("Odchylenie stand: ",odchylenie_stand2(aust2[0]))
#PD
#(2,1)
#(5,2)
#(7,3)
#(8,3)
#B=(XTX)^-1 *XTY) T- transponowana
#wyniki [2/7, 5/14]Yi
macierz = []
with open("macierz.txt","r") as file:
    macierz = [list(map(lambda a: float(a),line.split())) for line in file]
x=np.array(macierz)
print("Macierz:")
print(x)

def regresjalin(x):
    m_x=np.array([[1,i[0]]for i in x])
    m_y=np.array([i[1]for i in x])
    xtx= np.dot(m_x.T,m_x) #XTX
    xtxodw=np.linalg.inv(xtx) #(XTX)^-1
    xtxodwx=np.dot(xtxodw,m_x.T) #(XTX)^-1 * XT
    return np.dot(xtxodwx,m_y) #(XTX)^-1 * XTY

print("Regresja lin",regresjalin(x))
#13.04.2022 
#rozkład macierzy na QR:
#1.stworzenie macierzy ortogonalnej(Ortogonalizacja Grama-Schmidta)
#proj u(v)= (<u,v>/<u,u>)*u
#2.QR = QQTA=(QQT)TTA=(QTQ)TA=ITA=A (w drugą strone)
a = np.array([[2,0],[0,1],[1,2]])
def qr(a):
    v_list=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
    v_list=np.array(v_list)
    v1=v_list[0] #u1
    v2=v_list[1]
    projuV=(np.dot(v2.T,v1)/np.dot(v1.T,v1))*v1
    u2=v2-projuV
    e1=v1/m.sqrt(np.dot(v1.T,v1))
    e2=u2/m.sqrt(np.dot(u2.T,u2))
    q=np.array([e1,e2])
    r=np.dot(q,v_list.T)
    return q,r
q,r=qr(a)
print("===== Q =====")
print(q)
print("===== R =====")
print(r)
