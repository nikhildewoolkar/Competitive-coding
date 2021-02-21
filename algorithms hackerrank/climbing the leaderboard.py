def climbingLeaderboard(s,a):
    t=list(sorted(set(s),reverse=True))
    for j in range(len(a)):
        flag=0
        for i in range(len(t)): 
            if(a[j]>t[i]):
                print(i+1)
                flag=1
                break
            elif(a[j]==t[i]):
                print(i+1)
                flag=1
                break
        if(flag==0):
            print(len(t)+1)
input()
s = list(map(int, input().rstrip().split()))
input()
a = list(map(int, input().rstrip().split()))
climbingLeaderboard(s,a)
