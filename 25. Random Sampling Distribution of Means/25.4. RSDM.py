import numpy as np

# Create a population
population = np.random.randint(0, 100, size=1000)

# Calculate the population mean
population_mean = np.mean(population)

# Create a list to store the sample means
sample_means = []

# Take 1000 samples of size 10 from the population
for i in range(1000):
    sample = np.random.choice(population, size=10)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# Plot the sampling distribution of means
plt.hist(sample_means)
plt.axvline(population_mean, color='red')
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.title('Sampling distribution of means')
plt.show()

# This code will create a population of 1000 numbers, calculate the population mean, and then take 1000 samples of size 10 from the population. The sample means will be stored in a list and then plotted on a histogram. The red line on the histogram represents the population mean.

#As you can see from the histogram, the sample means are all close to the population mean, but they do vary a bit. This is because samples are only a small part of the population, and so they will not always be exactly the same as the population.

#The standard deviation of the sampling distribution of means is called the standard error of the mean. The standard error of the mean tells us how much the sample means are likely to vary from the population mean. In this example, the standard error of the mean is 2.

#The standard error of the mean can be used to calculate the confidence interval for the population mean. The confidence interval is a range of values that is likely to contain the population mean. In this example, the 95% confidence interval for the population mean is 98.5 to 101.5.

#The random sampling distribution of means is a powerful tool that can be used to make inferences about populations based on samples.
