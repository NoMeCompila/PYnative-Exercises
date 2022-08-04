# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.

def multi_or_sum(x: int, y: int) -> int:
    """
    returns the sum if the product is equal or lower than 1000 else return addition
    :param x: int
    :param y: int
    :return: int
    """
    return x * y if x * y <= 1000 else x + y


print(multi_or_sum(200,6))
print(multi_or_sum(200,5))