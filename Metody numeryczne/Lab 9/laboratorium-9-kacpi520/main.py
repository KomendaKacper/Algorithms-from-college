import numpy as np
import matplotlib.pyplot as plt

from typing import Union, List


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


def barycentric_inte(xi: np.ndarray, yi: np.ndarray, wi: np.ndarray, x: np.ndarray) -> np.ndarray:
    try:
        if not all(isinstance(i, np.ndarray) for i in [xi, yi, wi, x]):
            raise TypeError("Inputs must be numpy arrays")
        if xi.shape != yi.shape or yi.shape != wi.shape:
            raise ValueError("Shapes of inputs xi, yi, and wi must match")
        y = []
        for val in np.nditer(x):
            le = wi / (val - xi)
            y.append(yi @ le / sum(le))

        return np.array(y)
    except (ValueError, TypeError):
        return None


def L_inf(xr: Union[int, float, List, np.ndarray], x: Union[int, float, List, np.ndarray]) -> float:
    try:
        if np.array(x).shape != np.array(xr).shape:
            raise ValueError("Shapes of inputs x and xr must match")
        elif np.size(np.array(x)) == 1:
            return abs(x - xr)
        else:
            return max(abs(np.array(xr) - np.array(x)))
    except (ValueError, TypeError):
        return np.NaN
