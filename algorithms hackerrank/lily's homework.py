#lily's homework
"""def lilysHomework(arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]!=t[i]):
            c=arr.index(t[i])
            arr[i],arr[c]=arr[c],arr[i]
            count+=1
            
            if(arr==t):
                break
    return count
n = int(input())
a = list(map(int, input().rstrip().split()))
s=list(reversed(a))
t=sorted(a)
result = lilysHomework(a)
result1=lilysHomework(s)
print(min(result,result1))"""
"""def lilysHomework(arr,t):
    count=0
    for i in range(len(arr)):
        if(arr[i]!=t[i]):
            c=arr.index(t[i])
            arr[i],arr[c]=arr[c],arr[i]
            count+=1
            
            if(arr==t):
                break
    return count
n = int(input())
a = list(map(int, input().rstrip().split()))
s=list(reversed(a))
r=sorted(a)
#result = lilysHomework(a)
#result1=lilysHomework(s)
print(min(lilysHomework(a,s),lilysHomework(a,r)))"""
def solution(a):

    m = {}
    for i in range(len(a)):
        m[a[i]] = i 
        
    sorted_a = sorted(a)
    ret = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret +=1
            
            ind_to_swap = m[ sorted_a[i] ]
            m[ a[i] ] = m[ sorted_a[i]]
            a[i],a[ind_to_swap] = sorted_a[i],a[i]
    return ret

input()
a = [int(i) for i in input().split(' ')]

asc=solution(list(a))
desc=solution(list(reversed(a)))
print(min(asc,desc))    
    
    
