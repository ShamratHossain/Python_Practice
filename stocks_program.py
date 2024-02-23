"""
You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price.
If stock already exist in your list (like info, ril etc) then it will append the price to the list.
Otherwise it will create new entry in your dictionary.
 For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
"""


stocks = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}
user_input = input("What operation you would like to do(print, add):")
if user_input == "print":
    for key in stocks:
        avg = 0
        for item in stocks[key]:
            avg = avg + item
        print(key, "==>", stocks[key], "==>", round(avg/len(stocks[key]), 2))


elif user_input == "add":
    new_stock = input("name of your stock: ")
    i = 0
    for key in stocks:
        i = i + 1
        print(i)
        print(len(stocks))
        if new_stock == key:
            price = int(input("price of your stock: "))
            stocks[key].append(price)
            print(stocks)
            break
        elif new_stock != key and i == len(stocks):
            stocks[new_stock] = []
            new_stock_price = int(input("price of your stock: "))
            stocks[new_stock].append(new_stock_price)
            print(stocks)
            break