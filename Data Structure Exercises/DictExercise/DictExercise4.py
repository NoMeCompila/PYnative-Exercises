"""
Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

Expected output:
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
"""

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


d1 = dict.fromkeys(employees, defaults)

print(d1)