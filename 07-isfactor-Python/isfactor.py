# Write the function isFactor(f, n) that takes two int values f and n, 
# and returns True if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	if n==0:
		return True
	if n!=0:	
		l=[]
		for i in range(1,n+1):
			if n%i==0:
				l.append(i)
		if abs(f) in l:
			return True
		else:
			return False



	# replace with your solution
