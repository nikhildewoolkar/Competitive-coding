import math
def isPrime(n):  
    if n <= 1: 
        return False
    for i in range(2, int(math.sqrt(n)+1)): 
        if n % i == 0: 
            return False; 
    return True
def prime(n,m,k):
    p=0
    l=[]
    for j in range(10**(n-1),10**(n)):
        count=0
        for i in range(n):
            f=(j//pow(10,n-(i+1)))%10
            if(isPrime(i+1)==True):
                if(isPrime(f)==True):
                    count+=1
                else:
                    break
            elif(isPrime(i+1)==False):
                if(isPrime(f)==False):
                    count+=1
                else:
                    break
        if(count==n):
            print(j)
            l.append(j)
            if(j%m==k):
                p+=1
    print(l)
    print(p)
t = int(input())
for i in range(t):
    n = int(input())
    m = int(input())
    k = int(input())
    result = prime(n,m,k)
"""def binary_search(arr, low, high, x): 
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return True
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x) 
    else:  
        return False
def prime(n,m,k,l,s):
    p=0
    s=[2,3,5,7]
    for j in range(10**(n-1),10**(n)):
        count=0
        if(j%m==k):
            for i in range(n):
                f=(j//pow(10,n-(i+1)))%10
                if(binary_search(l,0,len(l)-1,i+1)==True):
                    if(binary_search(s,0,len(s)-1,f)==True):
                        count+=1
                    else:
                        break
                elif(binary_search(l,0,len(l)-1, i+1)==False):
                    if(binary_search(s,0,len(s)-1,f)==False):
                        count+=1
                    else:
                        break
            if(count==n):
                p+=1
    print(p)
t = int(input())
l=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
s=[2, 3, 5, 7]
for i in range(t):
    n = int(input())
    m = int(input())
    k = int(input())
    result = prime(n,m,k,l,s)
"""
import math
def binary_search(arr, low, high, x): 
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return True
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x) 
    else:  
        return False
def prime(n,m,k,l):
    p=0
    s=[2,3,5,7]
    for j in range(10**(n-1),10**(n)):
        count=0
        for i in range(n):
            f=(j//pow(10,n-(i+1)))%10
            if(binary_search(l,0,len(l)-1,i+1)==True):
                if(binary_search(s,0,len(s)-1,f)==True):
                    count+=1
                else:
                    break
            elif(binary_search(l,0,len(l)-1, i+1)==False):
                if(binary_search(s,0,len(s)-1,f)==False):
                    count+=1
                else:
                    break
        if(count==n):
            if(j%m==k):
                p+=1
    print(p)
t = int(input())
l=[]
for i in range(t):
    n = int(input())
    m = int(input())
    k = int(input())
    for j in range(1,501):  
        if j <= 1: 
            break
        for i in range(2, int(math.sqrt(n)+1)): 
            if j % i == 0: 
                break 
        l.append(j)
    print(l)
    result = prime(n,m,k,l)

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
5 20 80 480 480 9370 11520

12334342424234"""

