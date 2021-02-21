def absolutePermutation(n, k):
    arr=[]
    count=1
    if(k!=0):
        if(n%2!=0 or n%(k*2)!=0):
            print("-1")
        elif(n%2==0 and n%(k*2)==0):
            for i in range(n//(k*2)):
                for i in range(k):
                    arr.append(count+k)
                    count+=1
                for i in range(k):
                    arr.append(count-k)
                    count+=1
            print(*arr)
        elif(n%2==0 and k*2==n):
            while(count+k<=n):
                arr.append(count+k)
                count+=1
            # print(count)
            while(count-k<=k):
                arr.append(count-k)
                count+=1
            print(*arr)
    else:
        co=1
        a=[]
        while(co<=n):
            a.append(co)
            co+=1
        print(*a)
t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    absolutePermutation(n, k)
