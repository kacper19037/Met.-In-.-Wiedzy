import numpy as np
import math as m

def q(a):
    v_list=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
    u_list = []
    q = []
    
    for v in v_list:
        v = np.array(v)
        sum = 0
        for u_x in u_list:
            u_x = np.array(u_x)
            sum+=(np.dot(v.T,u_x)/np.dot(u_x.T,u_x))*u_x
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
    for i in range(20):
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
    E = np.eye(a.shape[1])
    for i in range(len(a)):
        X = wartwl(a)[i]
        X = X*E
        a1 = a-X
        a1 = np.append(a1, newc, axis=1)
        a1 = np.delete(a1,i,0)
        a1 = gauss_el(a1)+[1]
        print("===== Wektor%d =====" %(i+1))
        print(np.round(a1,decimals=3))

a=np.array([[2.,1.,3.],[1.,6.,7.],[3.,7.,9.],])


wektwl(a)
#https://matrixcalc.org/pl/vectors.html#eigenvectors(%7B%7B2,1,3%7D,%7B1,6,7%7D,%7B3,7,9%7D%7D)
b=np.array([[12.,5.,6.],[2.,4.,6.],[37.,8.,0.],])
wektwl(b)
#https://matrixcalc.org/pl/vectors.html#eigenvectors(%7B%7B12,5,6%7D,%7B2,4,6%7D,%7B37,8,0%7D%7D)
