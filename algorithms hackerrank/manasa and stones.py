import math
import os
import random
import re
import sys
from itertools import combinations_with_replacement
def stones(n, a, b):
    res=[]
    l=list(combinations_with_replacement([a,b],n-1))
    # print("l",l)
    for i in l:
        if(sum(i) not in res):
            res.append(sum(i))
    print(*list(sorted(res)))
T = int(input())
for T_itr in range(T):
    n = int(input())
    a = int(input())
    b = int(input())
    result = stones(n, a, b)
