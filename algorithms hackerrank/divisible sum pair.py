def divisibleSumPairs(n, k, a):
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if((a[i]+a[j])%k==0):
                c+=1
    print(c)

nk = input().split()
n = int(nk[0])
k = int(nk[1])
a = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, a)
