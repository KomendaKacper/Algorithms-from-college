import numpy as np
from typing import Union, Callable


def solve_euler(fun: Callable, t_span: np.array, y0: np.array):
    ''' 
    Funkcja umożliwiająca rozwiązanie układu równań różniczkowych z wykorzystaniem metody Eulera w przód.
    
    Parameters:
    fun: Prawa strona równania. Podana funkcja musi mieć postać fun(t, y). 
    Tutaj t jest skalarem i istnieją dwie opcje dla ndarray y: Może mieć kształt (n,); wtedy fun musi zwrócić array_like z kształtem (n,). 
    Alternatywnie może mieć kształt (n, k); wtedy fun musi zwrócić tablicę typu array_like z kształtem (n, k), tj. każda kolumna odpowiada jednej kolumnie w y. 
    t_span: wektor czasu dla którego ma zostać rozwiązane równanie
    y0: warunek początkowy równania o wymiarze (n,)
    Results:
    (np.array): macierz o wymiarze (n,m) zawierająca w wkolumnach kolejne rozwiązania fun w czasie t_span. W przypadku błędnych danych wejściowych powinna zwracać None

    '''
    try:
        if not isinstance(y0, np.ndarray) or not isinstance(t_span, np.ndarray):
            return None
            
        y = y0
        for i in range(0, y.shape[0] - 1):
            y[i + 1, :] = y[i, :] + fun(y[i, :], t_span[i]) * (t_span[i + 1] - t_span[i])
        return y
    except:
        return None

def arenstorf(x: np.array, t):
    '''     
    Parameters:
    t: czas
    x: wektor stanu 
    Results:
    (np.array): wektor pochodnych stanu
    '''
    try:
        mi = 0.012277471
        mip = 1 - mi
        D1 = np.power(np.power(x[0] + mi ,2) + np.power(x[2],2),3/2)
        D2 = np.power(np.power(x[0] - mip,2) + np.power(x[2],2),3/2)
        x1 = x[1]
        x2 = x[0] + 2 * x[3] - mip * (x[0] + mi) / D1 - mi * (x[0] - mip) / D2
        x3 = x[3]
        x4 = x[2] - 2 * x[1] - mip * x[2] / D1 -  mi * x[2] / D2
        return np.array([x1, x2, x3, x4])
    except:
        return None
  
