import numpy as np

def skewness(data):
  """
  Calculates the skewness of a data set.

  Args:
    data: A NumPy array of data.

  Returns:
    The skewness of the data.
  """

  mean = np.mean(data)
  stddev = np.std(data)

  # Calculate the third moment of the distribution.
  third_moment = np.mean((data - mean)**3)

  # Calculate the skewness.
  skewness = third_moment / stddev**3

  return skewness

# This code can be used to calculate the skewness of any data set. The skewness can be used to describe the shape of the distribution and to compare different distributions.
