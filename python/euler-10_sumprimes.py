#!/usr/bin/python
#
# Problem 10
# 08 February 2002
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
#
# Answer: 
# 

from time import time

# Check if n is prime number
# 
def is_prime(n):
	i = 2
	while i*i <= n+1:
		if n % i == 0:
			return False
		i += 1
	return True
	
max = 2000000
#max = 10
print "The sum of all the primes below ", max
start = time()

n = 2
sum = 0
while n < max:
        if is_prime(n):
                sum = sum + n

        n += 1
        
print sum
elapsed = (time() - start)
print "Time:", elapsed
