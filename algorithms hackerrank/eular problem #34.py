def facto(a1):
    fact=1
    for i in range(1,a1+1):
        fact=fact*i
    return fact
a=int(input())
arr=[]
res=0
for i in range(10,a):
    c=0
    z=i
    while(z>0):
        b=int(z % 10)
        arr.append(b)
        c=c+facto(b)
        z=int(z/10)
        # print(arr,z,c)
    if(c%i==0):
        # print("c and i",c,i,c%i)
        res+=i
    # print("res",res)
print(res)
