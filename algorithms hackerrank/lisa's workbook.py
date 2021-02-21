import math
import os
import random
import re
import sys
def workbook(n, k, arr):
    p=1
    count=0
    for i in range(n):
        extra=arr[i]%k
        if(extra>0):
            tmp=int(arr[i]/k)+1
        else:
            tmp=int(arr[i]/k)
        q=0
        for j in range(p,p+tmp):
            if(arr[i]>=k):
                if(j>q and j<=q+k):
                    count=count+1
                q=q+k
                arr[i]=arr[i]-k
            else:
                if(j>q and j<=q+arr[i]):
                    count=count+1
        p=p+tmp
    print(count)
nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
workbook(n, k, arr)
"""def workbook(n, k, arr):
    count=0
    index=0
    d={}
    for i in arr:
        a=[(x+1) for x in range(i)]
        while(len(a)>=k):
            d[index]=a[0:k]
            del(a[0:k])
            index+=1
        if(len(a)):
            d[index]=a
            index+=1
        # print(d)
    for i in range(len(d)):
        if((i+1) in d[i]):
            count+=1
    print(count)"""
"""
def workbook(n, k, arr):
    count=0
    r=[]
    for i in arr:
        a=[(x+1) for x in range(i)]
        print(a)
        while(len(a)>=k):
            r.append(a[0:k])
            del(a[0:k])
        if(len(a)):
            r.append(a)
        print(r)
    for i in range(len(r)):
        if((i+1) in r[i]):
            count+=1
    return count
