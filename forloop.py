"""
1. After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads
"""

# result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]
#
# total = 0
# for item in result:
#     if item == "heads":
#         total = total + 1
#
# print(total)


"""
2. Print square of all numbers between 1 to 10 except even numbers
"""


# for i in range(1, 11):
#     if i % 2 == 1:
#         print(i*i)


"""
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should
tell you in which month that expense occurred. 
If expense is not found then it should print that as well.
"""


# expense_list = [2340, 2500, 2100, 3100, 2980]
#
# user_input = int(input("put your expense: "))
#
# for i in range(len(expense_list)):
#     if user_input == expense_list[i]:
#         print("Month:", i+1)
#         break
#     elif i == len(expense_list)-1:
#         print("expense not found")


"""
Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
"""

# for i in range(5):
#     print("You have completed " + str(i+1) + " km")
#     if i == 4:
#         print("Congratulation!!! you have completed the Race")
#         break
#     user_answer = input("are you tired? ")
#     if user_answer == "yes":
#         print("Sorry! you haven't completed the Race")
#         break
#     elif user_answer == "no":
#         continue


"""
Write a program that prints following shape
*
**
***
****
"""

for i in range(4):
    s = ''
    for j in range(i+1):
        s = s + "*"
    print(s)
