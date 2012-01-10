#!/usr/bin/python
sum = 0

for i in range(1,1000):
	if i%3 == 0 or i%5 == 0:
		sum = sum + i
		print i
print 'sum of 3/5 modulos < 1000:'
print sum
