import numpy 
a=int(input("enter the numbers you want to do sort:-"))
print "enter elements"
c=[]
for i in range (0,a):
    b=int(input())
    
    c.append(b)
print c
np.savetxt('array.csv', [c], delimiter=',', fmt='%d')

