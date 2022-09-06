def fibo(x):
    """
    :param x:
    :return:
    """
    if x < 0:
        return "Enter a positive number"
    if x < 2:
        return x
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(8))
