"""
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""

s = "pynative"

for i in s:
    if s.index(i) % 2 == 0:
        print(i)

