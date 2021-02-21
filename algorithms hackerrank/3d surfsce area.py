def surfaceArea(a):
    res=0
    res1=0
    res3=0
    for i in range(h):
        res+=a[i][0]
        res3+=a[i][w-1]
        # print("res3",res3)
        for j in range(0,w-1):
            if(a[i][j+1]-a[i][j]>=0):
                res=res+a[i][j+1]-a[i][j]
    res1=sum(a[h-1])
    for i in range(h-1,0,-1):
        for j in range(0,w):
            if(a[i-1][j]-a[i][j]>=0):
                res1=res1+a[i-1][j]-a[i][j]
    res2=sum(a[0])
    # print("res2",res2)
    for i in range(h-1):
        for j in range(w):
                if(a[i+1][j]-a[i][j]>=0):
                    res2=res2+a[i+1][j]-a[i][j]
        # print(res2)

    for i in range(w-1,-1,-1):
        for j in range(h-1,0,-1):
            if(a[i][j-1]-a[i][j]>=0):
                res3=res3+a[i][j-1]-a[i][j]
        # print(res3)
    print(res1+res+res2+res3+2*(h*w))
HW = input().split()
h = int(HW[0])
w = int(HW[1])
A = []
for _ in range(h):
    A.append(list(map(int, input().rstrip().split())))
surfaceArea(A)
 #error
"""
