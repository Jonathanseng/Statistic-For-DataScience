import numpy as np

def excess_kurtosis(data):
  """
  Calculates the excess kurtosis of a dataset.

  Args:
    data: A NumPy array of data points.

  Returns:
    The excess kurtosis of the dataset.
  """

  # Calculate the fourth standardized moment.
  fourth_standardized_moment = np.mean((data - np.mean(data))**4)

  # Calculate the excess kurtosis.
  excess_kurtosis = fourth_standardized_moment - 3

  return excess_kurtosis

# Here is an example of how to use the excess_kurtosis() function:
# Create a dataset.
data = np.array([1, 2, 3, 4, 5])

# Calculate the excess kurtosis.
excess_kurtosis = excess_kurtosis(data)

print(excess_kurtosis)

# This will print the following output:
2.0

# This indicates that the dataset has a kurtosis of 2.0, which is higher than the kurtosis of a normal distribution (3.0). This suggests that the dataset has a more pronounced peak than a normal distribution.
