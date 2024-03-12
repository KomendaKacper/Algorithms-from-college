import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle

from typing import Union, List, Tuple



def square_from_rectan(A: np.ndarray, b: np.ndarray):
    try:
        if not isinstance(A, np.ndarray) or not isinstance(b, np.ndarray):
            raise ValueError
        if A.shape[0] != b.shape[0]:
            raise ValueError
        At = np.transpose(A)
        
        A_wynik = At @ A
        b_wynik = At @ b
        return A_wynik, b_wynik
    except ValueError as e:
        print(e)
        return None


def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    try:
        residuum = linalg.norm(b - A @ x)
        return residuum
    except ValueError:
        return None
