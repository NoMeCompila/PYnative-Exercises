"""
To access a range of items in a list, use the slicing operator :. With this operator, you can specify where to start the
 slicing, end, and specify the step.

For example, the expression list1[ start : stop : step] returns the portion of the list from index start to index stop,
at a step size step.

for 1st list: Start from the 1st index with step value 2 so it will pick elements present at index 1, 3, 5, and so on
for 2nd list: Start from the 0th index with step value 2 so it will pick elements present at index 0, 2, 4, and so on
"""


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


def get_odd_even_index(list1, list2):
    l3 = list1[1::2]
    l4 = list2[0::2]
    return l3 + l4


print(get_odd_even_index(l1, l2))
