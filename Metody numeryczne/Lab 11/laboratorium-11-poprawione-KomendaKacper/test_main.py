# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))
f = lambda x: x**2 + 3*x

results_custom_integration = expected['custom_integration']
results_trapezoidal_rule = expected['trapezoidal_rule']
results_rectangular_rule = expected['rectangular_rule']


@pytest.mark.parametrize("a, b, order, result", results_custom_integration)
def test_custom_integration(a, b, order, result):
    if result is None:
        assert main.custom_integration(f, a, b, order) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.custom_integration(f, a, b, order))
    else:
        res = main.custom_integration(f, a, b, order)
        assert res == pytest.approx(result), f'Spodziewany wynik: {result}, aktualny: {res}. Błędy implementacji.'


@pytest.mark.parametrize("a, b, n, result", results_trapezoidal_rule)
def test_trapezoidal_rule(a, b, n, result):
    if result is None:
        assert main.trapezoidal_rule(f, a, b, n) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.trapezoidal_rule(f, a, b, n))
    else:
        res = main.trapezoidal_rule(f, a, b, n)
        assert res == pytest.approx(result), f'Spodziewany wynik: {result}, aktualny: {res}. Błędy implementacji.'


@pytest.mark.parametrize("a, b, n, result", results_rectangular_rule)
def test_rectangular_rule(a, b, n, result):
    if result is None:
        assert main.rectangular_rule(f, a, b, n) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.rectangular_rule(f, a, b, n))
    else:
        res = main.rectangular_rule(f, a, b, n)
        assert res == pytest.approx(result), f'Spodziewany wynik: {result}, aktualny: {res}. Błędy implementacji.'
