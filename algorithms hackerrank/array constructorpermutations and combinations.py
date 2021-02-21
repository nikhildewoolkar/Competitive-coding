# from itertools import combinations
# import itertools
# def score(Arr,Brr,N):
#     sum1=0
#     for i in range(N):
#         sum1+=(Arr[i]+Brr[i])%2
#     return sum1
# from math import comb
import operator as op
from functools import reduce
# import scipy.misc
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2
n=int(input())
for i in range(n):
    a,b=map(int,input().strip().split())
    # arr=list(itertools.product([0, 1], repeat=a))
    # brr=list(itertools.product([0, 1], repeat=a))
    f=2**a
    # print(f**2)
    # c=comb(a,b)
    # c=scipy.misc.comb(a,b)
    c=ncr(a,b)
    # for j in range(len(arr)):
    #     for k in range(len(brr)):
    #         s=score(list(arr[j]),list(brr[k]),a)
    #         if(s==b):
    #             c+=1
    v=(c*f)%((10**9)+7)
    print(v)
