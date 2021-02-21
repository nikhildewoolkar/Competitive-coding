string1=input()
string2=input()
o=int(input())
answer = ""
len1, len2 = len(string1), len(string2)
for i in range(len1):
    match = ""
    for j in range(len2):
        if (i + j < len1 and string1[i + j] == string2[j]):
            match += string2[j]
        else:
            if (len(match) > len(answer)):
                answer = match
print(answer)
b=len(answer)-1
print(b)
ans=(len1-b)+(len2-b)
if(ans<=o):
    print("Yes")
else:
    print("No")
