import sys
import pytest
import numpy as np
from stats.mad import mad

# Test for a simple case where the values symetrical around the mean
def test_mad_simple_case():
    data = [1, 2, 3, 4, 5]
    expected_mad = 1.2
    assert np.isclose(mad(data), expected_mad), f"Expected {expected_mad}, but got {mad(data)}"

# Test for a case where the sample is all the same value
def test_mad_same_values():
    data = [5, 5, 5, 5, 5]
    expected_mad = 0.0
    assert mad(data) == expected_mad, f"Expected {expected_mad}, but got {mad(data)}"

# Test for an empty list (should raise a ValueError)
def test_mad_empty():
    with pytest.raises(ValueError, match="Data cannot be empty."):
        mad([])

# Test for a list with a single element (MAD should also be 0)
def test_mad_single_value():
    data = [10]
    expected_mad = 0.0
    assert mad(data) == expected_mad, f"Expected {expected_mad}, but got {mad(data)}"

# Test for a case with negative values (to verify the function handles negatives correctly)
def test_mad_negative_values():
    data = [-1, -2, -3, -4, -5]
    expected_mad = 1.2  # Same as the symmetric case
    assert np.isclose(mad(data), expected_mad), f"Expected {expected_mad}, but got {mad(data)}"

# Test for an unsorted list (MAD should not depend on order)
def test_mad_unsorted():
    data = [5, 1, 4, 2, 3]
    expected_mad = 1.2  # Same as the simple case
    assert np.isclose(mad(data), expected_mad), f"Expected {expected_mad}, but got {mad(data)}"

# Test for a large dataset
def test_mad_large_dataset():
    data = np.random.rand(1000000) * 1000  # Large dataset of random values
    result = mad(data)
    assert isinstance(result, float), f"Expected float, but got {type(result)}"

# Test for a case where the deviation from the mean is large
def test_mad_large_deviation():
    data = [5000, 2000, 1000, 3000, 4000]
    expected_mad = 1200.0  
    assert np.isclose(mad(data), expected_mad), f"Expected {expected_mad}, but got {mad(data)}"

# Test for a list with floating point numbers
def test_mad_floating_point():
    data = [6.6, 1.1, 2.2, 3.3, 4.4, 5.5]
    expected_mad = 1.65  # The MAD will be the same as the simple case
    assert np.isclose(mad(data), expected_mad), f"Expected {expected_mad}, but got {mad(data)}"