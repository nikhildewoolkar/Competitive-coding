

def solution(f):
    r=f.count("N")+2
    c=f.count("W")+f.count("E")+4
    a = [[0 for i in range(c)] for j in range(r)]
    r=r-1
    c=c-f.count("E")-1
    a[r][c]=1
    for i in range(0,len(f)):
        if(f[i]=="E"):
            a[r][c+1]=1
            c=c+1
        if(f[i]=="W"):
            a[r][c-1]=1
            c=c-1
        if(f[i]=="S"):
            a[r+1][c]=1
            r=r+1
        if(f[i]=="N"):
            a[r-1][c]=1
            r=r-1
    for i in a:
        print(i)
f="NENENWWWWN"
solution(f)
