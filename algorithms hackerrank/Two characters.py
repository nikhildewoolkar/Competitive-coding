from itertools import combinations
def isAlter(s):
    for i in range(1,len(s)):
        if(s[i]==s[i-1]):
            return False
    return True
def alternate(s):
    v=list(set(s))
    b=len(v)-2
    if(len(v)<2):
        print(0)
    else:    
        d=list(combinations(v,b))
        m=0
        for i in range(len(d)):
            s1=s
            for j in range(b):
                s1=s1.replace(d[i][j],'')
            if(isAlter(s1)==True):
                m=max(m,len(s1))
        print(m)
l = int(input().strip())
s = input()
alternate(s)
