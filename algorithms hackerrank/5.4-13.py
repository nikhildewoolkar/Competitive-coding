class Family:
def show_family(self): print("This is our family: ")
class Father(Family):
fathername = input("Enter your father's name: ") def show_father(self):
print(self.fathername) class Mother(Family):
mothername = input("Enter your mother's name: ") def show_mother(self):
print(self.mothername) class Son(Father, Mother):
yourname = input("Enter your name: ") def show_parent(self):
print("My name is : ",self.yourname) print("My Father's name is : ", self.fathername)
print("My Mother's name is : ", self.mothername)

s1 = Son() s1.show_family() s1.show_parent()
