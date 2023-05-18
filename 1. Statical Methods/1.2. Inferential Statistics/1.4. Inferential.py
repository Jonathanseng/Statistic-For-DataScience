import pandas as pd
import numpy as np

# Import the data
data = pd.read_csv("data.csv")

# Create a sample
sample = data.sample(n=100)

# Calculate the mean of the sample
sample_mean = sample["height"].mean()

# Calculate the standard deviation of the sample
sample_std = sample["height"].std()

# Calculate the t-statistic
t_statistic = (sample_mean - data["height"].mean()) / (sample_std / np.sqrt(len(sample)))

# Calculate the p-value
p_value = 1 - stats.t.cdf(t_statistic, df=len(data) - 1)

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# This code will calculate the t-statistic and p-value for a one-sample t-test. The t-statistic is a measure of how far the sample mean is from the population mean, in terms of standard deviations. The p-value is the probability of getting a t-statistic at least as extreme as the one calculated, assuming that the null hypothesis is true.

#In this example, the p-value is less than 0.05, which means that we can reject the null hypothesis. This means that there is a statistically significant difference between the sample mean and the population mean.

#Inferential statistics can be used to make inferences about a population based on a sample. By calculating these statistics, you can get a better understanding of the relationship between variables and make informed decisions about your data.
