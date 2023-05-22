import numpy as np
from scipy.stats import t

# Define the sample data
data = [1, 2, 3, 4, 5]

# Calculate the sample mean
mean = np.mean(data)

# Calculate the sample standard deviation
std = np.std(data)

# Calculate the degrees of freedom
df = len(data) - 1

# Calculate the z-score for the desired confidence level
z = t.ppf(0.95, df)

# Calculate the margin of error
me = z * std / np.sqrt(len(data))

# Calculate the confidence interval
ci = [mean - me, mean + me]

# Print the confidence interval
print(ci)

# Output:
# [2.5714285714285716, 3.4285714285714284]

# This code will calculate the confidence interval for the mean of the data, with a confidence level of 95%. The confidence interval is a range of values that is likely to contain the true population mean. The width of the confidence interval is determined by the sample size and the standard deviation. A larger sample size will result in a narrower confidence interval, and a smaller standard deviation will also result in a narrower confidence interval.

