def nonDivisibleSubset(k,s):
    d={}
    for i in range(k):
        z=[]
        for j in s:
            if(j%k==i):
                z.append(j)
        d[i]=z
    res=0
    f=0
    # print(d)
    if(len(d[0])>0):
        f=1
    # print(f)
    for i in range(1,k//2+1):
        # print("i,k-i",i,k-i)
        if(k-i!=i and k-i<k):
            res+=max(len(d[i]),len(d[k-i]))
        elif(k-i==i):
            res+=1
        # print(res)
    print(res+f)
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
s = list(map(int, input().rstrip().split()))
result = nonDivisibleSubset(k, s)
