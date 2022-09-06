'''
verificar si una palabra es palindroma
kayak
deified
'''


def is_palindrome(word):
    w = word[::-1]
    if w == word:
        return True
    else:
        return False

x = "kayak"
print(is_palindrome(x))
y = "Fernando"
print(is_palindrome(y))