import math
side1 = int(input("Enter 1st sides of the triangle: "))
side2 = int(input("Enter 2nd sides of the triangle: "))
side3 = int(input("Enter 3rd sides of the triangle: "))
p = (side1 + side2 + side3)//2
ans = math.sqrt(p*(p-side1)*(p-side2)*(p-side3))
print(ans)
