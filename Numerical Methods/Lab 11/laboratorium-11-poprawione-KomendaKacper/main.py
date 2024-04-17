##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss
from scipy.special import roots_legendre
from typing import Union, List, Tuple

def rectangular_rule(func, a, b, n):
    try:
        s = 0.0
        dx = float((b-a)/n)
        while a < b:
            s += dx * func(a)
            a += dx
        return s
    except:
        return None

def trapezoidal_rule(func, a, b, n):
    try: 
        s = 0.0
        dx = float((b - a) / n)

        while a < b:
            s+= (func(a)+func(a+dx))/2*dx
            a += dx
        return s
    except:
        return None




def custom_integration(func, a, b, order):
    """
    Własna funkcja całkująca, wykorzystująca kwadraturę Gaussa-Legendre'a.

    :param func: Funkcja do zintegrowania.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param order: Rząd kwadratury.
    :return: Przybliżona wartość całki.
    """
    try:
        nodes, weights = roots_legendre(order)
        x_mapped = 0.5 * (b - a) * nodes + 0.5 * (a + b)
        function_values = func(x_mapped)
        result = np.sum(weights * function_values) * 0.5 * (b - a)
        return result
    except:
        return None


