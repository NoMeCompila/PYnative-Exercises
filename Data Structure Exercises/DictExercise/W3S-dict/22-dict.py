"""
Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
"""

my_dict = {5: 500, 1: 5874, 3: 560, 4: 400, 6: 5874, 0: 20}

d1 = dict((sorted(my_dict.items(), key=lambda x:x[1], reverse=True))[:3])

print(d1)

"""print("the 3 highest are: ", end="")
for i in range(3):
    print(l1[i], end=" ")
"""
