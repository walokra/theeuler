#!/usr/bin/python
#
# Problem 20
# 21 June 2002
# 
# n! means n * (n - 1) * ... * 3 * 2 * 1
# 
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!
# 
# Answer: 
# 

from time import time

# Calculates factoria (!) for given n
# 5! = 120
#
def factorial(n):
	if n == 0: return 1
	
	return factorial(n-1)*n

# Main
#
start = time()

n = 100
fac = factorial(n)
sum = 0

for i in range(0, len(str(fac))):
	sum = sum + int(str(fac)[i])
	
print sum

elapsed = (time() - start)
print "Time:", elapsed
