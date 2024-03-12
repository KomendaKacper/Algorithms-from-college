##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt
from typing import Union, List, Tuple


def linear_least_squares(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    try:
        if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or len(x) != len(y):
            raise ValueError("Niepoprawne dane wejściowe")

        x_mean = np.mean(x)
        y_mean = np.mean(y)

        slope = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
        intercept = y_mean - slope * x_mean

        return np.array([intercept, slope])
    except ValueError as e:
        print(e)
        return None




import numpy as np

def chebyshev_nodes(n: int, interval: tuple) -> np.ndarray:
    """Funkcja tworząca wektor zawierający węzły Czebyszewa dla zadanego przedziału, posortowany od najmniejszego do największego węzła.
    
    Parameters:
    n (int): Ilość węzłów Czebyszewa. Wartość musi być większa od 0.
    interval (tuple): Przedział, na którym mają być wygenerowane węzły (początek, koniec).
     
    Results:
    np.ndarray: Posortowany wektor węzłów Czybyszewa o rozmiarze (n). 
                Jeżeli dane wejściowe niepoprawne, funkcja zwraca None.
    """
    try:
        if not isinstance(n, int) or not isinstance(interval, tuple) or len(interval) != 2 or n <= 0:
            raise ValueError("Niepoprawne dane wejściowe")

        a, b = interval
        chebyshev_nodes = 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))
        sorted_nodes = np.sort(chebyshev_nodes)

        return sorted_nodes
    except ValueError as e:
        print(e)
        return None
