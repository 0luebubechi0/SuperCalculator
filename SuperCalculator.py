#The goal of this program is to create a calculater to calculate the area of a Triangle

#Area of a Triangle = base * height/2

#Area of a Rectangle = length * width

#Area of a Circle = Pi * Radius * Radius

print("Hello, welcome to my super calculator program")

print("Enter number 1 to calculate the area of a triangle")

print("Enter number 2 to calculate the area of a rectangle")

print("Enter number 3 to calculate the area of a circle")

choice = input("enter your choice")


if choice == "1":
    base = eval(input("enter a base "))
    height = eval(input("enter a height "))
    areaofatriangle = base * height/2
    print("the area of a triangle with base of ", base, "and height of " ,height," is",areaofatriangle)
elif choice == "2":
    length = eval(input("enter a length "))
    width = eval(input("enter a width "))
    areaofarectangle = length * width
    print("the area of a rectangle with a length of ", length, "and the width of ",width," is",areaofarectangle)
elif choice == "3":
    PI = 3.14159
    radius = eval(input("enter a radius "))
    areaofacircle = PI * radius * radius
    print("the area of a circle with a radius of ", radius,"is",areaofacircle)
