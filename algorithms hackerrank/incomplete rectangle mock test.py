a=int(input())
for j in range(a):
    b=int(input())
    d1={}
    d2={}
    for i in range((b*4)-1):
        v,w=map(int,input().strip().split())
        if(v in d1.keys()):
            d1[v]+=1
        else:
            d1[v]=1
        if(w in d2.keys()):
            d2[w]+=1
        else:
            d2[w]=1    
    res=[]    
    for i in d1.keys():
        if(d1[i]%2!=0):
            res.append(i)
    for i in d2.keys():
        if(d2[i]%2!=0):
            res.append(i)
    print(*res)
