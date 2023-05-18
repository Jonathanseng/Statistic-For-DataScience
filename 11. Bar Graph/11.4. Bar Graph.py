# To create a bar graph in Python for statistical data visualization, you can use libraries such as Matplotlib or Seaborn. Here's an example of how to create a bar graph using Matplotlib:
import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [15, 30, 10, 25]

# Create the bar graph
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph')

# Display the graph
plt.show()


# In this example, we have a list of categories and their corresponding values. We use the plt.bar() function to create the bar graph, passing the categories as the x-axis values and the values as the y-axis values. Then, we add labels to the x-axis and y-axis using plt.xlabel() and plt.ylabel(), respectively. Finally, we set a title for the graph using plt.title().

# You may need to install the Matplotlib library if you don't already have it installed. You can do this by running pip install matplotlib in your Python environment.
