import pytest
from average import average


@pytest.mark.parametrize("a, b, expected", [(1, 1, 1), (2, 2, 2), (3, 3, 3)])
def test_average(a, b, expected):
    assert average(a, b) == expected


@pytest.fixture
def some():
    return 3


def test_some_test(some):
    assert some == 3
