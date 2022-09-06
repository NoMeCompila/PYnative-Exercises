import pprint

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]



# get all python devs
python_devs = [i['name'] for i in DATA if i['language'] == 'python']
print(python_devs)


python_devs = list(filter(lambda x: x['language'] == 'python', DATA))
name_python_devs = list(map(lambda x: x['name'], python_devs))
pprint.pprint(python_devs)
print(name_python_devs)


# Get all Platzi devs
platzi_devs = [i['name'] for i in DATA if i['organization'] == 'Platzi']
print(platzi_devs)
platzi_devs = list(filter(lambda x: x['organization'] == 'Platzi', DATA))
name_platzi_devs = list(map(lambda x: x['name'], platzi_devs))
print(name_platzi_devs)


# Get all adults
adults = list(filter(lambda x: x['age'] >= 18, DATA))
print(adults)
adults_name = list(map(lambda x: x['name'], adults))
print(adults_name)

adults = [i['name'] for i in DATA if i['age'] >= 18]
print(adults)


# Get people older than 70 years
olders = list(map(lambda x: x | {'old': x['age'] > 70}, DATA))
pprint.pprint(olders)

old_confirmation = lambda worker_age: worker_age > 70
olders = [ i | {'old': old_confirmation(i['age'])} for i in DATA]
pprint.pprint(olders)