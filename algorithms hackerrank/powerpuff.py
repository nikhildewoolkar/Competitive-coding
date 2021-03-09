arr3=[]
arr4=[]
arr5=[]
n = int(input())
arr1 = input().split(" ")
for i in range(len(arr1)):
    t = int(arr1[i])
    arr3.append(t)
del arr1[:]
arr2 = input().split(" ")
for i in range(len(arr2)):
    t = int(arr2[i])
    arr4.append(t)
del arr2[:]
print(n)
print(arr3)
print(arr4)
print(arr1)
print(arr2)
for i in range(n):
    arr5[i]=arr4[i]/arr3[i]
print(arr5)
arr5.sort()
print(arr5[:1]) 

