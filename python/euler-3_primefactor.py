#!/usr/bin/python
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 317584931803?
#
# Can be found eg. by Trial Division: http://en.wikipedia.org/wiki/Trial_division

num = 100


# Sieve of Eratosthenes
#
def e_sieve ( max ):
	nlist = []
	for i in range( 1, num ):
		nlist.append(i)

	base = 2
	product = 2
	result = [1]
	candidates = range(2, num+1)

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

print "Prime numbers below " + str(num) + ": "
print e_sieve( num )

