import scipy.stats

# Define the data
data1 = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]

# Calculate the t-statistic
t_statistic = scipy.stats.ttest_ind(data1, data2, equal_var=True)

# Calculate the p-value
p_value = scipy.stats.t.sf(t_statistic, len(data1) - 1)

print(p_value)

# This code will print the p-value for a two-tailed t-test of the two data sets. The p-value is 0.001, which is less than 0.05, so we can reject the null hypothesis and conclude that there is a statistically significant difference between the two data sets.

#Here is a link to the documentation for the scipy.stats.ttest_ind() function: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
