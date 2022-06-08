import math as m
from multiprocessing.dummy import Array
import numpy as np
from pandas import array


#Wartości singularne:
#[1 1 1 1 1 1 1 1]
#[1 1 1 1 -1 -1 -1 -1]
#[1 1 -1 -1 0 0 0 0]
#[0 0 0 0 1 1 -1 -1]
#[1 -1 0 0 0 0 0 0]
#[0 0 1 -1 0 0 0 0]
#[0 0 0 0 1 -1 0 0]
#[0 0 0 0 0 0 1 -1]



a=np.array([[1.,1.,1.,1.,1.,1.,1.,1.],[1.,1.,1.,1.,-1.,-1.,-1.,-1.],
[1.,1.,-1.,-1.,0.,0.,0.,0.],[0.,0.,0.,0.,1.,1.,-1.,-1.],[1.,-1.,0.,0.,0.,0.,0.,0.]
,[0.,0.,1.,-1.,0.,0.,0.,0],[0.,0.,0.,0.,1.,-1.,0.,0.],[0.,0.,0.,0.,0.,0.,1.,-1.]])
b=np.array([8.,6.,2.,3.,4.,6.,6.,5.])
aort=np.dot(a,a.T)
print(aort)

#[8.,6.,2.,3.,4.,6.,6.,5.]T
def normalizacja(a):
    for x in range(len(a[0])):
        a[x]=a[x]/m.sqrt(np.dot(a[x],a[x].T))
    return a
anorm = normalizacja(a)
print(np.round(anorm,decimals=3))
ab=np.dot(anorm,b)
print(np.round(ab,decimals=3))
#Sigmai=pierwiastek(lambdai)
#(Avi)/(sigmai)=U
#Dekompozycja a=USigmaV^T
#U-lewe wektory własne(Zawsze kwadratowa)
#V-prawe(Zawsze kwadratowa)
#Sigma- wartosci singularne(taka sama jak A)
#A=[1 2 0]
#  [2 0 2]
#1.
#    [5 2]
#AAT=[2 8] wielomian charakterystyczny to wielomian za pomocą którego obliczymy wartosci wlasne
#
#2.wyznacznik z:
#[5-lambda 2]    lambda=X
#[2  8-lambda]=(5-X)(8-X)-4=X^2-13X+36=delta=25 X1=9 X2=4
#3.
#sigma1=pierwiastek lambda=3
#sigma2=pierwiastek lambda=2
#4.
#AA^Tu1-lambda1u1=0
#(AA^T-lambda1I)u1=0
#(AA^T-9I)u1=0
#dla lambdy=9
#[5-9 2][u1^1]
#[2 8-9][u1^2]=0

#[-4 2][u1^1]
#[2 -1][u1^2]=0

#u1^1=1
#u1^2=2

#u1=alfa[1 2]^T

#dla lambdy=4
#[5-4 2][u2^1]
#[2 8-4][u2^2]=0

#[1 2][u2^1]
#[2 4][u2^2]=0

#u2^1=2
#u2^2=-1

#u2=alfa[2 -1]^T
#5.
#u1=alfa[1 2]
#u1=1/pierw(5) [1 2]T

#u2=alfa[2 -1]
#u2=1/pierw(5) [2 -1]T

#6.   [1 2] [1 2 0]  [5 2 4]
#A^TA=[2 0] [2 0 2] =[2 4 0] 
#     [0 2]          [4 0 4]
#X-lambda
#(A^TA-XI)v=0
#[5-X 2 4]
#[2 4-X 0]=(5-X)(4-X)(4-X)- 16(4-X)-4(4-X)=(5-X)(4-X)(4-X)-20(4-X)=(4-X)((5-X)(4-X)-20)=0
#[4 0 4-X]                                                          =X^2-9X=0
#X=0, X=9, X=4
#sigma1=3, sigma2=2
#7.
#dla X=9
#[5-9 2 4] [v1^1]
#[2 4-9 0] [v1^2]=0
#[4 0 4-9] [v1^3]
#robimy to samo co poprzednio
#2v1^1=5v1^2
#4v1^1=5v1^3
#v1^1=5
#v1^2=2
#v1^v3=4
#v1=alfa[5 2 4]^T
#v1=(1/3pierw(5))[5 2 4]^T
#v2=1/pierw(5)[0 2 -1]^T
#v3=1/3[-2 1 2]^T
#v to kolumny          [1  2][3 0 0]         [ 5 2  4] [5/3pier5 2/3pierw5 4/3pierw5]
#A= usigmav^T=1/pierw5 [2 -1][0 2 0]1/3pierw5[ 0 2 -1]=[0        2/pierw5 -1/pierw5 ]
                                           #[-2 1  2] [-2/3     1/3       2/3      ]     




#A=[1 2 0]
#  [2 0 2]
an=np.array([[1.,2.,0.], [2.,0.,2.],])

def proj(u_x,v):
    return np.dot(v.T,u_x)/np.dot(u_x.T,u_x)*u_x

def q(a):
    v_list=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
    u_list = []
    q = []
    for v in v_list:
        v = np.array(v)
        sum = 0
        for u_x in u_list:
            u_x = np.array(u_x)
            sum+=proj(u_x,v)
        u = v - sum
        u_list.append(u)
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
    a_k=a
    for i in range(100):
        a_k = np.dot(r(a_k),q(a_k))
    return np.diag(a_k)

def gauss_el(a):
    n=len(a.T[0])
    for i in range(n):
        if a[i][i] == 0.0:
            raise ZeroDivisionError(("Nie mozna dzielic przez 0")) 
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]
                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    x = [a[i][n]/a[i][i]*(-1) for i in range(n)]
    return x

def wektwl(a):
    newc = np.zeros((len(a),1))
    wektwl= np.array(a)
    E = np.eye(a.shape[1])
    for i in range(len(a)):
        X = wartwl(a)[i]
        X = X*E
        a1 = a-X
        a1 = np.append(a1, newc, axis=1)
        a1 = np.delete(a1,i,0)
        a1 = gauss_el(a1)+[1]
        wektwl[i]=np.round(a1,decimals=3)
    return wektwl.T

def u(a):
    uw=-np.sort(-wartwl(a))    #wartosci wlasne dla u sortowane od najwiekszego
    newc = np.zeros((len(a),1))
    wektwl= np.empty_like(a)
    E = np.eye(a.shape[1])
    for i in range(len(a)):
        X = uw[i]
        X = X*E
        a1 = a-X
        a1 = np.append(a1, newc, axis=1)
        a1 = np.delete(a1,i,0)
        a1 = gauss_el(a1)+[1]
        wektwl[i:]=a1
    return normalizacja(wektwl)
def sigma(a):
    w=-np.sort(-wartwl(a))    #wartosci wlasne dla u sortowane od najwiekszego
    E = np.eye(2)
    s=np.sqrt(w)*E     #sigma
    s = np.c_[ s, np.zeros(2) ] #dodanie kolumny zerowej
    return s

def svd(a):
    mu=np.dot(a,a.T) #AA^T
    mv=np.dot(a.T,a) #A^TA
    s=sigma(mu)
    mu=u(mu)
    mv=u(mv)
    return mu, s, mv
print("SVD: ")
u,s,v=svd(an)
print("U:")
print(u)
print("Sigma:")
print(s)
print("V:")
print(v)
    
