import math as m
import numpy as np


#wartości własne i wektory własne
#Av=lambdav
#A - macierz kwadratowa
#v - wektor
#Av-lambdav=0
#Av-lambdaIv=0
#(A-lambdaI)v=0
#|A-lambdaI|=0

#Av=lambdav
#(Av)^H=(lambdav)^H
#V^H A^H = lambda^H v^H 
#v^H A=lambda^H v^H /*v
#v^H Av=lambda^H v^H v
#lambdav^H v = lambda^H v^H v
#lambda= lambda^H

#A0=A
#Ak=QkRk
#Ak+1=RkQk
#Ak+1=RkQk=IRkQk=(QkTQk)RkQk=QkTAkQk=Qk^-1AkQk


def q(a):
    vl=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
    ul = []
    q = []
    
    for v in vl:
        v = np.array(v)
        sum = 0
        for u_x in ul:
            u_x = np.array(u_x)
            sum+=(np.dot(v.T,u_x)/np.dot(u_x.T,u_x))*u_x
        u = v - sum
        ul.append(u)
        if m.sqrt(np.dot(u.T,u))==0:
            e=u
        else:
            e = (1/m.sqrt(np.dot(u.T,u)))*u
        q.append(e)
    return np.array(q).T

def r(a):
    r=np.dot(q(a).T,a)
    return r
def wartwl(a):
    for i in range(20):
        a = np.dot(r(a),q(a))
    return np.diag(a)
a=np.array([[2.,1.,3.],[1.,6.,7.],[3.,7.,9.],])
print("===== Q =====")
print(np.round(q(a),decimals=3))
print("===== R =====")
print(np.round(r(a),decimals=3))
w1 = wartwl(a)
print("===== Wartosci Wlasne =====")
print(np.round(w1,decimals=3))
