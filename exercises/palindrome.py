def palindrome(input_string):
    """Return True if a given string is a palindrome, False otherwise"""
    if len(input_string) <= 1:
        return True

    half_length = len(input_string) // 2

    index = 0

    while index < half_length:
        if input_string[index] != input_string[len(input_string) - 1 - index]:
            return False
        index += 1

    return True
