data = dict()
data["name"] ="Jane"
data["surname"] = "Doe"
data ["hobbies"] = ["running", "sky diving", "singing"]
data ["age"] = 35
data ["children"] = [
    {
        "name": "Alice",
        "age": 6
        },
        {
        "name": "Bob",
        "age": 8
        }
    ]
child = "Rob"

if child in data["children"][0]["name"] or child in data["children"][1]["name"]:
    print('Имя, ', child, ' есть в спсике.')
else:
    print('Noname')

