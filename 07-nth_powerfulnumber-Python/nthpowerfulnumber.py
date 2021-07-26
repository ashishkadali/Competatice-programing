# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.




def factors(n):

	l=[]
	for i in range(2,n):
		if n%i==0:
			if(prime(i)):
				l.append(i)
	return l

def prime(n):
	for i in range(2,n):
		if  n% i == 0:
			return False	
	else:
		return True

def powerful(m,num):
    if(len(m)==0):
        return False
    for j in m:
        if(num%(j**2) !=0):
            return False
    return True
def nthpowerfulnumber(n):
    # Your code goes here
    if(n==0):
        return 1
    i=1
    res=[]
    while(len(res)<n):
        p=factors(i)
        if(powerful(p,i)==True):
            res.append(i)
        i=i+1
        # print(res,'res')
    # print(res)
    return res[n-1]
print(nthpowerfulnumber(6))

		

	

nthpowerfulnumber(10)


