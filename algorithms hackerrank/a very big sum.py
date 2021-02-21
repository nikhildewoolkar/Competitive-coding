a=int(input())
b = list(map(int,input().split()))
c=0
for i in range(0,a):
    c=b[i]+c
print(c)
