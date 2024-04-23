import json

data = {
    "first_name": "John",
    "last_name": "Dou",
    "age": 25,
    "email": "johnDou@gmail.com"
}

data_json = json.dumps(data)
print(type(data_json))
print(data_json)

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
    print(type(data))
    print(data)
