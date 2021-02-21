def minimumBribes(q):
    c=0
    for i in range(len(q)):
        if(q[i]-(i+1)>2):
            print("Too chaotic")
            return
        else:
            for j in range(q[i]-2,i):
                if(q[j]>q[i]):
                    c+=1
    print(c)
t = int(input())
for t_itr in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    minimumBribes(q)
"""
def minimumBribes(q):
    c=0
    for i in range(len(q)):
        if(q[i]-(i+1)>2):
            print("Too chaotic")
            return
        else:
            for j in range(q[i]-2,i):
                if(q[j]>q[i]):
                    c+=1
    if(q.index(1)==len(q)-1):
        print(c)
    else:
        print(c-1)
t = int(input())
for t_itr in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    minimumBribes(q)
