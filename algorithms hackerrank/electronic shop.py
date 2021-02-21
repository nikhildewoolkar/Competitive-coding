def getMoneySpent(key, drive, b):
    k=sorted(key,reverse=True)
    d=sorted(drive)
    max=0
    if(k[len(k)-1]+d[0]>b):
        print(-1)
    else:
        for i in range(len(k)):
            for j in range(len(d)):
                if(k[i]+d[j]>max and k[i]+d[j]<=b):
                    max=k[i]+d[j]
        print(max)
            

bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)
