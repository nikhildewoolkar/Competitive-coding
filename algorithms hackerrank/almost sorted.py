n = int(input())
arr = list(map(int, input().rstrip().split()))
arr1=arr.copy()
if(arr1==sorted(arr1)):
    print("yes")
else:
    
    for i in range(1,len(arr1)):
        if(arr1[i-1]>arr1[i]):
            a=i-1
            b=arr1.index(min(arr1[i-1:]))
            t=arr1[a]
            arr1[a]=arr1[b]
            arr1[b]=t
            if(arr1==sorted(arr1)):
                print("yes")
                print("swap",a+1,b+1)
                break
            else:
                x=arr[:a]
                y=arr[a:b+1]
                y.reverse()
                z=arr[b+1:]
                x.extend(y)
                x.extend(z)
                if(x==sorted(x)):
                    print("yes")
                    print("reverse",a+1,b+1)
                    break
                else:
                    print("no")
                    break
    

                
