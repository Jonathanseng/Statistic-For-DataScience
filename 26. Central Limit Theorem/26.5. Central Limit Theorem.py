import numpy as np
import matplotlib.pyplot as plt

# Generate a population of data
population = np.random.randint(0, 100, 10000)

# Calculate the mean and standard deviation of the population
population_mean = np.mean(population)
population_std = np.std(population)

# Draw 1000 samples of size 100 from the population
samples = []
for i in range(1000):
    samples.append(np.mean(np.random.choice(population, 100)))

# Calculate the mean and standard deviation of the sample means
sample_mean = np.mean(samples)
sample_std = np.std(samples)

# Plot the distribution of the sample means
plt.hist(samples, bins=100)
plt.axvline(sample_mean, color='red', linestyle='dashed')
plt.axvline(population_mean, color='blue', linestyle='dashed')
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.title('Distribution of sample means')
plt.show()

#This code will generate a population of 10,000 random integers between 0 and 100. It will then draw 1000 samples of size 100 from the population and calculate the mean and standard deviation of each sample. Finally, it will plot the distribution of the sample means.

#The plot will show that the distribution of the sample means is approximately normal, even though the distribution of the population is not normal. The mean of the distribution of sample means will be equal to the mean of the population, and the standard deviation of the distribution of sample means will be equal to the standard deviation of the population divided by the square root of the sample size.

#This is an example of how the central limit theorem can be used to make inferences about populations based on samples. By understanding the CLT, you can better understand the limitations of your data and make more informed decisions.
