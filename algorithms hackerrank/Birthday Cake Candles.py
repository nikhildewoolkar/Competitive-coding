from itertools import groupby
result=[]
n = int(input())
g = list(map(int,input().split()))
g.sort(reverse=True)
count=1
for i in range(0,len(g)):
    if(g[i]==g[i+1]):
        count=count+1
    else:
        break
print(count)
