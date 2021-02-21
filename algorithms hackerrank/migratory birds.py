def migratoryBirds(a):
    b=list(sorted(set(a)))
    c=0
    for i in range(len(b)):
        if(c<a.count(b[i])):
            v=b[i]
            c=a.count(b[i])
    print(v)

    # print(max(a,key=a.count))

arr_count = int(input().strip())
a = list(map(int, input().rstrip().split()))
migratoryBirds(a)

