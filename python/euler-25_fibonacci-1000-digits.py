#!/usr/bin/python
#
# Problem 25
# 30 August 2002
# 
# The Fibonacci sequence is defined by the recurrence relation:
# 
# Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# 
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the first term in the Fibonacci sequence to contain 1000 digits?
# 
# Answer: 
# 

from time import time

# Returns the values from fibonacci sequence
#
def fibonacci_seq():
	next, prev, iter = 1, 1, 1
	while 1:
		yield next, iter
		next, prev, iter = prev, next+prev, iter+1
	
# Main
#
start = time()

digits = 1000
for num, term in fibonacci_seq():
	if len(str(num)) == digits:
		break

print "1st Fibonacci term with", str(digits), "digits:"
print term

elapsed = (time() - start)
print "Time:", elapsed
