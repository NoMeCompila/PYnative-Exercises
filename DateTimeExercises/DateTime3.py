"""
Subtract a week (7 days)  from a given date in Python
given_date = datetime(2020, 2, 25)
Expected output:
2020-02-18
"""


from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print(f"original = {given_date}")

one_week_ago = given_date - timedelta(days=7)
print(f"one week ago = {one_week_ago}")


