def find(a):
    i=a[0]
    j=a[1]
    x=a[2]
    y=a[3]
    c=0
    s1=[[i,j],[i-1,j-2],[i-2,j-1],[i+1,j-2],[i+2,j-1],[i-1,j+2],[i-2,j+1],[i+1,j+2],[i+2,j+1]]
    s2=[[x,y],[x-1,y-2],[x-2,y-1],[x+1,y-2],[x+2,y-1],[x-1,y+2],[x-2,y+1],[x+1,y+2],[x+2,y+1]]
    i=0
    while i<len(s1):
        if s1[i][0]<1 or s1[i][0]>8 or s1[i][1]<1 or s1[i][1]>8:
            s1.pop(i)
        else:
            i+=1
    i=0
    while i<len(s2):
        if s2[i][0]<1 or s2[i][0]>8 or s2[i][1]<1 or s2[i][1]>8:
            s2.pop(i)
        else:
            i+=1
    # print(s1,s2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if(s1[i]==s2[j]):
                return(1)   
n=int(input())
for i in range(n):
    a=list(map(int, input().rstrip().split()))
    c=find(a)
    if(c==1):
        print("YES")
    else:
        print("NO")



        
def find(a):
    t=[[0 for i in range(18)] for j in range(18)]
    i=a[0]+5
    j=a[1]+5
    x=a[2]+5
    y=a[3]+5
    t[i][j]=1
    t[x][y]=1
    t[i-1][j-2]=1
    t[i-2][j-1]=1
    t[i+1][j-2]=1
    t[i+2][j-1]=1
    t[i-1][j+2]=1
    t[i-2][j+1]=1
    t[i+1][j+2]=1
    t[i+2][j+1]=1
    t[x-1][y-2]=1
    t[x-2][y-1]=1
    t[x+1][y-2]=1
    t[x+2][y-1]=1
    t[x-1][y+2]=1
    t[x-2][y+1]=1
    t[x+1][y+2]=1
    t[x+2][y+1]=1
    c=0
    for l in range(5,18-5):
        for k in range(18):
            if(t[l][k]==1):
                c+=1
    if(c<=16):
        print("YES")
    else:
        print("NO")
n=int(input())
for i in range(n):
    a=list(map(int, input().rstrip().split()))
    find(a)

def find(a):
    i=a[0]
    j=a[1]
    x=a[2]
    y=a[3]
    c=0
    s1=[[i,j],[i-1,j-2],[i-2,j-1],[i+1,j-2],[i+2,j-1],[i-1,j+2],[i-2,j+1],[i+1,j+2],[i+2,j+1]]
    # for k in range(len(s1)):
    #     if(s1[k][0]<0 or s1[k][1]<0):
    #         del s1[k]
    s2=[[x,y],[x-1,y-2],[x-2,y-1],[x+1,y-2],[x+2,y-1],[x-1,y+2],[x-2,y+1],[x+1,y+2],[x+2,y+1]]
    # for k in range(len(s1)):
    #     if(s2[k][0]<0 or s2[k][1]<0):
    #         del s2[k]
    print(s1,s2)
    for i in range(len(s1)):
        if(s1[i][1]>0 and s1[i][0]>0):
            for j in range(len(s2)):
                if(s1[i]==s2[j]):
                    return(1)   
n=int(input())
for i in range(n):
    a=list(map(int, input().rstrip().split()))
    c=find(a)
    if(c==1):
        print("YES")
    else:
        print("NO")
