def kangaroo(x1, v1, x2, v2):
    x=x1
    y=x2
    flag=0
    while(x<=1000*v1*v2):
        x=x+v1
        y=y+v2
        # print(x,y)
        if(y==x):
            flag=1
            break
    if(flag==1):
        print("YES")
    else:
        print("NO")
    


x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
kangaroo(x1, v1, x2, v2)
