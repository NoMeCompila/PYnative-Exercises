"""
Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
"""

import random

l1 = []

for i in range(100):
    l1.append(random.randrange(1000000000, 9999999999))

win = random.sample(l1, 2)

print(win)

