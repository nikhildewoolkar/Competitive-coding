n=int(input())
a=[]
for i in range(n):
    r=list(map(int,input().strip().split()))
    a.append(r)
z=int(input())
t=0
for i in range(z):
    b,r1,r2= map(int, input().split())
    count=0
    b=b-t
    for j in range(r1-1,r2):
        g=(b*a[j][2])
        if(g<=a[j][1]):
            count+=g
        else:
            count+=a[j][1]
    t=b
    print(count)


n=int(input())
a=[]
b=[]
for i in range(n):
    r=list(map(int,input().strip().split()))
    a.append(r)
z=int(input())
for i in range(z):
    t=list(map(int,input().strip().split()))
    b.append(t)
for i in range(z):
    count=0
    if(i!=0):
        b[i][0]=b[i][0]-b[i-1][0]
    for j in range(b[i][1]-1,b[i][2]):
        g=(b[i][0]*a[j][2])
        if(g<a[j][1]):
            count+=g
        else:
            count+=a[j][1]
    print(count)


def calc(l1,l2,l3,h,list1,list2,list3):
    for i in range(h):    
        sum=0
        if i!=0:
            l1[i]=l1[i]-l1[i-1]
        for k in range(l2[i]-1,l3[i]):
            if list3[k]*l1[i]<list2[k]:
                sum+=list3[k]*l1[i]
            else:
                sum+=list2[k]        
        print(sum) 

t=int(input())
list1=[]
list2=[]
list3=[]
for i in range(t):
    
    a,b,c = [int(l) for l in input().split()] 
    list1.append(a)
    list2.append(b)
    list3.append(c)
h=int(input())
l1=[]
l2=[]
l3=[]
for i in range(h):
    x,y,z = [int(l) for l in input().split()]
    l1.append(x)
    l2.append(y)
    l3.append(z)
calc(l1,l2,l3,h,list1,list2,list3)



n=int(input())
a=[]
for i in range(n):
    r=list(map(int,input().strip().split()))
    a.append(r)
z=int(input())
t=0
for i in range(z):
    b,r1,r2= map(int, input().split())
    count=0
    for j in range(r1-1,r2):
        count+=min((a[j][2]*b)-(a[j][2]*t),a[j][1])
    t=b
    print(count)
