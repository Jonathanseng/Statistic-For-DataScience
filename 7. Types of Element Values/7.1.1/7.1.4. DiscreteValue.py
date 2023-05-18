# Here's an example of Python code for working with discrete values in statistics. This code demonstrates how to calculate descriptive statistics and create a bar graph to visualize the frequencies of different discrete values:

import matplotlib.pyplot as plt

# Example dataset of discrete values
data = [1, 3, 2, 3, 4, 2, 1, 3, 1, 4, 2, 3, 2]

# Calculate the count of values
count = len(data)

# Calculate the mode (most frequently occurring value)
mode = max(set(data), key=data.count)

# Calculate the mean
mean = sum(data) / count

# Calculate the median
sorted_data = sorted(data)
middle_index = count // 2
if count % 2 == 0:
    median = (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
else:
    median = sorted_data[middle_index]

# Print the descriptive statistics
print("Count:", count)
print("Mode:", mode)
print("Mean:", mean)
print("Median:", median)

# Create a bar graph to visualize the frequencies
unique_values = sorted(set(data))
frequencies = [data.count(value) for value in unique_values]

plt.bar(unique_values, frequencies)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Frequency of Discrete Values")
plt.show()

# This code uses the matplotlib library to create a bar graph that displays the frequencies of different discrete values in the dataset. You can modify the data list to use your own set of discrete values for analysis.
