import math
def isPrime(n):  
    if n <= 1: 
        return False
    for i in range(2, int(math.sqrt(n)+1)): 
        if n % i == 0: 
            return False; 
    return True

m,n=map(int,input().split())
mat=[]
for i in range(m):
    mat.append(list(map(int,input().strip().split())))
maxi=[]
maxj=[]
for i in range(m):
    count=0
    for j in range(n):
        if(isPrime(mat[i][j])==True):
            count+=1
    maxi.append(count)
for i in range(n):
    count=0
    for j in range(m):
        if(isPrime(mat[j][i])==True):
            count+=1
    maxj.append(count)
c=0
if(max(maxi)>=max(maxj)):
    print("nick")
    o=max(maxi)
    for j in range(n):
        if(isPrime(mat[o][j])==False):
            while(isPrime(mat[o][j])==False):
                mat[o][j]+=1
                print(mat[j][o])
                c+=1
    print (c-1)
elif(max(maxi)<max(maxj)):
    print("nick")
    o=max(maxj)
    for j in range(m):
        if(isPrime(mat[j][o])==False):
            while(isPrime(mat[j][o])==False):
                mat[j][o]+=1
                print(mat[j][o])
                c+=1
    print (c-1) 
    
