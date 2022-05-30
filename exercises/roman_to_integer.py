numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(roman_number):
    """
    Transform and return the roman number passed in input to the relative integer number
    """
    integer_number = 0
    N = len(roman_number)

    for index in range(N):
        if index == N - 1:
            integer_number += numbers[roman_number[index]]
        elif numbers[roman_number[index]] < numbers[roman_number[index + 1]]:
            integer_number -= numbers[roman_number[index]]
        else:
            integer_number += numbers[roman_number[index]]

    return integer_number
