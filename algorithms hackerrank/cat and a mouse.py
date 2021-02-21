def catAndMouse(x,y,z):
    if(abs(x-z) < abs(y-z)):
        print("Cat A")
    elif(abs(x-z) > abs(y-z)):
        print("Cat B")
    else:
        print("Mouse C")
q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    catAndMouse(x,y,z)
