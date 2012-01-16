#!/usr/bin/python
#
# Problem 9
# 25 January 2002
# 
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#       a^2 + b^2 = c^2
#
# For example,
#        3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# 
# Find the product abc.
#
# Answer: 31875000
# (a: 375 ; b: 200 ; c: 425 ; sum= 1000)
#

from time import time

# a + b + c = 1000
# a^2 + b^2 = c^2
# c = 1000 - (a + b)
# a^2 + b^2 = (1000 - a - b)*(1000 - a - b)
# a^2 + b^2 = 1000000 - 1000a - 1000b - 1000a + a^2 + ab - 1000b + ab + b^2
# 0 = 1000000 - 2000a - 2000b + 2ab
# 2000a + 2000b - 2ab = 1000000
# 1000a + 1000b - ab = 500000
# a = (500000 - 1000b)/(1000 - b)
def bf(result):
        sum_ = 0
        b = 1
        while result > sum_:
                if (500000 - 1000*b)%(1000 - b) == 0:
                        a = (500000 - 1000*b)/(1000 - b)
                        c = 1000 - a - b
                        sum_ = a + b + c
                        print "a:", a, "; b:", b, "; c:", c, "; sum=", sum_
                        print "product:", a*b*c
                b +=1
                
start = time()
max_ = 1000
bf(max_)
elapsed = (time() - start)
print "Time:", elapsed
