import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2

json_data = json.loads(sampleJson)

print(json_data["key2"])

# reqres example data

reqres_data = '''
    
    {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        }
    ]
}
'''
json_reqres = json.loads(reqres_data)

print(json_reqres['page'])

print(json_reqres['data'][0]['first_name'])