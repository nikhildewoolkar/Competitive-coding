import math
s=input()
sm=s.replace(" ","")
r=math.floor(math.sqrt(len(sm)))
c=math.ceil(math.sqrt(len(sm)))
for i in range(c):
    print(sm[i::c],end=" ")

import math 
def encryption(s): 
    s=s.replace(" ","")
    d1=int(math.sqrt(len(s)))
    d2=int(math.sqrt(len(s)))+1
    g=[]
    l=0
    for i in range(d1):
        f=[]
        for i in range(d2):
            f.append(s[l])
            l+=1
        g.append(f)
    tran=list(zip(*g))
#code include    
s = input()
result = encryption(s)
