import math
import os
import random
import re
import sys
p=int(input())
def pooh(p):
    count=0
    n=p*2
    while(n>0):
        count=count+1
        n=n//10
    n=10**(count-1)
    if(p<=4):
        count=0
        for i  in range(1,p):
                count+=i    
        print(count)
        return
    else:
        count=0
        for i  in range(1,p+1):
            for j in range(i,p+1):
                if((i+j)%n==n-1):
                    count+=1
                    print(i,j)
        print(count)
pooh(p)
