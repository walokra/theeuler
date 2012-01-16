#!/usr/bin/python
#
# Problem 6
# 14 December 2001
# 
# The sum of the squares of the first ten natural numbers is,
# 	1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# 	(1 + 2 + ... + 10)^2 = 552 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# Answer: 25164150
#

from time import time

def sum_squares(min, max):
	sum = 0
	for i in range(min, max+1):
		sum = sum + i**2
	
	return sum

def squares_sum(min, max):
	sum = 0
	for i in range(min, max+1):
		sum = sum + i
	
	sum = sum**2
	
	return sum

min = 1
max = 100
start = time()
sum_sq = sum_squares(min, max)
sq_sum = squares_sum(min, max)
print "Sum of squares from ", min, " to ", max, ": ", sum_sq
print "Squares of the sum from ", min, " to ", max, ": ", sq_sum
print "Difference: ", abs(sum_sq - sq_sum)
elapsed = (time() - start)
print "Time:", elapsed
