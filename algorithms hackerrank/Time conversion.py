b=[]
g=input()
for i in range(0,len(g)-2):
    t = g[i]
    b.append(t)
x=''.join(b)
del b[:]
for i in range(len(g)-2,len(g)):
    t=g[i]
    b.append(t)
y=''.join(b)
del b[:]
a = list(map(int,x.split(":")))
if(y=="pm" or y=="PM"):
    c=str(a[0]+12)
else:
    if a[0]>=12:
        c="0"+str(a[0]-12)
    else:
        c="0"+str(a[0])
for i in range(2,len(x)):
    t = x[i]
    b.append(t)
x=''.join(b)
d=c+x
print(d)



