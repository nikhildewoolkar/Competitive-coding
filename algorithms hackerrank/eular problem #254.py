def split_to_digits(n):
    d = list(str(n))
    return [int(z) for z in d]
def fact(n):
    if n>1:
        return n* fact(n-1)
    else:
        return 1
def f(n):
    return sum([fact(z) for z in split_to_digits(n)])
def sf(n):
    return sum( split_to_digits(f(n)) )
def g(p):
    n = 1
    sf_val = sf(n)
    while sf_val != p:
        n+=1
        sf_val = sf(n)
    return n
def sg(p):
    return sum( split_to_digits( g(p) ) )
def gvalues():
    d=[]
    d[0]=0
    for i in range(0,40):
        d.append(sum([sg(i) for i in range(1,i+1)]))
def answer():
    c=[]
    d=[0, 1, 3, 8, 14, 21, 24, 28, 33, 39, 46, 54, 62, 71, 84, 93, 103, 114, 127, 141, 156, 172, 189, 207, 220, 234, 249, 258, 268, 279, 291, 304, 318, 330, 343, 357, 372, 391, 419, 443, 468, 505, 536, 568, 613 , 659 ,709]
    a=int(input())
    for i in range (0,a):
        g = list(map(int,input().split()))
        if g[0]<47:
            print(d[g[0]])
        else:
            print(sum([sg(i) for i in range(47,g[0]+1)]))
    """for j in range(0,a):
        if c[j]<47 :
            print(d[c[j]])
        else:
            print(sum([sg(i) for i in range(1,g[i]+1)]))"""
answer()
5
