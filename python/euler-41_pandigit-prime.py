#!/usr/bin/python
# 
# Problem 41
# 11 April 2003
# 
# We shall say that an n-digit number is pandigital 
# if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?
# 
# Answer: 
# 
# Resources:
# http://en.wikipedia.org/wiki/Pandigital_number
#

from time import time

# Check if prime
#
def is_prime(n):
   for x in xrange(2, int(n**0.5) + 1):
        if not n % x:
                return False
   return True

# Calculates primes to max and returns list of primes
#
def prev_prime(n):
	c = n
	while 1:
		if (is_prime(c)):
			return c
		c -= 1

# Check if given number is n-digit pandigital
# (has all digits from 1 to n just once)
# 
def check_pandigital(num):
	a = sorted(str(num))
	for i in range(1,len(str(num))+1):
		if a[i - 1] != str(i):
			return False
	return True

# Checks the list of primes for pandigitals of n-digit
#
def primes_pandigit(digits):
	primes_pd = []
	start = 7654321
	while 1:
		prime = prev_prime(start)
		if check_pandigital(prime):
			primes_pd.append(str(prime))
		start = prime - 1
		if start < 2:
			break

	return primes_pd

# Main
#
t_start = time()

digits = 4
pandigital_primes = primes_pandigit(digits)

pandigital_primes.sort(key=int)
#print "Prime pandigs:", pandigital_primes
print pandigital_primes[-1]

t_elapsed = (time() - t_start)
print "Time:", t_elapsed
