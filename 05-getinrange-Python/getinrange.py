# Write the function getInRange(x, bound1, bound2) which takes 3 int values x, bound1, and bound2, 

# where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified.  
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.




# b1<b2 or b1>b2

def fun_getinrange(x, bound1, bound2):
	
	l=[bound1,bound2]
	a=max(l)
	b=min(l)
	if x in range(bound1,bound2):
		return x
	elif x>a:
		return a
	elif x<b:
		return b


		

	

	
	