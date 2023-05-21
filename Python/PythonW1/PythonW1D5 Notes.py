# my_dog = {
#   'name': 'Rufus',
#   'age': 4,
#   'good_dog': True
# }

# print(my_dog)

# -------------------------------------------------------------------

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }


# print(sample_dict["class"]['student']['marks']['history'])

# -----------------------------------------------------------------------------

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }

# keys_to_remove = ["name", "salary"]

# Solution1 (Not good way):
   # del sample_dict ["name"]
   # del sample_dict ["salary"]
   # print(sample_dict)

# Solution2 (Dynamic):

# for keys_to_remove in keys_to_remove:
#     del sample_dict[keys_to_remove]

# print(sample_dict)

# -----------------------------------------------------------------------------
# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }

# Solution1(Best):

# for x, y in my_books.items():
#     print("The " + x + " is " + y)

# Solution2:

# for zafr in my_books.keys():
#     print("The "+zafr+ " " +"is "+my_books[zafr])

# -----------------------------------------------------------------------------


numbers = [10,20,30,40,50,60]


# Solution 1

# for i in range (len(numbers)):
#     print (f"The number at index {i} is {numbers[i]}")

# Solution 2

# for i in enumerate(numbers):
#     print(f"The number at index {i[0]} is {i[1]}")

# Solution 3

# for x,y in enumerate (numbers):
#     print (f"The number at index {x} is {y}")

# -----------------------------------------------------------------------------

# list1 = [1,2,3]
# list2 = ['a','b','c']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

# new_list = list1 + list2 + list3
# print(new_list)

# -----------------------------------------------------------------------------

# x =  0
# while x < 2:
#     print (f"x is {x}")
#     x += 1
#     print (f"x is {x}")
#     break
# print("X is bigger than 2")

# -----------------------------------------------------------------------------
# Solution 1
# my_list = list(range(0,11))
# new_list = []

# for num in my_list:
#     if num % 2 == 0:
#      new_list.append(num)
# print (new_list)

# Solution 2
# my_list = [num for num in range(0,11) if num%2 == 0]
# print (my_list)


# -----------------------------------------------------------------------------

# family_age = {'Lea': 12, 'Mark': 25, 'George': 50}

# new_year = 1

# new_family_age = {name: age+new_year for (name, age) in family_age.items()}

# print(new_family_age)

# >> {'Lea': 13, 'Mark': 26, 'George': 51}

# -----------------------------------------------------------------------------
# Solution 1
   # my_list = []

   # for i in [2, 3, 4]:
   #     for j in [100, 200, 300]:
   #         my_list.append(i*j)

   # print(my_list)

# Solution 2
   # my_list = []
   # my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]
   # print(my_list)

   # -----------------------------------------------------------------------------