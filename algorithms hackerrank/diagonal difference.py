a=int(input())
x=0
y=a-1
sum1=0
sum2=0
for i in range(0,a):
        b = list(map(int,input().split()))
        sum1=sum1+b[x]
        x=x+1
        sum2=sum2+b[y]
        y=y-1
print(abs(sum1-sum2))
