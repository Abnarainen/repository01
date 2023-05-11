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
#     print("the" + x + "is" + y)

# Solution2:

# for zafr in my_books.keys():
#     print("The "+zafr+ " " +"is "+my_books[zafr])

# -----------------------------------------------------------------------------

# list1 = [1,2,3]
# list2 = ['a','b','c']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

# new_list = list1 + list2 + list3
# print(new_list)
