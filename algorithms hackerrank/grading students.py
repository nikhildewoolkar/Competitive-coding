a=int(input())
b=[]
for i in range(0,a):
    r=int(input())
    b.append(r)
for i in range(0,a):    
    c=5*(int(b[i]/5)+1)
    if(b[i]>37):
        if(c-b[i]<3):
            print(c)
        else:
            print(b[i])
    else:
        print (b[i])
