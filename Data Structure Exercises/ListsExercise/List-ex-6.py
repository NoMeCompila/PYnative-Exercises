"""
 Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
"""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

l2 = list(filter(lambda x: x != "", list1))

print(l2)