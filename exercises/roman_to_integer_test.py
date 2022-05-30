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
        ("VI", 6),
        ("VII", 7),
        ("VIII", 8),
        ("IX", 9),
        ("X", 10),
        ("XI", 11),
        ("XII", 12),
        ("XIII", 13),
        ("XIV", 14),
        ("XV", 15),
        ("XX", 20),
        ("XXX", 30),
        ("XXX", 30),
        ("XL", 40),
        ("L", 50),
        ("LX", 60),
        ("LXX", 70),
        ("LXXX", 80),
        ("XC", 90),
        ("C", 100),
        ("CC", 200),
        ("CCC", 300),
        ("CD", 400),
        ("D", 500),
        ("DC", 600),
        ("DCC", 700),
        ("DCCC", 800),
        ("CM", 900),
        ("M", 1000),
        ("MI", 1001),
        ("MV", 1005),
        ("MX", 1010),
        ("ML", 1050),
        ("MC", 1100),
        ("MD", 1500),
        ("MM", 2000),
    ],
)
def test_roman_to_integer(roman_number, expected_integer_number):
    """Test the transformation between roman and integer numbers"""
    assert roman_to_integer(roman_number) == expected_integer_number
