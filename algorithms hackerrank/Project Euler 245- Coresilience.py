#Project Euler #245: Coresilience
"""import math
def primeFactors(n): 
    fac = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        fac.append(2) 
        n = n // 2

        # n must be odd at this point 
        # so a skip of 2 ( i = i + 2) can be used 
        for i in range(3,int(math.sqrt(n))+1,2):
            # while i divides n , print i ad divide n 
            while n % i== 0:
                fac.append(i) 
                n = n // i 

            # Condition if n is a prime 
            # number greater than 2 
            if n > 2: 
                fac.append(n)
            fac1 = list(set(fac))
            return fac1    


def fi(n):
    arr1 = primeFactors(n)
    for i in range(len(arr1)):
        n = n*(arr1[i]-1)/(arr1[i])
    return n

if __name__ == "__main__":
    n = int(input())
    phi = []
    for i in range(2,n+1):
        phi.append(int(fi(i)))
    summm = 0
    for j in range(n-1):
        k = j+2
        if k - phi[j] == 1 or  phi[j]%(k-1) == 0:
            summm+= k
    print(summm)
"""
n=int(input())
def nik(num):
    count=1
    c=0
    for i in range(2,num):
        if num%i==0:
            count=count+1
    if n-1 % n-count == 0:
       c=1
    return c
for i in range (0,n+1):
    v=0
    b=nik(i)
    if b == 1:
       v=v+i 
print (v)

    
