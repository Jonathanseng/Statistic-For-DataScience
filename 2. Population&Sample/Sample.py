# Certainly! Here's an example of Python code that demonstrates how to take a sample from a dataset using the random module:

import random

# Original dataset
dataset = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# Set the sample size
sample_size = 5

# Randomly select a sample from the dataset
sample = random.sample(dataset, sample_size)

# Print the sample
print("Sample:", sample)

# In this example, we have a dataset represented by a list [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]. We want to take a sample of size 5 from this dataset. The random.sample() function is used to randomly select a sample of the specified size.

# The output will be a randomly selected sample of 5 elements from the dataset, for example: [25, 15, 60, 30, 40].

# Remember to adjust the dataset and sample size according to your specific needs.
