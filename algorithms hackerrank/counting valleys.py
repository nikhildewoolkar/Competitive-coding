def countingValleys(n,s):
    c=0
    count=0
    for i in range(len(s)): 
        if(s[i]=="U"):
            c+=1
        if(s[i]=="D"):
            c-=1
        if(c==0 and s[i]=="U"):
            count+=1
    print(count)
n = int(input())
s = input()
countingValleys(n,s)
