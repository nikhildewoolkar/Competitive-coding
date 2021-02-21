
def find(c):
    l=len(c)
    d=[]
    f= list([sum(i) for i in zip(*c)])
    for i in range(l):
        v=0
        for j in range(l):
            v+=c[i][j]
        d.append(v)
    for i in range(l):
        for j in range(l):
            if(f[i]==d[j]):
                f[i]=-1
                d[j]=-1
    if(f.count(-1)==l and d.count(-1)==l):
        print("Possible")
    else:
        print("Impossible")
q = int(input())
for q_itr in range(q):
    n = int(input())
    c = []
    for _ in range(n):
        c.append(list(map(int, input().rstrip().split())))
    find(c)


    tran=list(zip(*container))
    m1=[]
    m2=[]
    for i in range(len(container)):
            m1.append(sum(container[i]))
            m2.append(sum(tran[i]))
    if(sorted(m1)==sorted(m2)):
        return "Possible"
    else:
        return "Impossible"
