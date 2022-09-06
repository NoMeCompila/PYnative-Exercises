def facts(x):
    if x < 0:
        return "enter a positive number"

    if x == 1 or x == 0:
        return 1
    else:
        return x * facts(x-1)

# facts = lambda x: [1, 0][x > 1] or facts(x - 1) * x


print(facts(5))

