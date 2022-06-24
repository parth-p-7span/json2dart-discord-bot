from class_generator import Generator
import json

data = r'''
{
    "plus_code": {
        "compound_code": "9W6R+2CQ Boston, MA, USA",
        "global_code": "87JC9W6R+2CQ"
    },
    "results": [
        {
            "address_components": [
                {
                    "long_name": "2",
                    "short_name": "2",
                    "types": [
                        "street_number"
                    ]
                },
                {
                    "long_name": "City Hall Square",
                    "short_name": "City Hall Square",
                    "types": [
                        "route"
                    ]
                },
                {
                    "long_name": "02203",
                    "short_name": "02203",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "2 City Hall Square, Boston, MA 02203, USA",
            "geometry": {
                "location": {
                    "lat": 42.3600757,
                    "lng": -71.05893929999999
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 42.36142468029149,
                        "lng": -71.05759031970848
                    },
                    "southwest": {
                        "lat": 42.35872671970849,
                        "lng": -71.0602882802915
                    }
                }
            },
            "place_id": "ChIJh3uUAd5x44kRUbQ9liy0tLU",
            "plus_code": {
                "compound_code": "9W6R+2C Boston, MA, USA",
                "global_code": "87JC9W6R+2C"
            },
            "types": [
                "street_address"
            ]
        }
    ],
    "status": "OK"
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
                checkData(v[0], parent + '-' + k)


checkData(data, '')

# print(temp)

file = open('temp.dart', mode='w')

temp_generator = Generator("DartClass", data)
file.write(temp_generator.create_class() + "\n\n")

for i in temp:
    loc = i.split('-')
    loc.remove('')
    print(loc)
    temp_data = data
    for k in loc:
        if isinstance(temp_data, list):
            temp_data = temp_data[0][k]
        else:
            temp_data = temp_data[k]
    if isinstance(temp_data, list):
        temp_generator = Generator(loc[-1].capitalize(), temp_data[0])
        file.write(temp_generator.create_class() + "\n\n")
    else:
        temp_generator = Generator(loc[-1].capitalize(), temp_data)
        file.write(temp_generator.create_class() + "\n\n")

file.close()
