# Filter even numbers with list comprehension

import numpy as np

numbers = np.arange(20)

print([number for number in numbers if number % 2 == 0])
