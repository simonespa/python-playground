from matplotlib import markers, pyplot as plt

age = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
median_salary = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_median_salary = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# plt.plot(age, median_salary, "k--", label="All devs")
# plt.plot(age, py_median_salary, "b", label="Python devs")

plt.plot(age, median_salary, color="k", linestyle="--", marker=".", label="All devs")
plt.plot(age, py_median_salary, color="b", marker="o", label="Python devs")

plt.title("Median Salary (USD) by age")
plt.xlabel("Ages")
plt.ylabel("Median salary (USD)")

# plt.legend(["All devs", "Python devs"])
plt.legend()
plt.tight_layout()

plt.show()
