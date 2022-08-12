"""
Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
"""

list1 = [34, 54, 67, 89, 11, 43, 94]

x = list1.pop(4)
list1.insert(2, x)
list1.append(x)
print(list1)

