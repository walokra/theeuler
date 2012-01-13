#!/usr/bin/python
sum = 0
max = 1000
for i in range(1,max):
	if i%3 == 0 or i%5 == 0:
		sum = sum + i
print 'sum of 3/5 modulos < ' + str(max) + ': ' + str(sum)
