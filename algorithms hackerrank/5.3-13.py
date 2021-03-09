class shape:
    def area(*args):
        if(len(args)==2):
            print("Area : ", args[0]*args[1])
        if(len(args)==1):
            print("Area : ", (3.14)*args[0]*args[0])
print("Area-")
print("1. Rectangle")
print("2. Circle")
task = int(input("Enter choice : "))
if(task==1):
    a = int(input("Enter Length : "))
    b = int(input("Enter WIdth : "))
    shape.area(a,b)
if(task==2):
    a = int(input("Enter Radius : "))
    shape.area(a)
