#!/usr/bin/python
#
# Problem 4
# 16 November 2001
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609
#

def isPalindrome(string):
	chars = [n for n in string]
	#print chars
	return (chars == chars[::-1])

result = []
min = 100
max = 1000
for i in range(min, max):
	for j in range(min, max):
		#print "product: " + str(i) + " * " + str(j)
		product = i * j
		if isPalindrome(str(product)):
			result.append(product)

print "The largest palindrome made from the product of two 3-digit numbers"
result.sort(key=int)
#print result
print result[-1]


