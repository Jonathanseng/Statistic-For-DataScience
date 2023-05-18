import statistics

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the mean
mean = statistics.mean(numbers)

# Print the mean
print(mean)

# The mean of a list of numbers can also be calculated using the built-in sum() and len() functions:
# Calculate the mean using sum() and len()
mean = sum(numbers) / len(numbers)

# Print the mean
print(mean)
