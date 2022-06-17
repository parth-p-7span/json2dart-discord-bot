from class_generator import Generator
import json

data = '''{
    "class_name": "Person",
    "name": "parth",
    "age": 21,
    "members": [
        {"id": 1, "name": "a"},
        {"id": 1, "name": "a"},
        {"id": 1, "name": "a"}
    ]
}'''

j_data = json.loads(data)
print(j_data)

# final_string = ""
#
# generator = Generator("Person", data)
#
# final_string += generator.create_class() + "\n\n"
#
# for key, value in data.items():
#     if type(value) == dict:
#         temp_generator = Generator(key.capitalize(), value)
#         final_string += temp_generator.create_class() + "\n\n"
#     elif type(value) == list:
#         dtype = type(value[0])
#         if dtype == dict:
#             temp_generator = Generator(key.capitalize(), value[0])
#             final_string += temp_generator.create_class() + "\n\n"
#
# print(final_string)
