def fairRations(B):
    count=0
    for i in B:
        if(i%2!=0):
            count+=1
    if(count%2==0):
        count=0
        for i in range(N):
            if(B[i]%2!=0):
                B[i]+=1
                B[i+1]+=1
                count+=2
        print(count)
    else:
        print("NO")

N = int(input())
B = list(map(int, input().rstrip().split()))
fairRations(B)
