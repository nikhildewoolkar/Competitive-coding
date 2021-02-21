def circularArrayRotation(a, k, q):
    g=len(a)-k
    a=a[g:]+a[:g]
    for i in q:
        print(a[i])
    c=[]
    a=deque(a)
    a.rotate(k)
    c=(list([a[m] for m in q]))
    for i in c:
        print(i)
nkq = input().split()
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))
queries = []
for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)
result = circularArrayRotation(a, k, queries)

