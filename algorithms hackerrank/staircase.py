a=int(input())
for i in range(0,a):
    for j in range(a,i+1,-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("#",end="")
    print("\r")
