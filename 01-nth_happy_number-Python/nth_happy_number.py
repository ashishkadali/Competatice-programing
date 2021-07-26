# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def ishappynumber(n):
        l=[]
        l.append(n)
        if n<0:
            return False
    
        if n==1:
            return True
        # if n==2:
        #     return False
                # your code goes here
        n=int(n)
        while n>1:
            a=str(n)
            sum=0
            for i in a:
                sum=sum+(int(i)**2)
            n=int(sum)
            print(sum)
            if sum==1:
                return True
                
            elif sum in l:
                return False
            else:
                l.append(sum)
        # return True
    
    # print(ishappynumber(19))

def nth_happy_number(n):
    f = 1
    g = 0
    while(f<=abs(n)):
        g+=1
        if(ishappynumber(g)):
            f+=1
    return g

print(nth_happy_number(2))