st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
p = list(map(int, input().rstrip().split()))
q = list(map(int, input().rstrip().split()))
x=[]
y=[]
count1=0
count2=0
for i in range (0,m):
    if s<=p[i]+a and t>=p[i]+a:
        count1=count1+1
for i in range (0,n):
    if s<=q[i]+b and t>=q[i]+b:
        count2=count2+1
print(count1)
print(count2)
