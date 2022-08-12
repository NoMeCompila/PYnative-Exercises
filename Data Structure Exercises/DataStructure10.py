"""
Remove duplicates from a list and create a tuple and find the minimum and maximum number
Given:

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
Expected Outcome:

unique items [87, 45, 41, 65, 99]
tuple (87, 45, 41, 65, 99)
min: 41
max: 99
"""

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]


def get_uniques(l):
    return list(set(l))


def get_tuple(l):
    return tuple(set(l))


def get_max_min(l):
    return max(l), min(l)


def execute_all(l):

    print(f"unique numbers: {get_uniques(l)}")

    print(f"tuple: {get_tuple(l)}")

    ma, mi = get_max_min(l)

    print(f"maximum: {ma}")
    print(f"minimum: {mi}")


execute_all(sample_list)