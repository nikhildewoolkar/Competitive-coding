def breakingRecords(scores):
    max=0
    min=0
    a=scores[0]
    b=scores[0]
    for i in range(1,len(scores)):
        if(a<scores[i]):
            max+=1
            a=scores[i]
        if(b>scores[i]):
            min+=1
            b=scores[i]
    print(max,min)
n = int(input())
scores = list(map(int, input().rstrip().split()))
breakingRecords(scores)
