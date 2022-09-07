"""
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

# My solution


def pow_dict(n):
    return {x: x*x for x in range(1, n+1)}


n = 5
d1 = pow_dict(n)

print(d1)


"""
W3 solution

n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 
"""