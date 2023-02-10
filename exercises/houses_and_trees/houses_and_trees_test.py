import pytest
import numpy as np
from houses_and_trees import houses_and_trees

@pytest.mark.parametrize(
    "matrix, A, expected",
    [
        (
            np.array(
                [
                    ["1", "1", "0", "0", "0"],
                    ["*", "1", "0", "1", "1"],
                    ["1", "1", "0", "1", "*"],
                ]
            ),
            2,
            True,
        ),
        (
            np.array(
                [
                    ["1", "1", "0", "0", "0"],
                    ["*", "1", "0", "1", "1"],
                    ["1", "1", "0", "1", "*"],
                ]
            ),
            0,
            False,
        ),
        (
            np.array(
                [
                    ["0", "0", "4", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            2,
            False,
        ),
    ],
)
def test_houses_and_trees(matrix, A, expected):
    assert houses_and_trees(matrix, A) == expected
