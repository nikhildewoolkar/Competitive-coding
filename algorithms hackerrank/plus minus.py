a=int(input())
b = list(map(int,input().split()))
c1=c2=c3=0
for i in range(0,a):
    if b[i]>0:
        c1=c1+1
    elif b[i]<0:
        c2=c2+1
    else:
        c3=c3+1
print(c1/a)
print(c2/a)
print(c3/a)
