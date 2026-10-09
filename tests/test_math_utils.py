import pytest

from src.math_utils import add, divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0.1, 0.2, 0.3),
        (-5, -5, -10),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


def test_divide_valid_numbers():
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        divide(10, 0)
