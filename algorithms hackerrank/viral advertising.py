def viralAdvertising(n):
    count=0
    c=5
    for i in range(n):
        count+=(c//2)
        c=(c//2)*3
    print (count)           
n = int(input())
viralAdvertising(n)

