# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))
f = lambda t,x: (x+t)/(x-t)
def test(t,x):
    xp1 = x[2]
    xp2 = x[3]
    xp3 = -x[0]/((x[0] ** 2 + x[1] ** 2) ** (3/2))
    xp4 = -x[1]/((x[0] ** 2 + x[1] ** 2) ** (3/2))
    return np.array([xp1,xp2,xp3,xp4])

result_euler = expected['euler']
result_euler2 = expected['euler2']
result_arenstorf = expected['arenstorf']


@pytest.mark.parametrize("t_span, y0, result", result_euler)
def test_euler(t_span, y0, result):
    if result is None:
        assert main.solve_euler(f, t_span, y0) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.solve_euler(f, t_span, y0))
    else:
        res = main.solve_euler(f, t_span, y0)
        assert res == pytest.approx(result), f'Spodziewany wynik: {result}, aktualny: {res}. Błędy implementacji.'

@pytest.mark.parametrize("t_span, y0, result", result_euler2)
def test_euler2(t_span, y0, result):
    if result is None:
        assert main.solve_euler(test, t_span, y0) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.solve_euler(test, t_span, y0))
    else:
        res = main.solve_euler(test, t_span, y0)
        assert res == pytest.approx(result), f'Spodziewany wynik: {result}, aktualny: {res}. Błędy implementacji.'

@pytest.mark.parametrize("t, x, result", result_arenstorf)
def test_arenstorf(t, x, result):
    if result is None:
        assert main.arenstorf(t, x) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.arenstorf(t, x))
    else:
        res = main.arenstorf(t, x)
        assert res == pytest.approx(result), f'Spodziewany wynik: {result}, aktualny: {res}. Błędy implementacji.'