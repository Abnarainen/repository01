
# Challenge 1:

# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

# Solution:

# User = str(input("Enter a word! "))
# Dictionary = {}

# for i, word in enumerate(User):
#     if word in Dictionary:
#         Dictionary[word].append(i)
#     else:
#         Dictionary[word] = [i]

# for word, _ in Dictionary.items():
#     print(f"{word}:{_}")
# -----------------------------------------------------------------------

# Challenge 2:

# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.


# Solution:

# items_to_purchase = {
#   "Water": 1,
#   "Bread": 3,
#   "TV": 1000,
#   "Fertilizer": 20,
# }

# items_to_purchase = {
#   "Apple": 4,
#   "Honey": 3,
#   "Fan": 14,
#   "Bananas": 4,
#   "Pan": 100,
#   "Spoon": 2
# }

# items_to_purchase = {
#   "Phone": 999,
#   "Speakers": 300,
#   "Laptop": 5000,
#   "PC": 1200
# }

# wallet = 100
# # comment: wallet_amount = int(wallet.strip("$").replace(",", ""))  # Convert wallet amount to an integer
# items_purchased = []

# for item, price in items_to_purchase.items():
#     if price <= wallet:
#         items_purchased.append(item)
#         wallet -= price

# if len(items_purchased) == 0:
#     print("Nothing is affordable")
#     print(f"Money left in wallet is $ {wallet}")
# else:
#     print(sorted(items_purchased))
#     print(f"Money left in wallet is $ {wallet}")
