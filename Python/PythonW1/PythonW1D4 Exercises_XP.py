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
