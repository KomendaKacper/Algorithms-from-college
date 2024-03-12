#1
import math
import numpy as np

def cylinder_area(r:float,h:float) -> float:
    
    try:
        if r <= 0 or h <= 0:
            return float('nan')
        pole = float(r * r * math.pi*2  + 2*h*np.pi*r)
        return pole
    except:
        return float('nan')

#2
a = np.linspace(0,10,7)
print (a)

b = np.arange(0, 10, 0.25)
print (b)

#3
def fib(n:int):
    try:
        if n <= 0:
            return None    
        elif n == 1:
            return [1]
        elif n == 2:
            return [1,1]
        else:
            tab = [1,1]
            for i in range (2, n):
                tab.append(tab[i-1] + tab [i-2])
        return tab
    except:
        return None
#4
def matrix_calculations(a:float) -> tuple:
    try:
        matrix = np.array ([[a,1,-a],[0,1,1],[-a,a,1]])
        Minv = np.min(matrix)
        Mt = np.transpose(matrix)
        Mdet = np.linalg.det(matrix)
        return (Minv, Mt, Mdet)
    except:
        return None
print (matrix_calculations(3))
#5
Matrix = np.array ([[3,1,-2,4], [0,1,1,5], [-2,1,1,6], [4,3,0,1]])
print (Matrix[0,0])
print (Matrix[2,2])
print (Matrix[2,1])

w1 = Matrix [2][:]
w2 = Matrix [:][1]

#6
def custom_matrix(m:int, n:int):
    try:
        if (m < 1 or n < 1):
            return None
        else:
            tab = np.zeros ((m,n), dtype = int)
            for i in range (m):
                for j in range (n):
                    if j >= i:
                        tab[i,j] = j
                    else:
                        tab[i,j] = i     
        return tab   
    except:
        return None
    
#7
v1 = np.array ([[1],[3],[13]])
v2 = np.array ([[8],[5],[-2]])

print (np.multiply (4, v1))
print (np.multiply (v2,(-1)) + [2,2,2])
print (np.multiply (v1,v2))
# print (np.dot (v1,v2)) - nie działa, rząd macierzy nie jest odpowiedniM1 = np.array ([[1,-7,3], [-12,3,4], [5,13,-3]])

#8
v1 = np.array ([[1],[3],[13]])
v2 = np.array ([[8],[5],[-2]])
M1 = np. array ([[1,-7,3],[-12,3,4],[5,13,-3]])
print (M1 * 3)
print (M1 * 3 + np.ones(3))
print (np.transpose(M1))
print (M1 @ v1)
print (np.transpose(v2) @ M1)