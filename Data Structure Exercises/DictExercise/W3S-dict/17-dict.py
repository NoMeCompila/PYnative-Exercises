"""
Write a Python program to remove duplicates from Dictionary.
"""

student_data = {
    'id1': {'name': ['Sara'],  'class': ['V'],  'subject_integration': ['english, math, science']},
    'id2': {'name': ['David'], 'class': ['V'],  'subject_integration': ['english, math, science']},
    'id3': {'name': ['Sara'],  'class': ['V'],  'subject_integration': ['english, math, science']},
    'id4': {'name': ['Surya'], 'class': ['V'],  'subject_integration': ['english, math, science']},
}


resultado = dict()


for k, v in student_data.items():
    if v not in resultado.values():
        resultado[k] = v

print(resultado)

