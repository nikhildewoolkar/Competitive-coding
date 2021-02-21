def saveThePrisoner(N, M, S):
    # v=(s-1)+(m%n)
    # if(v>n):
    #     print(v%n)
    # else:
    #     print(v)
    print(((S - 1 + M - 1) % N) + 1)
t = int(input())
for t_itr in range(t):
    nms = input().split()
    n = int(nms[0])
    m = int(nms[1])
    s = int(nms[2])
    saveThePrisoner(n, m, s)
