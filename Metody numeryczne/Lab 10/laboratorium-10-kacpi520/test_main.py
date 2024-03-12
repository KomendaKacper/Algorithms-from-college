# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))
results_linear_least_squares = expected['linear_least_squares']
results_chebyshev_nodes = expected['chebyshev_nodes']





@pytest.mark.parametrize("x, y, result", results_linear_least_squares)
def test_linear_least_squares(x, y, result):
    if result is None:
        assert main.linear_least_squares(x, y) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.linear_least_squares(x, y))
    else:
        m, c = main.linear_least_squares(x, y)
        assert (m, c) == pytest.approx(result), f'Spodziewany wynik: {result}, aktualny: {(m, c)}. Błędy implementacji.'



@pytest.mark.parametrize("n, interval, result", results_chebyshev_nodes)
def test_chebyshev_nodes(n:int, interval:tuple, result):
    if result is None:
        assert main.chebyshev_nodes(n,interval) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.chebyshev_nodes(n))
    else:
        assert main.chebyshev_nodes(n,interval) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.chebyshev_nodes(n, interval))
