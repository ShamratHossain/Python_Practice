"""
This is a function called calculate_area that takes base and height as an input and returns and area of a triangle.
Equation of an area of a triangle is, area = (1/2)*base*height
"""

def calculate_area(base,height):
    area = (1/2) * base * height
    return area


new_base = int(input("Type the base value of your triangle: "))
new_height = int(input("Type the height value of your triangle: "))

triangel_area = calculate_area(new_base,new_height)

print("The area of your triangel is ", triangel_area)