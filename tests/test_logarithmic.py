import pytest
from logarithmic.logarithmic import calculate_logbx
from math import log

def test_valid_cases():
    assert abs(calculate_logbx(8,2) - 3) < 1e-10
    assert abs(calculate_logbx(27, 3) - 3) < 1e-10
    assert abs(calculate_logbx(100, 10) - 2) < 1e-10
    assert abs(calculate_logbx(81, 3) - 4) < 1e-10

def test_invalid_cases():
    with pytest.raises(ValueError):
        calculate_logbx(0,2)
    
    with pytest.raises(ValueError):
        calculate_logbx(-1,2)

    with pytest.raises(ValueError):
        calculate_logbx(10,1)

    with pytest.raises(ValueError):
        calculate_logbx(10,0)

def test_base2():
    assert abs(calculate_logbx(32, 2) - 5) < 1e-5
    assert abs(calculate_logbx(8, 2) - 3) < 1e-5
    assert abs(calculate_logbx(128, 2) - 7) < 1e-5

def test_comparison():
    assert abs(calculate_logbx(8, 2) - log(8, 2)) < 1e-10
    assert abs(calculate_logbx(27, 3) - log(27, 3)) < 1e-10
    assert abs(calculate_logbx(100, 10) - log(100, 10)) < 1e-10

