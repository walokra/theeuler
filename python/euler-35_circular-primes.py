#!/usr/bin/python
#
# Problem 35
# 17 January 2003
# 
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?
# 
# Answer: 
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
def list_primes(max):
	i = 1
	primes = []
	while i <= max:
		i += 1
		if (is_prime(i)):
			primes.append(i)
	return primes

# Circulate the given int and return a list
# 
# The first digit is removed 
# and readded at the right side of the remaining string of digits. 
# This process is repeated until the starting number is reached again
#
def circulate(x):
	l = []
	s = str(x)
	l.append(s)
	c = 0
	max = len(s)-1
	for i in s:
		circ = s[1:] + i
		s = circ
		l.append(circ)
		c += 1
		if c >= max:
			break

	return l
	
# Main
#
start = time()

max = 1000000
count = 0
circ_primes = set([])

for x in list_primes(max):
	if len(str(x)) > 1:
		both_primes = False
		for y in circulate(x):
			z = int(''.join(map(str,y)))
			if is_prime(z):
				both_primes = True
			else:
				both_primes = False
				break
				
		if both_primes:
			circ_primes.add(x)
	else:
		circ_primes.add(x)

print circ_primes
print len(circ_primes)

elapsed = (time() - start)
print "Time:", elapsed
