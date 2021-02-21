def birthday(s, d, m):
    k=0
    for i in range(len(s)):
        if(sum(s[i:i+m])==d):
            k+=1
    print(k)
n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
birthday(s,d,m)
