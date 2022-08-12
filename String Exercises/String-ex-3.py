"""
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle,
and last characters.

Given:
s1 = "America"
s2 = "Japan"

Expected Output:
AJrpan
"""


def tri_string(s):
    size = len(s)

    first = s[0]
    last = s[-1]
    mid = s[int(size / 2)]

    return first + mid + last


s1 = "America"
s2 = "Japan"

ns1 = tri_string(s1)
ns2 = tri_string(s2)

new_str = s1[0]+s2[0]+s1[1]+s2[1]+s1[2]+s2[2]

print(new_str)

