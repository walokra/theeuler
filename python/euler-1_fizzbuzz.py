# Problem 1
# 05 October 2001
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168
# 

#!/usr/bin/python
sum = 0
max = 1000
for i in range(1,max):
	if i%3 == 0 or i%5 == 0:
		sum = sum + i
print 'sum of 3/5 modulos < ' + str(max) + ': ' + str(sum)
