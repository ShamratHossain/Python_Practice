"""
Write circle_calc() function that takes radius of a circle as an input from user and
then it calculates and returns area, circumference and diameter.
You should get these values in your main program by calling circle_calc function and then print them
"""

import math


def circle_calc():
    radius = float(input("Radius of your circle: "))
    area_of_circle = math.pi * radius * radius
    circumference_of_circle = 2 * math.pi * radius
    diameter_of_circle = 2 * radius
    return round(area_of_circle, 2), round(circumference_of_circle, 2), round(diameter_of_circle, 2)


my_circle = circle_calc()
print("Area of Circle is: ", my_circle[0])
print("Circumference of Circle is: ", my_circle[1])
print("Diameter of Circle is:", my_circle[2])
