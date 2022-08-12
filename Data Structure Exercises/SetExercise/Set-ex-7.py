"""
Check if two sets have any elements in common. If yes, display the common elements
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

Expected output:

Two sets have items in common
{10}
"""


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

s3 = set1 & set2

print(s3)