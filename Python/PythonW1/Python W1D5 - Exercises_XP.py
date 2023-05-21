# Exercise 1:
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Solution:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Dictionary = dict(zip(keys,values))

# print(Dictionary)

# ----------------------------------------------------------------
# Exercise 2:
# 1. A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# 2. Given the following object:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# 3. How much does each family member have to pay ?

# 4. Print out the family’s total cost for the movies.
# 5. Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# Solution1:
# numberofuser = int(input("Please enter the number of persons? "))
# Clients = []
# Clientage = []
# for i in (range(numberofuser)):
#     name= input(f"What is the name of person {i + 1}? ")
#     Clients.append(name)
#     age= int(input(f"How old is {name}? "))
#     Clientage.append(age)

# dictionary = dict(zip(Clients, Clientage))

# cost = []
# for person, age in dictionary.items():

#     if age < 3:
#         print(f"The ticket for {person} is free")
#         cost.append(0)
#     elif age > 2 and age < 13:
#         print(f"The ticket for {person} is $10")
#         cost.append(10)
#     elif age > 12:
#         print(f"The ticket for {person} is $15")
#         cost.append(15)

# totalPrice = sum(cost)
# print(f"The total price is $ {totalPrice}")

# Solution2:
# numberofuser = int(input("Please enter the number of family members: "))
# family = {}

# for i in range(numberofuser):
#     name = input(f"What is the name of family member {i + 1}? ")
#     age = int(input(f"How old is {name}? "))
#     family[name] = age

# cost = []
# for person, age in family.items():
#     if age < 3:
#         print(f"The ticket for {person} is free")
#         cost.append(0)
#     elif age >= 3 and age <= 12:
#         print(f"The ticket for {person} is $10")
#         cost.append(10)
#     else:
#         print(f"The ticket for {person} is $15")
#         cost.append(15)

# totalPrice = sum(cost)
# print(f"The total cost for the movies is $ {totalPrice}")

# ----------------------------------------------------------------
# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:]

# Brand = {
# 'name': 'Zara',
# 'creation_date': 1975,
# 'creator_name': 'Amancio Ortega Gaona',
# 'type_of_clothes': ['men', 'women', 'children', 'home'],
# 'international_competitors': ['Gap', 'H&M', 'Benetton'],
# 'number_stores': 7000,
# 'major_color': {
#     'France': 'blue', 
#     'Spain' : 'red', 
#     'US' : ['pink', 'green']
# }
# }

# Solution: 
# Brand['number_stores'] = 2
# clients = ', '.join(Brand['type_of_clothes'])
# print(f"Zara's clients are {clients}.")
# Brand['country_creation'] = 'Spain'
# if 'international_competitors' in Brand:
#     Brand['international_competitors'].append('Desigual')
# Brand.pop('creation_date')
# print(Brand['international_competitors'][-1])
# print(f"The Major color clothes in the US for {Brand['name']} is {Brand['major_color']['US']}")
# print(len(Brand))
# print(Brand.keys())

# more_on_zara = {
# 'creation_date': 1975,
# 'number_stores': 10000,
# }
# Brand.update(more_on_zara)
# print(Brand)

# print(Brand['number_stores']) --> "The number of store has been updated"

# ----------------------------------------------------------------
# Exercise 4 : Disney Characters

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# 1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# 3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

# Solution: 

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# dictionary = {}

# for i, user in enumerate(users):
#     dictionary[user] = i
# print(dictionary)

# for i, user in enumerate(users):
#     dictionary[i] = user
# print(dictionary)

# x = sorted(users)
# for i, user in enumerate(x):
#     dictionary[user] = i
# print(dictionary)

# for i, user in enumerate(users):
#     if 'i' in user:
#         dictionary[user] = i 
# print(dictionary)

# for i, user in enumerate(users):
#     if 'm' in user.lower() or 'p' in user.lower():
#         dictionary[user] = i 
# print(dictionary)

