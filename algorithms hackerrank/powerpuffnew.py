result=[]
n=int(input())
inp1 = list(map(int,input().split()))
inp2 = list(map(int,input().split()))
res = [i / j for i, j in zip(inp2,inp1)]
for i in range(len(res)):
    t = int(res[i])
    result.append(t)
del res[:]
result.sort()
print(result[0])
