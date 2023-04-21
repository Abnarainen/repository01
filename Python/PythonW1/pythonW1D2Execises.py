# Exercise 1 : Hello World
# print Hellow World 4 times

# for x in range(5):
#     print("Hello World")

# -----------------------------------

# Exercise 2 : Some Math
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

# calculation = ((99 ** 3)*8)
# print (calculation)

# ------------------------------------

# Exercise 3 : What Is The Output ?
# Predict the output of the following code snippets:
# >>> 5 < 3 / prediction: false
# >>> 3 == 3 / prediction: true
# >>> 3 == "3" / prediction: SyntaxError  comment: Because "3" is a str
# >>> "3" > 3 / prediction: SyntaxError  comment: Because "3" is a str
# >>> "Hello" == "hello" / prediction: true

# --------------------------------------

# Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

# computerBrand = "Asus VivoBook"
# print ("I have a" + computerBrand +" computer")
# or
# print(f"I have a {computerBrand} computer")

# ----------------------------------------

# 🌟 Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

# name="Abraham"
# age=19
# shoe_size= 43
# info=f"Hi! My name is {name} , I'm {age} years old and my shoes size is {shoe_size}"
# print(info)

# --------------------------------------------

# Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

# num1 = input ("Enter the frist number")
# num2 = input ("Enter the second number")
# if num1 > num2 :
#     print (f"{num1} is greater than {num2}")
# else:
#         print (f"{num2} is greater than {num1}")

# ----------------------------------------------------

# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

# num = int(input("Enter the frist number"))
# if (num % 2) == 0 :
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")

# ------------------------------------------------------------

#  Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

# guestName = input("what is your name?")
# myName = "Abraham"
# if (guestName == myName)==True:
#     print(f"We have the name {guestName} ! Welcome to you")
# else:
#     print(f"Sorry {guestName}, your access has been denied")

# ------------------------------------------------------------

# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

# userHeight=int(input("What is your size (in inch)?"))
# limitHeight = int(145/2.54)
# if userHeight > limitHeight:
#     print("you are tall enough to ride!")
# else:
#     print(f"you are {int(limitHeight*2.54)}cm! you are not tall enough to ride :(")

# ------------------------------------------------------------
