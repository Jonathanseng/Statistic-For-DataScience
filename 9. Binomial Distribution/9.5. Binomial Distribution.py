import numpy as np

def binomial_distribution(n, p):
  """
  Calculates the probability of getting k successes in n trials,
  where each trial has a probability of success of p.

  Args:
    n: The number of trials.
    p: The probability of success in each trial.

  Returns:
    A list of probabilities, one for each possible number of successes.
  """

  probabilities = []
  for k in range(n + 1):
    probabilities.append(np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k)) * p ** k * (1 - p) ** (n - k))

  return probabilities

#This code can be used to calculate the probability of getting any number of successes in a binomial distribution. For example, to calculate the probability of getting exactly 5 successes in 10 trials, where the probability of success in each trial is 0.5, you would use the following code:

probabilities = binomial_distribution(10, 0.5)

print(probabilities[5])

# This code would print the following output:
0.24609375

# This means that the probability of getting exactly 5 successes in 10 trials, where the probability of success in each trial is 0.5, is 0.24609375.
