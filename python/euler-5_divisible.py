#!/usr/bin/python
#
# Problem 5
# 30 November 2001
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Answer: 232792560
#

from time import time

# Erastothene Sieve
#
def sieve(n):
	primes = range(2,n+1)

	for i in primes:
		j = 2
		# remove all multiples
		product = i * j
		while product <= primes[-1]:
			# if the multiple is in the list, take it out
			if product in primes:
				primes.remove(product)
			j += 1
			product = i * j

	return primes

# Trial Division
#
def trial_division(n):
	if n == 1: return [1]
	primes = sieve(int(n**0.5) + 1)
	prime_factors = []
 
	for p in primes:
		if p*p > n: break
		while n % p == 0:
			prime_factors.append(p)
			n //= p

	if n > 1: prime_factors.append(n)
 
	return prime_factors

# Track of the max occurrences of a key in a dict
#
def set_max_count(dict_,(key,val)):
    if dict_[key] < val :
        dict_[key] = val
    return dict_
    
# Least Common Multiple
#
def lcm(min, max):
	factors = []
	d = dict((n, 0) for n in range(min,max))
	for i in xrange(min, max):
		val = trial_division(i)
		for z in val:
			set_max_count(d, (z, val.count(z)))	
		factors.append(val)
		 
	#print "factors: ", factors
	#print "factors by max pow: ", d

	num = 1
	for key, value in d.items():
		#print "key: ", key, "value: ", value
		num = num*key**value

	return num

# Check for divisibility by brute force
#
def lcm_bf(min, max):
	result = []
	i = 2
	
	while len(result) < 1 :
		if all(i % n == 0 for n in reversed(xrange(min, max))):
			result.append(i)
		i += 1
	return result[0]

min = 2
max = 20
print "The smallest number evenly divisible by all of the numbers from ", min,  " to ", max
start = time()
#print lcm_bf(min, max)
print lcm(min, max)
elapsed = (time() - start)
print "Time:", elapsed
