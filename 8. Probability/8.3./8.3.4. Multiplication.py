# Here's an example of Python code that demonstrates the application of the multiplication rule of probability in statistics:

# Multiplication rule for independent events
def multiplication_rule_independent(prob_a, prob_b):
    # Calculate the probability of both events A and B occurring (independent)
    prob_a_and_b = prob_a * prob_b
    return prob_a_and_b

# Multiplication rule for dependent events
def multiplication_rule_dependent(prob_a, prob_b_given_a):
    # Calculate the probability of both events A and B occurring (dependent)
    prob_a_and_b = prob_a * prob_b_given_a
    return prob_a_and_b

# Example usage
prob_a = 0.4  # Probability of event A
prob_b = 0.3  # Probability of event B
prob_b_given_a = 0.2  # Probability of event B given event A

# Calculate the probability of both events A and B occurring (independent)
result_independent = multiplication_rule_independent(prob_a, prob_b)
print("Probability of both events A and B occurring (independent):", result_independent)

# Calculate the probability of both events A and B occurring (dependent)
result_dependent = multiplication_rule_dependent(prob_a, prob_b_given_a)
print("Probability of both events A and B occurring (dependent):", result_dependent)

# In this code, the multiplication_rule_independent function calculates the probability of both events A and B occurring when the events are independent. The multiplication_rule_dependent function calculates the probability of both events A and B occurring when the events are dependent. The probabilities of events A and B, along with the conditional probability of B given A, are provided as input to the functions. The calculated probabilities are then printed as output.

# You can modify the probabilities (prob_a, prob_b, prob_b_given_a) to match your specific scenario and observe the results.
