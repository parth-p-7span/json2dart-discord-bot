from class_generator import Generator
import json

# data = '''
# {
#     "name":"parth",
#     "profile":{
#         "surname":"panchal",
#         "age":21,
#         "job":{
#             "title":"developer",
#             "company":{
#                 "name":"7Span",
#                 "area":{
#                     "name": "sola",
#                     "pin": 380060
#                 },
#                 "skills":[
#                     {"id":1, "name":"flutter"},
#                     {"id":2, "name":"python"}
#                 ]
#             }
#         }
#     }
# }
# '''

data = r'''

{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
'''

data = json.loads(data)

temp = []


def checkData(d, parent):
    for k, v in d.items():
        if isinstance(v, dict):
            temp.append(parent + '-' + k)
            checkData(v, parent + '-' + k)
        elif isinstance(v, list):
            if isinstance(v[0], dict):
                temp.append(parent + '-' + k)


checkData(data, '')

print(temp)

file = open('temp.dart', mode='w')

temp_generator = Generator("DartClass", data)
file.write(temp_generator.create_class() + "\n\n")

for i in temp:
    loc = i.split('-')
    loc.remove('')
    print(loc)
    temp_data = data
    for k in loc:
        temp_data = temp_data[k]
    if isinstance(temp_data, list):
        temp_generator = Generator(loc[-1].capitalize(), temp_data[0])
        file.write(temp_generator.create_class() + "\n\n")
    else:
        temp_generator = Generator(loc[-1].capitalize(), temp_data)
        file.write(temp_generator.create_class() + "\n\n")

file.close()
