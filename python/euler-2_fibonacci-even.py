#!/usr/bin/python
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# Find the sum of all the even-valued terms in the sequence which do not exceed one million.

sum = 0
next = 2
max = 1000000
prev = 1
while next < max:
	next_t = next
	next = next + prev
	prev = next_t

	if next_t % 2 == 0:
		sum = sum + next_t

print "sum of all even terms < " + str(max) + ": " + str(sum)