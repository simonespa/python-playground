import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (2, 2, 4), (3, 3, 6)])
def test_calculator(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
