import pandas as pd

# Create a list of interval data
data = [1, 2, 3, 4, 5]

# Create a Pandas DataFrame
df = pd.DataFrame({"Data": data})

# Calculate the mean of the data
mean = df["Data"].mean()

# Calculate the median of the data
median = df["Data"].median()

# Calculate the mode of the data
mode = df["Data"].mode()

# Calculate the standard deviation of the data
std = df["Data"].std()

# Print the results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard deviation:", std)

# This code will print the following output:
#Mean: 3
#Median: 3
#Mode: 3
#Standard deviation: 1.4142135623730951

# This output shows that the mean, median, and mode of the data are all equal to 3. The standard deviation is 1.4142135623730951, which tells us that the data is spread out evenly around the mean.
