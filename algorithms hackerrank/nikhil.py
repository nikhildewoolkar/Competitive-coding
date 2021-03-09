import numpy as np
a=int(input("enter the numbers you want to do sort:-"))
print ("enter elements")
c=[]
c.append(a)
for i in range (0,a):
    b=int(input())
    
    c.append(b)

    
np.savetxt('array.csv', [c], delimiter=',', fmt='%d')

