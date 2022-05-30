numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_integer(roman_number):
    sum = 0
    N = len(roman_number)

    for index in range(N):
        if index == N - 1:
            sum += numbers[roman_number[index]]
        elif numbers[roman_number[index]] < numbers[roman_number[index + 1]]:
            sum -= numbers[roman_number[index]]
        else:
            sum += numbers[roman_number[index]]

    return sum
