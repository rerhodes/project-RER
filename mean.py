# Print the mean of the numbers given in a file

import sys

sum = 0
x = 0

# Sum input values
for num in open('data.txt'):
	sum += float(num)
	x += 1
# output mean and x
print sum / x
print x	

