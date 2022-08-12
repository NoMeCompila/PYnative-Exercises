"""
Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Given:

s1 = "Ault"
s2 = "Kelly"

AuKellylt
"""


s1 = "Ault"
s2 = "Kelly"

size1 = len(s1)
size2 = len(s2)

mid1 = s1[int(size1/2)]
mid2 = s2[int(size2/2)]

new_string = s1[:int(size1/2)] + s2 + s1[int(size1/2):]

print(new_string)