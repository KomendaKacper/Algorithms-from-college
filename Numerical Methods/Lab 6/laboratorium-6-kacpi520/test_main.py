# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

result_residual_norm = expected['residual_norm'] 
result_is_diagonaly_dominant = expected['is_diagonaly_dominant']

@pytest.mark.parametrize("A,x,b,result", result_residual_norm)
def test_residual_norm(A: np.ndarray, x: np.ndarray,b: np.ndarray, result):
    if result is None:
        assert main.residual_norm(A,x,b) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.residual_norm(A,x,b))
    else:    
        assert main.residual_norm(A,x,b) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.residual_norm(A,x,b))

@pytest.mark.parametrize("A,result", result_is_diagonaly_dominant)
def test_is_diagonaly_dominant(A, result):
    if result is None:
        assert main.is_diagonaly_dominant(A) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.is_diagonaly_dominant(A))
    else:    
        assert main.is_diagonaly_dominant(A) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.is_diagonaly_dominant(A))

