import random

# Create a list of ratio data
ratio_data = []
for i in range(10):
  ratio_data.append(random.randint(1, 100))

# Calculate the mean of the ratio data
mean = sum(ratio_data) / len(ratio_data)

# Calculate the median of the ratio data
median = ratio_data[len(ratio_data) // 2]

# Calculate the mode of the ratio data
mode = max(ratio_data, key=ratio_data.count)

# Calculate the range of the ratio data
range = max(ratio_data) - min(ratio_data)

# Calculate the standard deviation of the ratio data
standard_deviation = sum((x - mean) ** 2 for x in ratio_data) / len(ratio_data) ** 0.5

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", range)
print("Standard deviation:", standard_deviation)

#This code will create a list of 10 random ratio values, calculate the mean, median, mode, range, and standard deviation of the data, and then print the results.
