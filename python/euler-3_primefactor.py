#!/usr/bin/python
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
#
# Can be found eg. by Trial Division: http://en.wikipedia.org/wiki/Trial_division
#
# Answer: 6857
#

from math import sqrt
from math import floor

# Sieve of Eratosthenes
#
def e_sieve ( max ):
	base = 2
	product = 2
	result = [1]
	candidates = range(2, max)

	while candidates:
		while product <= max:
			if product in candidates:
				candidates.remove(product)
			product = product + base
		result.append(base)
		base = candidates[0]
		product = base
		del candidates[0]

	result.append(base)

	return result

# Check if prime
#
def isprime(n):
   for x in xrange(2, int(floor(n**0.5)) + 1):
        if not n % x:
                return False
   return True

# Trial Division
# - just do first the division and check for primes later
#
def trial_division( n ):
        print "n: " + str(n)
        if n == 1: return [1]
        #primes = e_sieve(int(floor(n**0.5)) + 1)
        #print "primes: " + str(primes)
        factors = []

        for s in range(2,int(floor(sqrt(n)))):
        #for s in primes:
                if n % s == 0:
                        if isprime(s):
                                factors.append(s)

        return factors

# Main
# 
# n = 13195
n = 600851475143

primes = trial_division(n)

print "Primes: " + str(primes)
print "Largest prime factor for " + str(n) + ": " +str(primes[-1])


