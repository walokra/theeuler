#!/usr/bin/python
#
# Problem 48
# 18 July 2003
# 
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# 
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
# 
# Answer: 
# 

from time import time

# Main
#
t_start = time()

i = 1
max = 1000
s = 0
for i in range(1, max+1):
	s = s + i**i
	
print str(s)
print str(s)[-10:]

t_elapsed = (time() - t_start)
print "Time:", t_elapsed
