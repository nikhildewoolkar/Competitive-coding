def reverse(n): 
    rev = 0
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10
    return rev 
def beautifulDays(i, j, k):
    count=0
    for p in range(i,j+1):
        if((abs(reverse(p))-p)%k==0):
            count+=1
    print(count)
ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
result = beautifulDays(i, j, k)
