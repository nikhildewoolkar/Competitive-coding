T = int(input())
while(T>0):
    T -= 1 
    N = int(input()) 
    g = list(map(int,input().split(",")))
    print(g)
    o = list(map(int,input().split()))
    g.sort()
    o.sort()
    count = 0 
    for i in range(N):
        for j in range(count,N):
            if(g[i]>o[j]):
                count +=1 
                break 
            else:
                break 
    print(count)
