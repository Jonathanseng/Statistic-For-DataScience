import numpy as np
import scipy.stats as stats

# Define the mean and standard deviation
mean = 0
std = 1

# Create a normal distribution object
norm = stats.norm(mean, std)

# Plot the distribution
x = np.linspace(-3, 3, 100)
y = norm.pdf(x)
plt.plot(x, y)
plt.show()

# This code will create a normal distribution with a mean of 0 and a standard deviation of 1. The distribution will be plotted as a bell curve, with the peak at the mean. The height of the curve at each point represents the probability of a random variable taking on that value.

#Here is an explanation of the code:

#import numpy as np imports the NumPy library, which provides functions for working with arrays and matrices.
#import scipy.stats as stats imports the SciPy stats library, which provides functions for working with probability distributions.
#mean = 0 defines the mean of the distribution.
#std = 1 defines the standard deviation of the distribution.
#norm = stats.norm(mean, std) creates a normal distribution object with the specified mean and standard deviation.
#x = np.linspace(-3, 3, 100) creates an array of 100 evenly spaced values between -3 and 3.
#y = norm.pdf(x) calculates the probability density function for the distribution at each value in the array x.
#plt.plot(x, y) plots the distribution as a line graph.
#plt.show() shows the plot.
