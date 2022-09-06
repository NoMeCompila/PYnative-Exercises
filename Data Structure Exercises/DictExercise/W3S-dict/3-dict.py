"""
Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
import pprint

dic1={1: 10, 2: 20}
dic2={3: 30, 4: 40}
dic3={5: 50, 6: 60}

# concatenate

# d4 = dic1 | dic2 | dic3

# otra forma
d4 = dict()
d4.update(dic1)
d4.update(dic2)
d4.update(dic3)
pprint.pprint(d4)