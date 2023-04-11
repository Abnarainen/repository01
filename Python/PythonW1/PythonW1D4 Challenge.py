# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

# --> Solution:

# user_number = int(input("Please enter a number "))
# user_length = int(input("Please enter your length "))
# calculation = []
# i = 1

# while len(calculation) < user_length:
#     calculation.append(user_number * i)
#     i += 1

# print(calculation)

# ---------------------------------------------------------------------

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

# --> Solution:

# user_info = input("Please enter a word with duplications ")
# transformation = " "
# for i in range(len(user_info)):
#     if i == 0 or user_info[i] != user_info[i-1]:
#         transformation += user_info[i]

# print ("User info without duplicates strings", transformation)