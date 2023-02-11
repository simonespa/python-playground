import pytest
from fibonacci import fibonacci


@pytest.mark.parametrize(
    "N, expected",
    [
        (-1, 0),
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ],
)
def test_fibonacci(N, expected):
    assert fibonacci(N) == expected
