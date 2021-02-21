b = list(map(int,input().split()))
b.sort()
sum1=sum2=0
for i in range(0,4):
    sum1=b[i]+sum1
for i in range(1,5):
    sum2=b[i]+sum2
print(sum1,sum2)
