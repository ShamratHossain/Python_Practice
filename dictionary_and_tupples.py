"""
1. We have following information on countries and their population (population is in crores),

Country	Population
China	    143
India	    136
USA	        32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
i. print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21

ii. add: if user input add then it should further ask for a country name to add.
    If country already exist in our dataset then it should print that it exist and do nothing.
    If it doesn't then it asks for population and add that new country/population in our dictionary and print it
iii. remove: when user inputs remove it should ask for a country to remove.
    If country exist in our dictionary then remove it and print new dictionary using format shown above in (i).
    Else print that country doesn't exist!
iv. query: on this again ask user for which country he or she wants to query.
    When user inputs that country it will print population of that country.
"""

country_population = {'china': 143, 'india': 136, 'usa': 32, 'pakistan': 21}

user_input = input("Choose your input(print, add, remove, query): ")

if user_input == "print":
    for k,v in country_population.items():
        print(k + "==>" + str(v))
elif user_input == "add":
    new_country = input("put the name of your country: ")
    i = 0
    for key in country_population:
        i = i + 1
        if key == new_country:
            print("This country already exists")
            break
        elif key != new_country and i == 4:
            country_population[new_country] = int(input("put the population of the country: "))
            print(country_population)
            break
elif user_input == "remove":
    del_item = input("put the country you want to remove: ")
    i = 0
    for key in country_population:
        i = i + 1
        if del_item == key:
            del country_population[del_item]
            print(country_population)
            break
        elif del_item != key and i == 4:
            print("The country doesn't exist in our dictionary")

elif user_input == "query":
    query_item = input("Which country population you want to know about? ")
    i = 0
    for key in country_population:
        i = i + 1
        if query_item == key:
            print(country_population[query_item])
            break
        elif query_item != key and i == 4:
            print("This country is not available in our dictionary")