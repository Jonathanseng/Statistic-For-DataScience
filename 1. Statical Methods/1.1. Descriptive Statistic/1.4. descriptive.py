# Python provides several libraries that make it convenient to perform descriptive statistics on datasets. One of the commonly used libraries is numpy. Here's an example code snippet that demonstrates how to calculate descriptive statistics using numpy:

import numpy as np

# Sample dataset
data = [12, 15, 18, 22, 10, 9, 20, 25, 13, 16]

# Calculate mean
mean = np.mean(data)
print("Mean:", mean)

# Calculate median
median = np.median(data)
print("Median:", median)

# Calculate mode
mode = np.mode(data)
print("Mode:", mode)

# Calculate range
range_val = np.ptp(data)
print("Range:", range_val)

# Calculate variance
variance = np.var(data)
print("Variance:", variance)

# Calculate standard deviation
std_deviation = np.std(data)
print("Standard Deviation:", std_deviation)

# Calculate quartiles
quartiles = np.percentile(data, [25, 50, 75])
print("Quartiles:", quartiles)

# Make sure you have the numpy library installed in your Python environment to run this code. You can install it using pip install numpy. Replace the data variable with your own dataset, and the code will compute the respective descriptive statistics for your data.
