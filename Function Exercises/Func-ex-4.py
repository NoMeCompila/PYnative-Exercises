"""
Create a function with a default argument
Write a program to create a function show_employee() using the following conditions.

It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary
"""


def employee_data(name, salary=90000):
    return f"name: {name} - salary: {salary}"


print(employee_data("Fernando", 200000))

print(employee_data("Antonio"))