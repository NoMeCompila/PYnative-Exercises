import json

data = {"key1" : "value1", "key2" : "value2"}

json_data = json.dumps(data, indent = 4)

print(json_data)
