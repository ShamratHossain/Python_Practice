"""
Here is a function called print_pattern that takes integer number
as an argument and prints a pattern if input number is 3,
"""


def print_pattern(num = 5):
    for i in range(num):
        s = ''
        for j in range(i + 1):
            s = s + '*'

        print(s)


print_pattern(10)