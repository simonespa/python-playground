import pytest
from flatten_list import flatten, flatten_comprehension

list_of_tuples = [
    ([], []),
    ([[1]], [1]),
    ([[1, 2]], [1, 2]),
    ([[1], [2]], [1, 2]),
    ([[1, 2], [3, 4]], [1, 2, 3, 4]),
]


@pytest.mark.parametrize("list, expected", list_of_tuples)
def test_flatten(list, expected):
    assert flatten(list) == expected


@pytest.mark.parametrize("list, expected", list_of_tuples)
def test_flatten_comprehension(list, expected):
    assert flatten_comprehension(list) == expected
