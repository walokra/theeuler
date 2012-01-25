#!/usr/bin/python
#
# Problem 16
# 03 May 2002
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
# Answer: 
# 

from time import time

# Main
#
start = time()

square = 2**1000
sum = 0
for i in range(0, len(str(square))):
	sum = sum + int(str(square)[i])

print sum

elapsed = (time() - start)
print "Time:", elapsed
