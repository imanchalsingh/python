#Calculate the area of triangle.(1/2*base*hight)
side1 = input("Enter your triangle's base for find triangle's area: ")
side2 = input("Enter your triangle's hight for find triangle's area: ")
triangle_area = int(side1) * int(side2) * 1/2
print("It's area of tringle:" ,triangle_area)

if triangle_area == 0:
    print("Invalid!")
else:
    print("Thanks for using.\n")


#Calculate the area of square.(side^2)
side = input("Enter your side for find square's area: ")
square_area = int(side) * int(side)
print("It's area of square:" ,square_area)

if square_area == 0:
    print("Invalid!")
else:
    print("Thanks for using.\n")


#Calculate the area of circle.(pi*(radius)^2)
radius = input("Enter your circle's radius for find circle's area: ")
pi = 3.14
radius_area = float(radius) * float(radius) * float(pi)
print("it's area of circle:" ,radius_area)

if radius_area == 0:
    print("Invalid!")
else:
    print("Thank you.")


#Calculate the area of cube.(4 * (side)^2)
side3 = input("Enter your cube's side for find cube's area: ")
cube_area = 4 * int(side3) * int(side3)
print("It's area of cube:" ,cube_area)

if cube_area == 0:
    print("Invalid!")
else:
    print("Thanks for using.")


#Calculate the perimeter of circle.(2*pi*radius)
radius1 = input("Enter your circle's radius fo find circle's perimeter: ")
pi = 3.14
circle_perimeter = float(2) * float(pi) * float(radius1)
print("It's circle's perimeter:" ,circle_perimeter)

if circle_perimeter == 0:
    print("Invalid!")
else:
    print("Thank you.")

