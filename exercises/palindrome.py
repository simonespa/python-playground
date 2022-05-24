# Determine if a given string is a palindrome


def palindrome(input):
    """
    Return True if a given string is a palindrome, False otherwise
    """

    if len(input) <= 1:
        return True

    half_length = len(input) // 2

    index = 0

    while index < half_length:
        if input[index] != input[len(input) - 1 - index]:
            return False
        index += 1

    return True
