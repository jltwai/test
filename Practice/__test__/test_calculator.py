import pytest
from calculator import plus, minus, multiply, divide, divide_plus, minus_multiply, multiply_divide, plus_minus


@pytest.mark.parametrize("x, y, expected_result", [
    (12, 25, 37),
    (5, 5, 10),
    (44, 24, 68)
])
def test_plus(x, y, expected_result):
    assert plus(x, y) == expected_result, "WRONG!"


@pytest.mark.parametrize("x, y, expected_result", [
    (55, 22, 33),
    (17, 25, -8),
    (10, 8, 2)
])
def test_minus(x, y, expected_result):
    assert minus(x, y) == expected_result, "WRONG!"


@pytest.mark.parametrize("x, y, expected_result", [
    (6, 5, 30),
    (17, 1, 17),
    (20, 50, 1000)
])
def test_multiply(x, y, expected_result):
    assert multiply(x, y) == expected_result, "WRONG!"


@pytest.mark.parametrize("x, y, expected_result", [
    (3, 5, 0.6),
    (2, 5, 0.4),
    (25, 5, 5)
])
def test_divide(x, y, expected_result):
    assert divide(x, y) == expected_result, "WRONG!"


@pytest.mark.parametrize("x, y, z, expected_result", [
    (9, 4, 5, 25),
    (10, 7, 9, 27),
    (99, 77, 3, 66)
])
def test_minus_multiply(x, y, z, expected_result):
    assert minus_multiply(x, y, z) == expected_result, "WRONG!"


@pytest.mark.parametrize("x, y, z, expected_result", [
    (9, 3, 13, 16),
    (8, 2, 20, 24),
    (18, 3, 50, 56),
])
def test_divide_plus(x, y, z, expected_result):
    assert divide_plus(x, y, z) == expected_result, "WRONG!"


@pytest.mark.parametrize("x, y, z, expected_result", [
    (5, 5, 4, 6),
    (20, 10, 50, -20),
    (-100, 211, 11, 100),
])
def test_plus_minus(x, y, z, expected_result):
    assert plus_minus(x, y, z) == expected_result, "WRONG!"


@pytest.mark.parametrize("x, y, z, expected_result", [
    (25, 5, 20, 6.25),
    (36, 9, 50, 6.48),
    (64, 8, 50, 10.24),
])
def test_multiply_divide(x, y, z, expected_result):
    assert multiply_divide(x, y, z) == expected_result, "WRONG!"


