def chocolateFeast(n,c,m):
    k=n//c
    count=k
    while(k>=m):
        count+=(k//m)
        k=(k%m)+(k//m)
    print(count)
t = int(input())
for t_itr in range(t):
    ncm = input().split()
    n = int(ncm[0])
    c = int(ncm[1])
    m = int(ncm[2])
    chocolateFeast(n,c,m)
