def degrees_of_freedom(data):
  """Calculates the degrees of freedom for a given dataset.

  Args:
    data: A list of numbers.

  Returns:
    The degrees of freedom.
  """

  n = len(data)
  d = n - 1

  return d

# Here is an example of how to use the degrees_of_freedom function:
data = [1, 2, 3, 4, 5]

dof = degrees_of_freedom(data)

print(dof)

# This will print the following output:
4
