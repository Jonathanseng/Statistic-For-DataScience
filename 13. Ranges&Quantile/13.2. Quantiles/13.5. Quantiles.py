import statistics

# Create a list of data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate the quantiles
quantiles = statistics.quantiles(data, q=[0.25, 0.5, 0.75])

# Print the quantiles
print(quantiles)

# This code will print the following output:
[2.5, 5.0, 7.5]

# This means that the first quartile (25%) of the data is 2.5, the median (50%) of the data is 5.0, and the third quartile (75%) of the data is 7.5.

#Here is a breakdown of what each line of code does:

#The first line imports the statistics module. This module provides a number of functions for working with statistics, including the quantiles() function.
#The second line creates a list of data.
#The third line calculates the quantiles of the data using the quantiles() function. The quantiles() function takes two arguments: the data and a list of quantiles. The quantiles are specified as a list of floats between 0 and 1. The quantiles() function returns a list of values, one for each quantile.
#The fourth line prints the quantiles.
