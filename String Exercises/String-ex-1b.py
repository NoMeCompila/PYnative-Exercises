"""
Write a program to create a new string made of the middle three characters of an input string.
"""


str1 = "JhonDipPeta"

size = len(str1)

mid = str1[int(size/2) - 1] + str1[int(size/2)] + str1[int(size/2) + 1]

str2 = mid

print(str2)