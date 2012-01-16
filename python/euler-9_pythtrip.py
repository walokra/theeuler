#!/usr/bin/python
#
# Problem 9
# 25 January 2002
# 
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# 
# Find the product abc.
#

from time import time

def pyth_trip:
	sum = 0
	for i in range(min, max+1):
		sum = sum + i**2
	
	return sum

start = time()
sum_sq = sum_squares(min, max)
sq_sum = squares_sum(min, max)
print "Result: ", pyth_trip
elapsed = (time() - start)
print "Time:", elapsed
