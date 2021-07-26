# ishappynumber(n) [10 pts]
# A happy number is a number defined by the following process: Starting with any positive integer, replace the 
# number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will 
# stay ), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 
# are happy numbers.

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# Write the function ishappynumber(n) which takes a possibly-negative integer and returns True if it is happy and 
# False otherwise. Note that all numbers less than 1 are not happy. Here are some test assertions for you:
# assert(ishappynumber(-7) == False)
# assert(ishappynumber(1) == True)
# assert(ishappynumber(2) == False)
# assert(ishappynumber(97) == True)
# assert(ishappynumber(98) == False)
# assert(ishappynumber(404) == True)
# assert(ishappynumber(405) == False)

def ishappynumber(n):
	l=[]
	l.append(n)
	if n<0 or n==0:
		return False

	if n==1:
		return True
	# if n==2:
	# 	return False
			# your code goes here
	n=int(n)
	while n>1:
		a=str(n)
		sum=0
		for i in a:
			sum=sum+(int(i)**2)
		n=int(sum)
		if sum==1:
			return True

		elif sum in l:
			return False
		else:
			l.append(sum)

		
	return True

print(ishappynumber(2))
