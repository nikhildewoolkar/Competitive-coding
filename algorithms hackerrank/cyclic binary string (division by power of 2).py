def h2(n):  
    return (n & (~(n - 1)))#highest power 2 divides the number
def maximumPower(s):
    u=len(s)
    if(s.count('1')==u):
        print(0)
    elif(s.count('0')==u):
        print(-1)
    elif(s.count('1')==1):
        print(u-1)
    else:
        maxi=0
        for i in range(len(s)):
            s = s[(len(s)-1):]+s[0:(len(s)-1)]
            n=int(s,2)
            maxi=max(maxi,h2(n))
        c=0
        if(maxi%2==1):
            print(0)
        else:
            while(maxi!=1):
                maxi=maxi//2
                c+=1
            print(c)
s = input()
maximumPower(s)

