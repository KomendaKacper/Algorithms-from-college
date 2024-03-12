import numpy as np
import scipy as sp
from scipy import linalg
from  datetime import datetime
import pickle
from scipy.sparse import diags

from typing import Union, List, Tuple

def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    try:
        residuum = linalg.norm(b - A @ x)
        return residuum
    except ValueError:
        return None
    
def is_diagonaly_dominant(A):
    try:
        A_abs = np.abs(A)
        if A_abs.ndim < 2:
            return False 
        diag = np.diag(A_abs)
        diag_sum = np.sum(diag)
        off_diag_sum = np.sum(A_abs) - diag_sum

        return diag_sum > off_diag_sum
    except:
        return None
