"""
Write a program to create a new string made of an input string’s first, middle, and last character.
Given:
str1 = "James"
Expected Output:
Jms
"""

str1 = "James"

size = len(str1)

first = str1[0]

last = str1[-1]

mid = str1[int(size/2)]

str2 = first + mid + last

print(str2)