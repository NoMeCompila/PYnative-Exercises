"""
20. Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

d1 = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
    {"VIII": "S007"}
]


lis = set(i for j in d1
     for i in j.values())

print(lis)
