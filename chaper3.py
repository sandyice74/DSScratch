from matplotlib import pyplot as plt
from collections import Counter

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958]

plt.plot(years, gdp, color='blue', marker='o', linestyle='solid')
plt.title("normal GDP")
plt.ylabel("Billions of $")
plt.show()

# bar chart is a good choice when you want to show how some quantity varies among some discrete set of items.
# also be a good choice for plotting histograms of bucketed numeric values, in order to visually explore how the values
# are distributed
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)

plt.ylabel("# of Oscars")
plt.xlabel("Movies")
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()

grades = [83, 95, 91, 87, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science' ")
plt.ticklabel_format(userOffset=False)
plt.axis([2012.5, 2014.5, 499, 506])
plt.title("Look at the 'Huge' Increase")
plt.show()

# Line Charts showing trends

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_error, 'b-', label='total error')

plt.legend(loc=9)
plt.xlabel("model complecity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
