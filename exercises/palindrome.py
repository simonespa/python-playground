def palindrome(input_string):
    """Return True if a given string is a palindrome, False otherwise"""
    if len(input_string) < 1:
        return False

    if len(input_string) == 1:
        return True

    if len(input_string) == 2:
        if input_string[0] == input_string[1]:
            return True
        else:
            return False

    half_length = len(input_string) // 2

    index = 0

    while index < half_length:
        if input_string[index] != input_string[len(input_string) - 1 - index]:
            return False
        index += 1

    return True
