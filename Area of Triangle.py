"""
This is a function called calculate_area that takes base and height as an input and returns and area of a triangle.
Equation of an area of a triangle is, area = (1/2)*base*height
It can be either "triangle" or "rectangle".
Based on shape type it will calculate area.
Equation of rectangle's area is, rectangle area=length*width
"""

def calculate_area(base, height, shape = 'triangle'):
    if shape== 'triangle':
        area = (1/2) * base * height
        return area
    elif shape == 'rectangle':
        area = base * height
        return area


shape = input("What is the shape you want to calculate('triangle' or 'rectangle'): ")
new_base = int(input("Type the base/width value of your shape: "))
new_height = int(input("Type the height/length value of your shape: "))

shape_area = calculate_area(new_base, new_height, shape)

print("The area of your shape is ", shape_area)