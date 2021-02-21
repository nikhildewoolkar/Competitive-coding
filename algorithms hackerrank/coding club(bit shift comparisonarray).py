def logic(a,b):
    a1=[]
    b1=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==b[j]):
                a[i],b[j]=0,0
    for i in range(len(a)):
        if(a[i]!=0):
            a1.append(a[i])
    for i in range(len(b)):
        if(b[i]!=0):
            b1.append(b[i])
    if(len(a1)!=len(b1)):
        print("NO")
        return
    else:
        c=0
        for i in range(len(a1)):
            for j in range(len(b1)):
                if(a1[i]>b1[j]):
                    while(a1[i]>b1[j]):
                        a1[i]=a1[i]>>1
                        if(a1[i]==b1[j]):
                            a1[i]=0
                            b1[j]=0
                else:
                    while(a1[i]<b1[j]):
                        a1[i]=a1[i]<<1
                        if(a1[i]==b1[j]):
                            a1[i]=0
                            b1[j]=0
        if(a1.count(0)==len(a1)):
            print("YES")
        else:
            print("NO")
t=int(input())
s=int(input())
a=list(map(int, input().rstrip().split()))
b=list(map(int, input().rstrip().split()))
logic(a,b)
