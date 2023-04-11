# Exercise 1 : Set

# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# --> Solution:
# my_fav_numbers = {3,6,7}
# my_fav_numbers.add(10)
# my_fav_numbers.add(14)
# my_fav_numbers.remove(14)

# friend_fav_numbers = {12,13,15,17,18}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# --------------------------------------------------------

# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# --> Solution: Non

# ----------------------------------------------------

# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# --> Solution:

# My_list = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(f'My original list contains the followings: {My_list}')

# Modified_list = My_list.copy()
# Modified_list.remove("Banana")
# Modified_list.remove("Blueberries")
# Modified_list.append("Kiwi")
# Modified_list.insert(0,"Apples")
# Item_in_my_list = len(Modified_list)

# print(f'My new list contains the followings: {Modified_list}')
# print(f'There is a total of {Item_in_my_list} items in my new list')

# Modified_list.clear()
# print(f'My list contains now the followings: {Modified_list}, it is therefore empty')

# ----------------------------------------------------

# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

#--> Solution1:
# An integer is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place. 

# my_list = list()
# Current_number = 1.5

# while Current_number <=5:
#     if Current_number.is_integer():
#         my_list.append(int(Current_number))
#     else:
#         my_list.append(Current_number)
#     Current_number += 0.5
# print(my_list)

#--> Solution2:
# new_list = [ Current_number/2 for Current_number in range (3, 11)]
# my_list.append(int(Current_number)) if Current_number.is_integer() else my_list.append(Current_number)

# new_list = [ int(Current_number / 2)  if (Current_number / 2).is_integer() else Current_number /2 for Current_number in range (3, 11)]
# print(new_list)

#--> Solution3:

# my_list1 = [1.5,2.5,3.5,4.5]
# my_list2 = [2,3,4,5]

# my_list3 = my_list1 + my_list2
# my_list3.sort()

# print(my_list3)

# ----------------------------------------------------

# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

#--> Solution:
# for a in range (1,21):
#     print (a)

#     if (a%2) == 0:
#         print (f'index {a} is an even number')

# ----------------------------------------------------

# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

#--> Solution:
# equal_name = "Abraham"
# while True:

#     user_name = input ('What is your name?')
#     if user_name == equal_name:
#         print(f"That's awesome {user_name} , we have the same name! You're welcome")

#         break
#     else: 
#         print (F"Sorry {user_name}, we do not have the same name :/ ")        

# ------------------------------------------------------

# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

#--> Solution:
# User_info = [input("What is the name of your favorite fruit(s) (one or several fruits)? ")]
# query_input = input("Input the name of any fruit ")

# if query_input in User_info:
#     print(f"You chose {query_input} which is one of my favorite fruits! Enjoy it!")
# else:
#     print(f"You chose a {query_input}, this is a new fruit. I hope you enjoy.")

# ------------------------------------------------------

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

#--> Solution:
# my_list = list()
# question1 = input("Hello and Welcome to Mauritius Pizza! Do you want to order? (yes/quit)")
# if question1 == "yes":
#     while True : 
#         toppings = input("Enter your toppings (Enter quit to exit)")
#         if toppings == "quit":
#             break
#         else:
#             my_list.append(toppings)        
#             print ("We will add that toppings to your pizza!")
#             question2 = input("Do you want to add more toppings? (yes/quit) ")
#             if question2 == "quit":
#                 break

#     print(f"Thank you for ordering at Mauritius Pizza! Here is your order --> {', '.join(my_list)}")
# else:
#     print("Thank you! Goodbye")

# ------------------------------------------------------
# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

#--> Solution for age:

# question1 = int(input("Welcome to Cinemax! Indicate how many seats are you booking?"))
# total_cost = 0

# for persons in range(question1) :
#     client_age = int(input("What is the age of person {}?".format(persons+1)))
#     if client_age < 3:
#         total_cost += 0
#     elif client_age in range (3,13):
#         total_cost +=  10
#     elif client_age > 12:
#         total_cost += 15

# print(f"The total cost is {total_cost} ")

#--> Solution for teenagers:
# client_name = ["Abraham", "Martine", "Schon", "Anaelle", "John"]
# allowed_customer = []

# for client in client_name:
#     client_age = int(input("What is your age {}? ".format(client)))
#     if 16 <= client_age >= 21 :
#         allowed_customer.append(client)
# print(allowed_customer)

# ------------------------------------------------------

# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

#--> Solution:

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches = list()

# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich_orders)
#     print(f'I have made your {sandwich}')

# ------------------------------------------------------

# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to 
# remove all occurrences of ‘pastrami’ from sandwich_orders.Make sure no pastrami sandwiches end up in finished_sandwiches.

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich",  "Pastrami sandwich",  "Pastrami sandwich"]
# finished_sandwiches = []

# print("Sandwich orders are: ")

# for i, sandwich in enumerate (sandwich_orders):
#     print(f'{i + 1}. {sandwich}')


# print("Sandwich making: ")
# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")
#     print('Sorry, we run out of Pastrami for your sandwich')

# print("Here is your final order: ")
# for i, order in enumerate(sandwich_orders):
#     finished_sandwiches.append(sandwich_orders)
#     print (f'{i+1}.{order}')

# ------------------------------------------------------
