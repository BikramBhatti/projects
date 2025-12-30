import math

# this is the code for the accepting the first circle
x = int(input("Input the x coordinate for original circle:"))
y = int(input("Input the y coordinate for original circle:"))
radius = int(input("Input the radius of original circle:"))
print(f"Circle center:({x},{y}) Radius:{radius}")

#this is the code to check what position the second circle is at
def check_circle(a1, b1, x1, y1, radius1):
    radius2 = math.sqrt((x1 - a1) ** 2 + (y1 - b1) ** 2)
    if radius2 < radius1:
        print("In the Circle")
        print ("One circle may be inside the other circle but are not touching")
    elif radius2 == radius1:
        print("On the Circle")
        print("Tangent")
    else:
        print("Outside the Circle")
        print("Does not collide")

# this is the code for accepting coordinates and checking if it is in the form of (x,y)radius
cords = input("Enter Coordinates in format (x,y): ")
if len(cords) <= 5:
    cords = cords.replace("(", "").replace(")", "")  # replace ()  from input
    comma = cords.find(",")  # find index of ,
    check_circle(int(cords[:comma]), int(cords[comma+1:]), x, y, radius)  # passing new coordinates with original coordinates to function
else:
    cords = cords.replace("(", "").replace(")", "")  # replace () from input
    comma1 = cords.find(",")  # find index of ,
    check_circle(int(cords[:comma1]), int(cords[comma1+1]), x, y, int(cords[comma1+2:]))  # passing new coordinates with original coordinates to function
