import math as m
import random

import numpy as np

def f(x):
    return 1-(x**2)
def punkty(x, y):
    if ( y > 0) and (y <= f(x)):
        return 1
    elif ( y > 0) and (y <= f(x)):
        return -1
    return 0
def randPuntk(a, b):
    return  a + random.uniform(0, 1) * (b-a)
def monteCarlo(xp, xk, dokl):
    n= dokl * 100
    yp = 0
    yk = m.ceil(max(f(xp), f(xk)))
    pointsIn = 0
    for i in range(int(n)):
        pointsIn = pointsIn + punkty(randPuntk(xp,xk),randPuntk(yp, yk))
    calka = (pointsIn / n) * ((xk-xp) * (yk-yp))
    print("Wartosc calki wynosi w przyblizeniu ", np.round(calka,decimals=3))
#xp- poczatek przedzialu
#xk - koniec przedzialu
#dokl - dokladnosc calkownia
monteCarlo(0,2,5)
