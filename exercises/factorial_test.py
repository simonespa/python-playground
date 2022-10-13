import pytest
from factorial import factorial


@pytest.mark.parametrize(
    "N, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (10, 3628800),
    ],
)
def test_factorial(N, expected):
    assert factorial(N) == expected
