import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle 
from inspect import isfunction
import sympy as sp


from typing import Union, List, Tuple

def fun(x):
    return math.exp(-2*x)+x**2-1

def dfun(x):
    return -2*math.exp(-2*x)+2*x

def ddfun(x):
    return 4*math.exp(-2*x)+2

def bisection(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    step = 0.001
    i = np.arange(a,b,step)
    for e in i:
        if f(e) == False:
            raise ValueError #Sprawdzam ciągłość funkcji w danym przedziale na skończonej liczbie argumentów
        
    if (f(a)*f(b)) > 0 :
        raise ValueError(f(a),f(b)) #Wyświetlam wartości funkcji
    n = 0 
    for k in range(1, iteration):
        n += 1
        x = (a + b) / 2 
        if abs(f(x)) < epsilon:
            break
        else:
            if f(x) * f(a) < 0:
                b = x
            else:
                a = x
    return x,n  
    


def difference_quotient(f: typing.Callable[[float], float],x: Union[int,float], h: Union[int,float]):

    diff = (f(x+h)-f(x))/h
    return diff

def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[[float], float], a: Union[int,float], b: Union[int,float], epsilon: float, iteration: int) -> Tuple[float, int]:
    x = (a + b) / 2
    if f(a)*f(b) > 0 or f(a) == False or f(b) == False:
        raise ValueError('Funkcja na krańcach przedziału nie przyjmuje różnych znaków', f(a), f(b))
    
    n = 0
    while abs(f(x)) > epsilon and n < iteration:
        x = x - f(x) / df(x)  
        n += 1
    
    return x, n
    

    