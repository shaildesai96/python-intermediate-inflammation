"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


# TODO(lesson-robust) Implement tests for the other statistical functions
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [5, 0], [0, 1]], [5, 1]),
        ([[1, 2], [-3, 4], [5, -6]], [5, 4]),
    ]
)
def test_daily_max(test, expected):
    """Test that mean function works for an array of zeros, with one
    non-zero, and for positive and negative integers"""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))



@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [5, 0], [0, -1]], [0, -1]),
        ([[1, 2], [-3, 4], [5, -6]], [-3, -6]),
    ]
)
def test_daily_min(test, expected):
    """Test that mean function works for an array of zeros, with one
    non-zero, and for positive and negative integers"""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


