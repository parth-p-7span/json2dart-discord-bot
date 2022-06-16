data = {
    "name": "parth",
    "age": 21,
    "skills": [
        "python",
        ['fds', 'fasdfh'],
        3,
        {
            "dad": "hrp",
            "mom": "mhp"
        }
    ]
}

for key, value in data.items():
    if type(value) == list:
        datatype = type(value[0])

        for i in value:
            if type(i) == str:
                print("String")
            elif type(i) == int:
                print("int")
            elif type(i) == list:
                print("List")
            else:
                print(type(i))
