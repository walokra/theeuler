#!/usr/bin/python
#
# Problem 37
# 14 February 2003
# 
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
def next_prime(n):
	c = n
	while 1:
		if (is_prime(c)):
			return c
		c += 1

# Check if given number n if truncatable prime
#
def check_trunc(n):
	i = 1
	max = len(str(n))-1
	#print "n:", n
	while i <= max:
		#print "[i:]", str(n)[i:], "[:i]", str(n)[:i]
		left = int(str(n)[i:])
		right = int(str(n)[:i])
		if left == 1 or right == 1:
			return False
		if not is_prime(left):
			return False
		elif not is_prime(right):
			return False
		i += 1
	
	return True
	
# Main
#
start = time()

i = 11
primes = []
trunc_primes = []
while len(trunc_primes) < 11:
	primes.append(next_prime(i))
	#print "last", primes[-1]
	tp = primes[-1] 
	if check_trunc(tp):
		trunc_primes.append(tp)
	i = tp + 1

#print "primes:", primes
print "trunc:", trunc_primes

sum = 0
for x in trunc_primes:
	sum += x
	
print sum

elapsed = (time() - start)
print "Time:", elapsed
