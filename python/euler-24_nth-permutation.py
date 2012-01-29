#!/usr/bin/python
#
# Problem 24
# 16 August 2002
# 
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# 
# Answer: 
# 
# TODO: Calculate the nth permutation by using factoriad

from time import time

# Generate the next permutation lexicographically after a given permutation
#
def next_perm(arr, n):
	# Find the largest index k such that a[k] < a[k + 1]
	i = n - 1
	while arr[i-1] > arr[i]:
		i -= 1
	
	# If no such index exists, the permutation is the last permutation.
	if i <= 0:
		return 1
	
	# Find the largest index l such that a[k] < a[l]. 
	j = n
	while arr[j-1] < arr[i-1]:
		j -= 1

	# Swap a[k] with a[l]
	swap(i-1, j-1)

	# Reverse rest of the sequence
	i += 1
	j = n
	while i < j:
		swap(i-1, j-1)
		i += 1
		j -= 1
		
	return 0

# Swap elements
# 
def swap(a, b):
	arr[b], arr[a] = arr[a], arr[b]

# Calculates factoria (!) for given n
# 5! = 120
#
def factorial(n):
	if n == 0 or n == 1: return 1
	
	return n * factorial(n - 1)
    
# Main
#

# from 0 to 10
# the millionth permutation
n = 10
nth = 999999

# Create our 1st permutation
arr = []
for i in range(0, n):
	arr.append(i)

start = time()
# Using itertools
import itertools
print list(itertools.permutations(arr))[nth]
elapsed = (time() - start)
print "Time for itertools:", elapsed

start = time()
# Using manual algorithm
done = 0
i = 0
while not done:
	done = next_perm(arr, n)
	i += 1
	if not done:
		if i == nth:
			print arr
			print str(arr).replace(", ", "")
			break

elapsed = (time() - start)
print "Time for manu:", elapsed
