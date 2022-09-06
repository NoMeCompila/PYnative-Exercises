"""
generar una lista con los 100 primeros numeros naturales al cuadrado
"""

squares = [i*i for i in range(101)]

print(squares)

squares_2 = [i*i for i in range(101) if i % 3 != 0]

print(squares_2)

squares_4 = [i for i in range(1, 100001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

print(squares_4)
