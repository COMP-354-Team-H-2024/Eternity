import pytest

from power_function import power  # Import the function from power_function.py


def test_positive_exponent():
    assert power(2, 5) == 32  # Positive exponent


def test_zero_exponent():
    assert power(10, 0) == 1  # Zero exponent


def test_negative_exponent():
    assert pytest.approx(power(2, -3), 0.000001) == 0.125  # Negative exponent


def test_negative_base_even_exponent():
    assert power(-5, 2) == 25  # Negative base, positive even exponent


def test_negative_base_odd_exponent():
    assert power(-5, 3) == -125  # Negative base, positive odd exponent


def test_negative_base_negative_exponent():
    assert pytest.approx(power(-2, -3), 0.000001) == -0.125   # Negative base, negative exponent
`

def test_negative_base_positive_exponent():
    assert power(-2, 5) == -32 # Negative base, positive exponent


def test_zero_base_negative_exponent():
    with pytest.raises(ZeroDivisionError):
        power(0, -2)  # Base zero, negative exponent (should raise ZeroDivisionError)


def test_zero_base_zero_exponent():
    assert power(0,0) == 1  # Zero base, zero exponent


def test_fractional_base_positive_exponent():
    assert pytest.approx(power(0.5,2), 0.000001) == 0.25    # Fractional base, positive exponent


def test_fractional_base_negative_exponent():
    assert pytest.approx(power(0.5, -2), 0.000001) == 4.0  # Fractional base, negative exponent