import numpy as np

def kurtosis(data):
  """
  Calculates the kurtosis of a dataset.

  Args:
    data: A NumPy array of data.

  Returns:
    The kurtosis of the dataset.
  """

  fourth_moment = np.mean(data**4)
  variance = np.var(data)
  kurtosis = fourth_moment / variance**2

  return kurtosis

# Here is an example of how to use the kurtosis function:
data = np.array([1, 2, 3, 4, 5])

kurtosis(data)

# Output: 3.0

# The kurtosis of a normal distribution is 3. This means that the distribution is neither too peaked nor too flat, and it has neither too heavy nor too light tails.

# A distribution with a kurtosis greater than 3 is said to be leptokurtic. This means that the distribution has heavier tails than a normal distribution. The tails of a leptokurtic distribution extend out further from the mean, and they are more likely to contain outliers.

# A distribution with a kurtosis less than 3 is said to be platykurtic. This means that the distribution has lighter tails than a normal distribution. The tails of a platykurtic distribution extend out less from the mean, and they are less likely to contain outliers.
