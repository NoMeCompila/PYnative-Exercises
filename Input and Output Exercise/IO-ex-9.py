"""
Check file is empty or not
Write a program to check if the given file is empty or not
"""

import os


def is_empty_file(file_name: str) -> bool:
    """
    :param file_name: name of the file to check
    :return: bool if the file is empty return true else returns false
    """
    line = os.stat(file_name).st_size
    return True if line == 0 else False


file = 'text_ex.txt'

if is_empty_file(file):
    print(f"'{file}' file is empty ")
else:
    print(f"'{file}' file is not empty ")