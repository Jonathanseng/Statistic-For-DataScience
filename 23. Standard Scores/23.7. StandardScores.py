import numpy as np

def z_score(data):
  """Calculates z-scores for a given dataset.

  Args:
    data: A NumPy array of data.

  Returns:
    A NumPy array of z-scores.
  """
  mean = np.mean(data)
  std = np.std(data)
  z_scores = (data - mean) / std
  return z_scores


if __name__ == "__main__":
  # Create a sample dataset.
  data = np.array([6, 7, 7, 12, 13, 13, 15, 16, 19, 22])

  # Calculate the z-scores.
  z_scores = z_score(data)

  # Print the z-scores.
  print(z_scores)

# This code will print the following output:
[-1.394  -1.195  -1.195  -0.199   0.000   0.000   0.398   0.598   1.195   1.793]

# Z-scores are a way of standardizing data so that it can be compared across different datasets. They are calculated by subtracting the mean from each data point and then dividing by the standard deviation. This results in a set of values that have a mean of 0 and a standard deviation of 1.
  
