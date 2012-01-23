#!/usr/bin/python
#
# Problem 14
# 05 April 2002
# 
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13  40  20  10  5  16  8  4  2  1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# Answer: 
# 

from time import time

def max_len(dict_,(key,val)):
	dict_[key] = val
	return dict_
    
def chain_recur(n, d):
	if n == 1: return d
	current=n
	next=current
	seq = []
	seq.append(current)

	while next > 1:
		#print "cur:", current, "next:", next
		if current % 2 == 0:
			next = current/2
		else:
			next = 3*current + 1
		current = next
		seq.append(current)
	#print seq
		
	d = max_len(d, (n, len(seq)))
	
	return chain_bf(n-1, d)

def chain_bf(n, d):
	for i in range(n, 1, -1):
		current=i
		next=current
		seq = []
		seq.append(current)
		while next > 1:
			if current % 2 == 0:
				next = current/2
			else:
				next = 3*current + 1
			current = next
			seq.append(current)
		
		d = max_len(d, (i, len(seq)))
	
		#print d
		#print seq
	
# Main
#
start = time()

n = 999999
d = dict([(x,x+1) for x in range(1, n+1)])
chain_bf(n, d)
print max(d, key=d.get)

elapsed = (time() - start)
print "Time:", elapsed
