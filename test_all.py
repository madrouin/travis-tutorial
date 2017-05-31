from __future__ import division

import numpy as np

def test_addition():
    assert 1 + 1 == 2

def test_multiplication():
    assert 4*5 == 20

def test_division():
    assert 3/2 == 1.5

def test_partition():
    a = np.array([3, 4, 2, 1])
    assert (np.partition(a, 3) == np.array([2, 1, 3, 4])).all()