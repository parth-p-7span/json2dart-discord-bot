from class_generator import Generator
import json

data = '''
{
    "name":"parth",
    "profile":{
        "surname":"panchal",
        "age":21,
        "job":{
            "title":"developer",
            "company":{
                "name":"7Span",
                "area":{
                    "name": "sola",
                    "pin": 380060
                },
                "skills":[
                    {"id":1, "name":"flutter"},
                    {"id":2, "name":"python"}
                ]
            }
        }
    }
}
'''

data = json.loads(data)

temp = []


def checkData(d, parent):
    temp = []
    for k, v in d.items():
        if isinstance(v, dict):
            temp.append(parent)
            checkData(v, parent + '-' + k)
        elif isinstance(v, list):
            if isinstance(v[0], dict):
                temp.append(parent + '-' + k)


checkData(data, '')

file = open('temp.dart', mode='w')

for i in temp:
    loc = i.split('-')
    loc.remove('')
    print(loc)
    temp_data = data
    for k in loc:
        temp_data = temp_data[k]
    if not loc:
        temp_generator = Generator("DartClass", temp_data)
        file.write(temp_generator.create_class() + "\n\n")
    else:
        if isinstance(temp_data, list):
            temp_generator = Generator(loc[-1].capitalize(), temp_data[0])
            file.write(temp_generator.create_class() + "\n\n")
        else:
            temp_generator = Generator(loc[-1].capitalize(), temp_data)
            file.write(temp_generator.create_class() + "\n\n")

file.close()
