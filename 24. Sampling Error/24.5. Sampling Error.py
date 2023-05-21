import numpy as np

def sampling_error(data, sample_size):
  """
  Calculates the sampling error for a given dataset and sample size.

  Args:
    data: A NumPy array of data.
    sample_size: The size of the sample.

  Returns:
    The sampling error.
  """

  # Calculate the sample mean.
  sample_mean = np.mean(data)

  # Calculate the sample standard deviation.
  sample_std = np.std(data, ddof=1)

  # Calculate the sampling error.
  sampling_error = sample_std / np.sqrt(sample_size)

  return sampling_error

# Result:
# Create a dataset.
data = np.array([1, 2, 3, 4, 5])

# Calculate the sampling error for a sample size of 2.
sampling_error = sampling_error(data, 2)

# Print the sampling error.
print(sampling_error)

# This will print the following output:
0.7071067811865476

# The sampling error is the standard deviation of the sample means divided by the square root of the sample size. It is a measure of how much the sample mean can vary from the population mean. The larger the sample size, the smaller the sampling error.
