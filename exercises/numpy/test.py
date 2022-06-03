import numpy
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = stats.mode(speed)

standard_deviation = numpy.std(speed)
variance = numpy.var(speed)

print(f'Mean = {mean} +/- {standard_deviation}')
print(f'Variance = {variance}')
print(f'Median = {median}')
print(f'Mode = {mode.mode[0]}')

# Percentile

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentile_75 = numpy.percentile(ages, 75)
print(f'75% of the people are {percentile_75} or younger')

# Create an array containing 250 random floats between 0 and 5:
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)
