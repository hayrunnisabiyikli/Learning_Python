"""Write a program that asks for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same.
(The area of a rectangle is the rectangle’s length times its width.)"""

# Get length and width of rectangle 1 from user
length1 = float(input("Enter length of rectangle 1: "))
width1 = float(input("Enter width of rectangle 1: "))

# Get length and width of rectangle 2 from user
length2 = float(input("Enter length of rectangle 2: "))
width2 = float(input("Enter width of rectangle 2: "))
# It can also be a given decimal number, so I encoded it in float type.

# Calculate areas of both rectangles
area1 = length1 * width1
area2 = length2 * width2

# Compare areas and display result
if area1 > area2:
    print("Rectangle 1 has a greater area.")
elif area2 > area1:
    print("Rectangle 2 has a greater area.")
else:
    print("Both rectangles have the same area.")
