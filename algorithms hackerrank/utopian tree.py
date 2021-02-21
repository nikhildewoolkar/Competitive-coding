
def utopianTree(n):
    h=1
    for i in range(1,n+1):
        if(i%2==0):
            h+=1
        else:
            h*=2
    print(h)
t = int(input())
for t_itr in range(t):
    n = int(input())
    utopianTree(n)
