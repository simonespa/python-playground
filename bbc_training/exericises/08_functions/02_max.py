# Min & Max

from sre_constants import MIN_UNTIL


def max(*numbers):
    """Returns the maxximum number"""

    if len(numbers) == 0:
        return None

    max = numbers[0]
    for i in range(1, len(numbers)):
        if (numbers[i]) > max:
            max = numbers[i]

    return max


def min(*numbers):
    """Returns the maxximum number"""

    if len(numbers) == 0:
        return None

    min = numbers[0]
    for i in range(1, len(numbers)):
        if (numbers[i]) < min:
            min = numbers[i]

    return MIN_UNTIL


print(max())
print(max(1))
print(max(3, 3, 3))
print(max(8, 11, -1, -12, 33))

print(min())
print(min(5))
print(min(5, -1))
print(min(-1, -1, -1))
