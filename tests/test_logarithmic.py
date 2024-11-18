import pytest
from logarithmic.logarithmic import Log_Base_b
from math import log

def test_valid_cases():
    assert abs(Log_Base_b(8,2) - 3) < 1e-10
    assert abs(Log_Base_b(27, 3) - 3) < 1e-10
    assert abs(Log_Base_b(100, 10) - 2) < 1e-10
    assert abs(Log_Base_b(81, 3) - 4) < 1e-10

def test_invalid_cases():
    with pytest.raises(ValueError):
        Log_Base_b(0,2)
    
    with pytest.raises(ValueError):
        Log_Base_b(-1,2)

    with pytest.raises(ValueError):
        Log_Base_b(10,1)

    with pytest.raises(ValueError):
        Log_Base_b(10,0)

'''def test_small_values():
    assert abs(Log_Base_b(0.01, 10) + 2) < 1e-5
    assert abs(Log_Base_b(0.001, 10) + 3) < 1e-5
    assert abs(Log_Base_b(0.5, 2) + 1) < 1e-5'''##still need to work on this one


def test_base2():
    assert abs(Log_Base_b(32, 2) - 5) < 1e-5
    assert abs(Log_Base_b(8, 2) - 3) < 1e-5
    assert abs(Log_Base_b(128, 2) - 7) < 1e-5

def test_comparison():
    assert abs(Log_Base_b(8, 2) - log(8, 2)) < 1e-10
    assert abs(Log_Base_b(27, 3) - log(27, 3)) < 1e-10
    assert abs(Log_Base_b(100, 10) - log(100, 10)) < 1e-10

