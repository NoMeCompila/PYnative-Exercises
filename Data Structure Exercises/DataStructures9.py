"""
Get all values from the dictionary and add them to a list but don’t add duplicates
Given:

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
Expected Outcome:

[47, 52, 44, 53, 54]
"""


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}


speed_val = speed.values()

list_speed = list(speed_val)

set_speed = set(list_speed)

result = list(set_speed)

print(result)