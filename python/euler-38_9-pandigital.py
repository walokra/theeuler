#!/usr/bin/python
# 
# Problem 38
# 28 February 2003
# 
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 * 1 = 192
# 192 * 2 = 384
# 192 * 3 = 576
# 
# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying 
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
# which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed 
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?
# 
# Answer: 
# 

from time import time

# Check if given number is 1 to 9 pandigital
# (has all digits from 1 to 9 at least once)
# 
def check_pandigital(n):
	s = str(n)
	for i in range(1, 10):
		if s.find(str(i)) == -1:
			return False
	
	return True

# Create concatenated products 
# starting with n and ending when its lenght is bigger than max_len
#
def conc_products(n, max_len):
	product = ""
	products = []
	i = 1
	while 1:
		product = product + str(n * i)
		if len(product) <= max_len:
			products.append(product)
		else:
			break
		i += 1

	return products

# Main
#
start = time()

#start = 123456789
#end = 987654321
start = 2
# can end after 9999 because it's (1,2,3) is bigger than 9 digits
end = 9999
max_len = 9
pandigitals = []

for n in range(start, end):
	for x in conc_products(n, max_len):
		x = int(x)
		if check_pandigital(x):
			pandigitals.append(str(x))

pandigitals.sort(key=int)
print pandigitals[-1]

elapsed = (time() - start)
print "Time:", elapsed
