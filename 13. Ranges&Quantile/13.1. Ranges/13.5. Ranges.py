def range(data):
  """
  Calculates the range of a data set.

  Args:
    data: A list of numbers.

  Returns:
    The range of the data set.
  """

  max_value = max(data)
  min_value = min(data)

  return max_value - min_value

# Here is an example of how to use the range() function:
data = [1, 2, 3, 4, 5]

range(data)

# Output: 4

# The range() function can be used to calculate the range of any data set. It is a simple and efficient way to measure the variability of a data set.
