from functools import reduce
import numpy as np

numbers = np.arange(20)

even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

squared_even_numbers = list(map(lambda n: n**2, even_numbers))

print(reduce(lambda x, y: x + y, squared_even_numbers))
