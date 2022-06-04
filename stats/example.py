import numpy
from scipy import stats
from matplotlib import pyplot as plt

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = stats.mode(speed)

standard_deviation = numpy.std(speed)
variance = numpy.var(speed)

print(f"Mean = {mean} +/- {standard_deviation}")
print(f"Variance = {variance}")
print(f"Median = {median}")
print(f"Mode = {mode.mode[0]}")

# Percentile

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

percentile_75 = numpy.percentile(ages, 75)
print(f"75% of the people are {percentile_75} or younger")

# Graphs

# random floating numbers between 0 and 5:
random_floats = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(random_floats, 100)
plt.show()

# normal distribution a.k.a. gaussian distribution or bell curve
# the mean value is 5.0, and the standard deviation is 1.0.
normal_distribution = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(normal_distribution, 100)
plt.show()

# Scatter plot

# car age
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# car speed
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)
plt.xlabel("Car age (in years)")
plt.ylabel("Car speed (in Km/h)")
plt.title("Correlation between age and speed")
plt.show()

random_x = numpy.random.normal(5.0, 1.0, 1000)
random_y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(random_x, random_y)
plt.show()

another_x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
another_y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(another_x, another_y)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, another_x))

plt.set
plt.scatter(another_x, another_y)
plt.plot(another_x, mymodel)
plt.show()
