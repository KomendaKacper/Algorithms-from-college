##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt

from typing import Union, List, Tuple

def chebyshev_nodes(n: int = 10) -> np.ndarray:
    try:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        k = np.arange(0, n + 1, 1)
        cos = np.cos((k * np.pi) / n)
        return cos
    except (ValueError, TypeError):
        return None

def bar_czeb_weights(n: int = 10) -> np.ndarray:
    try:
        wj = np.ndarray((n + 1,))
        for j in range(n + 1):
            if j == 0 or j == n:
                dj = 0.5
                wj[j] = (-1) ** j * dj
            elif 0 < j < n:
                dj = 1
                wj[j] = (-1) ** j * dj
        return wj
    except TypeError:
        return None

    
def L_inf(xr:Union[int, float, List, np.ndarray],x:Union[int, float, List, np.ndarray]):
    
    if isinstance(xr, List):
        xr = np.array(xr)
    if isinstance(x, List):
        x = np.array(x)

    if not (isinstance(x, int) or isinstance(x, float) or isinstance(x, np.ndarray)):
        return np.nan
    if not (isinstance(xr, int) or isinstance(xr, float) or isinstance(xr, np.ndarray)):
        return np.nan

    # poprawne rozmiary w przypadku wektorów/macierzy
    if isinstance(xr, np.ndarray) and isinstance(x, np.ndarray):
        if (len(xr.shape)!=1 or len(x.shape)!=1) or xr.shape != x.shape:
            return np.nan
        
    # liczba i wkektor jedno elementowy
    if isinstance(x, (int,float)) and isinstance(xr, np.ndarray):
        if xr.shape[0] > 1 or len(xr.shape) > 1:
            return np.nan
        
    if isinstance(xr, (int,float)) and isinstance(x, np.ndarray):
        if x.shape[0] > 1 or len(x.shape) > 1:
            return np.nan

    return np.max(np.abs(xr-x))

 