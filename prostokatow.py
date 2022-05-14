import numpy as np


def f(x):
    return 1-(x**2)
def prostokatow(xp, xk, dokl):
    calka=0.0
    n=dokl*100
    dx=(xp-xk)/n
    for i in range(n):
        calka=calka+f(xp+i*dx)
    calka=calka*dx
    print("Wartosc calki wynosi w przyblizeniu ", np.round(calka,decimals=3))
#xp- poczatek przedzialu
#xk - koniec przedzialu
#dokl - dokladnosc calkownia
prostokatow(0,2,5)
