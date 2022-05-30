import pytest
from roman_to_integer import roman_to_integer


@pytest.mark.parametrize(
    "roman_number, expected_integer_number",
    [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("IV", 4),
        ("V", 5),
        ("V", 5),
    ],
)
def test_roman_to_integer(roman_number, expected_integer_number):
    assert roman_to_integer(roman_number) == expected_integer_number
