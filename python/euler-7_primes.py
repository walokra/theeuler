#!/usr/bin/python
#
# Problem 7
# 28 December 2001
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
#
# Answer: 104743
#

from time import time

# Check if n is prime number
# 
def is_prime(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def nth_prime(n):
	max = n
	count = 0
	i = 1
	while count < max:
		i += 1
		if (is_prime(i)):
			count += 1
	return i
	
max = 10001
start = time()
print "The " + str(max) + "st prime number (is_prime):", nth_prime(max)
elapsed = (time() - start)
print "Time:", elapsed
