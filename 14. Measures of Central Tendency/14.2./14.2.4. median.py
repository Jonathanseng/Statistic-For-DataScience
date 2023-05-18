def median(data):
  data.sort()
  n = len(data)
  if n % 2 == 1:
    return data[n // 2]
  else:
    return (data[n // 2 - 1] + data[n // 2]) / 2

#This code works by first sorting the data set in ascending order. Then, the median is found by either taking the middle value if the data set has an odd number of elements, or by taking the average of the two middle values if the data set has an even number of elements.

#Here is an example of how to use the median function:  

data = [1, 2, 3, 4, 5]
median(data)

# This is because the middle value of the data set is 3.

#The median function can be used to find the median of any data set, regardless of the size or type of data. It is a versatile and robust function that can be used in a variety of statistical applications.
