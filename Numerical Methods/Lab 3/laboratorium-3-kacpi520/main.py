import numpy as np
import scipy
import pickle
import math
from typing import Union, List, Tuple
import matplotlib as plt
import matplotlib.pyplot as plt



def p_diff(n: int, c: float) -> float:
    b = 2 ** n
    P1 = b - b + c
    P2 = b + c - b
    P = abs(P1 - P2)
    return P
n = np.arange (1,50,1)
c = [0.1,0.125, 0.25, 0.33, 0.5, 0.6]
for i in c:
    tab = []
    for j in n:
        tab.append(p_diff(j,i))
    plt.figure()
    plt.plot(n, tab, linestyle ='none', marker = 'o',label ='c = ' + str(i))
    plt.xlabel('n')
    plt.ylabel('Wynik')
    plt.legend()
    plt.title('Wartość funkcji p_diff')
plt.show()
 
#2
def exponential(x: Union[int, float], n: int) -> float:
    exp_aprox = 0
    for i in range (n):
        exp_aprox += (1/math.factorial(i))*x**i
    if x > 0 and i > 0: 
        return exp_aprox
    else:
        return 'Nan'
print (exponential(2,20))
print (np.e**2)

def coskx1(k: int, x: Union[int, float]) -> float:
    if k < 0:
        return 'Nan'
    if k == 0:
        return 1
    if k == 1:
        return np.cos(x)
    else:
        return 2*np.cos(x) * coskx1(k-1,x) - coskx1(k-2,x)

def coskx2(k: int, x: Union[int, float]) -> Tuple[float, float]:
    if k == 0:
        return [1,0]
    if k == 1:
        return [np.cos(x),np.sin(x)]
    else:
        def sinkx (k : int, x:Union[int,float]) -> float:
            if k == 1:
                return np.sin(x)
            else:
                return np.sin(x)*coskx2(k-1,x)[0] + np.cos(x) * sinkx(k-1,x)
        return [np.cos(x)*coskx2(k-1,x)[0] - np.sin(x) * sinkx(k-1,x), sinkx(k,x)]

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
tab = []
for i in x:
    tab.append(coskx1(2,i))
plt.figure()
plt.plot (x,tab)
plt.title("Wykres cosinusa rysowany metodą 1")
plt.xlabel('x')
plt.ylabel('Wartość funkcji')
plt.show()

tab = []
for i in x:
    tab.append(coskx2(1,i))
plt.figure()
plt.title("Wykres cosinusa i sinusa rysowany metodą 2")
plt.plot (x,tab, label = ['cosinus','sinus'])
plt.xlabel('x')
plt.ylabel('Wartość funkcji')
plt.legend()
plt.show()

#4
