import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from numpy.core._multiarray_umath import ndarray
from numpy.polynomial import polynomial as P
import pickle

# zad1
def polly_A(x: np.ndarray):
    if not isinstance(x, np.ndarray):
        return None
    w = P.polyfromroots((x))
    return w

def roots_20(a: np.ndarray):
    if not isinstance(a, np.ndarray):
        return None
    d = a + np.random.random_sample(a.shape) * 1e-10
    roots = P.polyroots(d)
    return d, roots

# zad 2

def frob_a(wsp: np.ndarray):
    if isinstance(wsp,np.ndarray) and (len(wsp) > 0):
        rozmiar = len(wsp) - 1
        A = np.zeros((rozmiar,rozmiar))
        for i in range(1,rozmiar):
            A[i-1,i] = 1
        A[-1,:] = -(wsp[0:-1])
        T,Z = scipy.linalg.schur(A,output = 'complex')
        return A,np.linalg.eigvals(A),np.diag(T),P.polyroots(wsp)
    
# zad 4
def is_nonsingular(A: np.ndarray)->bool:
    if not isinstance(A, np.ndarray):
        return None
    determinant = np.linalg.det(A)
    return determinant != 0

