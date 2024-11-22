import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from abx.abx import calculate_abx

def test_calculate_abx_valid():
    assert calculate_abx(2, 3, 4) == pytest.approx(162)
    assert calculate_abx(1, 2, 3) == pytest.approx(8)
    assert calculate_abx(5, 5, 2) == pytest.approx(125)

def test_calculate_abx_b_equals_1():
    assert calculate_abx(2, 1, 3) == "The growth/decay factor (b) must not equal 1"

def test_calculate_abx_edge_cases():
    assert calculate_abx(0, 2, 3) == pytest.approx(0)
    assert calculate_abx(2, 2, 0) == pytest.approx(2)
    assert calculate_abx(2, 2, -1) == pytest.approx(1)

def test_calculate_abx_negative_values():
    assert calculate_abx(-2, 3, 4) == pytest.approx(-162)
    assert calculate_abx(2, -3, 4) == pytest.approx(162)
    assert calculate_abx(2, 3, -4) == pytest.approx(0.012345679)

if __name__ == "__main__":
    pytest.main()