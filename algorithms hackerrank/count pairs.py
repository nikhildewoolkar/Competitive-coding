count=0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10):
                    count+=1
print(count/)
"""def magic(n): 
    if (n == 0): 
        return False
    if(n == 1):
        return True
    else:
        while (n != 1): 
                if (n % 2 != 0): 
                    return False
                n = n // 2
        return True
def countPairs(arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            n=int(arr[i]&arr[j])
            if(magic(n)):
                count+=1
    return count
arr_count = int(input().strip())
arr = []
for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)
result = countPairs(arr)
print(result)
"""
