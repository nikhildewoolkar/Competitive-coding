"""def jumpingOnClouds(c):
    z=0
    s=[0]
    for i in range(len(c)):
        if((z+2)<len(c) and c[z+2]==0):
            s.append(z+2)
        elif((z+1)<len(c) and c[z+1]==0):
            s.append(z+1)
        z=s[-1]
        # print(s)
    print(len(s)-1)"""
def jumpingOnClouds(c):
    z=0
    count=0
    # s=[0]
    for i in range(len(c)):
        if((z+2)<len(c) and c[z+2]==0):
            # s.append(z+2)
            z=z+2
            count+=1
        elif((z+1)<len(c) and c[z+1]==0):
            # s.append(z+1)
            z=z+1
            count+=1
        # z=s[-1]
    #     print(s)
    # print(len(s)-1)
    print(count)

n = int(input())
c = list(map(int, input().rstrip().split()))
jumpingOnClouds(c)
