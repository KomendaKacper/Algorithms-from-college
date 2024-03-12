from typing import Union, List, Tuple
import pickle
import numpy as np
import numpy.linalg as linalg
import numpy.random as random
from numpy.linalg import LinAlgError
class ParameterError(Exception):
    pass


def random_matrix_Ab(m: int):
    try:
        a1 = np.random.rand(m, m)
        a2 = np.random.rand(m)
    except(ValueError, TypeError):
        return None
    return a1, a2


def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    try:
        rn = linalg.norm(b - A @ x)
        return rn
    except ValueError:
        return None

def log_sing_value(n: int, min_order: Union[int, float], max_order: Union[int, float]):
    try:
        if min_order >= max_order or n <= 0 or not isinstance(n, int):
            raise ValueError
        ls = np.logspace(min_order, max_order, num=n)
        return ls[::-1]
    except(ValueError, TypeError):
        return None


def order_sing_value(n: int, order: Union[int, float] = 2, site: str = 'gre'):
    try:
        if n <= 0 or not isinstance(n, int) or not isinstance(order, (int, float)):
            raise ValueError
        if site not in ['low', 'gre']:
            raise ParameterError
        sing_value = np.random.rand(n) * 10
        sing_value = np.sort(sing_value)
        if site == 'low':
            sing_value[-1] = sing_value[-1] * 10 ** order
        elif site == 'gre':
            sing_value[0] = sing_value[0] * 10 ** order
        sing_value = np.sort(sing_value)[::-1]
        return sing_value
    except(ValueError, ParameterError):
        return None


def create_matrix_from_A(A: np.ndarray, sing_value: np.ndarray):
    try:
        u, s, v = linalg.svd(A)
        result = np.dot(u * sing_value, v)
        return result
    except(ValueError, LinAlgError):
        return None
