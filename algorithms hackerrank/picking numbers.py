def pickingNumbers(a):
    b=list(sorted(set(a)))
    m=0
    n=0
    flag=0
    if(len(b)>1):
        for i in range(0,len(b)):
            x=a.count(b[i])
            if(i+1<len(b) and b[i+1]-b[i]<=1):
                flag=1
                c=a.count(b[i+1])+a.count(b[i])    
                if(m<c):
                    m=c
            if(m<x):
                m=x
        print(m)
    else:
        print(a.count(b[0]))            
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
pickingNumbers(a)

"""
def pickingNumbers(a):
    t=list(set(a))
    # print(t)
    m=0
    for i in t:
        if((i+1) in t):
            if(a.count(i+1)+a.count(i)>m):
                m=a.count(i+1)+a.count(i)
        if((i-1) in t):
            if(a.count(i-1)+a.count(i)>m):
                m=a.count(i-1)+a.count(i)
        m=max(m,a.count(i))
    return m
    """
