#!/usr/bin/python
#
# Problem 17
# 17 May 2002
# 
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# 
# Answer: 
# 

from time import time

# Main
#
start = time()

sum = 0
l0=0
l1=int(len("One"))
l2=int(len("Two"))
l3=int(len("Three"))
l4=int(len("Four"))
l5=int(len("Five"))
l6=int(len("Six"))
l7=int(len("Seven"))
l8=int(len("Eigth"))
l9=int(len("Nine"))
l10=int(len("Ten"))
l11=int(len("Eleven"))
l12=int(len("Twelve"))
l13=int(len("Thirteen"))
l14=int(len("Fourteen"))
l15=int(len("Fifteen"))
l18=int(len("Eighteen"))
l20=int(len("Twenty"))
l30=int(len("Thirty"))
l40=int(len("Forty"))
l50=int(len("Fifty"))
l80=int(len("Eighty"))
l100=int(len("Hundred"))
l1000=int(len("OneThousand"))
a=int(len("and"))

nums = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15]

s0=""
s1="One"
s2="Two"
s3="Three"
s4="Four"
s5="Five"
s6="Six"
s7="Seven"
s8="Eight"
s9="Nine"
s10="Ten"
s11="Eleven"
s12="Twelve"
s13="Thirteen"
s14="Fourteen"
s15="Fifteen"
s18="Eighteen"
s20="Twenty"
s30="Thirty"
s40="Forty"
s50="Fifty"
s80="Eighty"
s100="Hundred"
s1000="OneThousand"
sa="and"

snums = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15]

for i in range(1, 1001):
	if i >= 10:
	 	pretens = int(str(i)[1:])
	 	if i >= 100:
		 	prehuns = int(str(i)[2:])
		 	prehuntens = int(str(i)[1:2])
		tens = int(str(i)[0:1])
		huns = int(str(i)[0:1])
	
	if i <= 15:
 		sum = sum + nums[i]
 		#print snums[i]

 	elif i > 15 and i < 20:
 		if i == 18:
 	 		sum = sum + l18
	 		#print s18
	 	else:
	 		sum = sum + nums[pretens] + int(len("teen"))
	 		#print snums[pretens] + "teen"
 		
 	elif i >= 20 and i < 30:
 		sum = sum + l20 + nums[i-20]
 		#print s20 +" " + snums[i-20]
 		
 	elif i >= 30 and i < 40:
 		sum = sum + l30 + nums[i-30]
 		#print s30 +" " + snums[i-30]
 		
 	elif i >= 40 and i < 50:
 		sum = sum + l40 + nums[i-40]
 		#print s40 +" " + snums[i-40]
 		
 	elif i >= 50 and i < 60:
 		sum = sum + l50 + nums[i-50]
 		#print s50 +" " + snums[i-50]
  			
 	elif i >= 60 and i < 100:
		if i >= 80 and i < 90:
			sum = sum + l80 + nums[pretens]
			#print s80 + " " + snums[pretens]
	
		else:
	 		sum = sum + nums[tens] + int(len("ty")) + nums[pretens]
	 		#print snums[tens] + "ty" + " " + snums[pretens]
 	
 	if i >= 100 and i < 1000:
 		x = huns*100
 		if i % x == 0:
 			sum = sum + nums[huns] + l100
 			#print snums[huns] + " " + s100
 		
 		elif i <= 15 + x:
 			sum = sum + nums[huns] + l100 + a + nums[i-x]
 			#print snums[huns] + " " + s100 + " " + sa + " " + snums[i-x]
	 	
	 	elif i > 15 + x and i < 20 + x:
	 		if i == 18 + x:
	 	 		sum = sum + nums[huns] + l100 + a + l18
		 		#print snums[huns] + " " + s100 + " " + sa + " "+ s18
		 	else:
	 			sum = sum + nums[huns] + l100 + a + nums[prehuns] + int(len("teen"))
	 			#print snums[huns] + " " + s100 + " " + sa + " " + snums[prehuns] + "teen"
 		
	 	elif i >= 20 + x and i < 30 + x:
	 		sum = sum + nums[huns] + l100 + a + l20 + nums[i-20-x]
	 		#print snums[huns] + " " + s100 + " " + sa + " " + s20 +" " + snums[i-20-x]
 		
 		elif i >= 30 + x and i < 40 + x:
 			sum = sum + nums[huns] + l100 + a + l30 + nums[i-30-x]
 			#print snums[huns] + " " + s100 + " " + sa + " " + s30 +" " + snums[i-30-x]
 		elif i >= 40 + x and i < 50 + x:
 			sum = sum + nums[huns] + l100 + a + l40 + nums[i-40-x]
 			#print snums[huns] + " " + s100 + " " + sa + " " + s40 +" " + snums[i-40-x]
 		
 		elif i >= 50 + x and i < 60 + x:
 			sum = sum + nums[huns] + l100 + a + l50 + nums[i-50-x]
 			#print snums[huns] + " " + s100 + " " + sa + " " + s50 +" " + snums[i-50-x]
 		
 		elif i >= 60 + x and i < 100 + x:
 		 	if i >= 80 + x and i < 90 + x:
 				sum = sum + nums[huns] + l100 + a + l80 + nums[prehuns]
 				#print snums[huns] + " " + s100 + " " + sa + " " +  s80 + " " + snums[prehuns]

 			else:
	 			sum = sum + nums[huns] + l100 + a + nums[prehuntens] + int(len("ty")) + nums[prehuns]
 				#print snums[huns] + " " + s100 + " " + sa + " " +  snums[prehuntens] + "ty" + " " + snums[prehuns]
 			 
	if i == 1000:
		sum = sum + l1000
		#print s1000
	 		
print sum

elapsed = (time() - start)
print "Time:", elapsed
