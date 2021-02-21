# a=[10,6,2,3,7,1,2]
# b=[1,2,2,3,6,7,10]
len(a)=7
for i in range(len(a)):
    d=b.index(a[i])+1
    if()
    len(a)
# c=[0,0,0,0,0,0,0]
# d=[0,0,0,0,0,0,0]
#f=[1,2,2,3,6,7,10]
a=list(map(int,input().split()))
b=list(sorted(a))
c=[]
c=[0]*len(a)
count=0
g=0
for i in range(len(a)):
    g= len(b) - b[::-1].index(a[i]) - 1
    if(a[i] in c):
        g-=c.count(a[i])
    if(c.count(0)==len(a)):
        c[g]=a[i]
        count+=1
    elif(a[i]<=a[i-1] and c[:g].count(0)== g):
        c[g]=a[i]
        count+=1
    elif(a[i]>=a[i-1] and c[g:].count(0)== len(c)-g):
        c[g]=a[i]
        count+=1
    elif(a[i]<=a[i-1] and c[:g].count(0)!=g):
        f=min(abs(len(c[g:])-c[g:].count(0)),len(c[:g])-abs(c[:g].count(0)))*2
        count+=f+1
        c[g]=a[i]
    elif(a[i]>=a[i-1] and c[g:].count(0)!=len(c)-g):
        f=min( abs(len(c[g:]) - c[g:].count(0)) ,abs( (len(c[:g]) - c[:g].count(0))))*2
        count+=f+1
        c[g]=a[i]
    # print(c)
    # print(count)
print(count)

#count=13
#[1,2,2,3,6,7,10]
