def minimumSwaps(s):
    count1=0
    for i in range(len(s)):
        if(i%2==0 and s[i]=="R"):
            count1+=1
        if(i%2==1 and s[i]=="S"):
            count1+=1
    count2=0
    for i in range(len(s)):
        if(i%2==0 and s[i]=="S"):
            count2+=1
        if(i%2==1 and s[i]=="R"):
            count2+=1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    status = input()

    result = minimumSwaps(status)
