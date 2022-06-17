class Generator:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def __create_fields(self):
        string = ""
        for key, value in self.fields.items():
            if type(value) == str:
                string += "   String " + key + ";\n"
            elif type(value) == int:
                string += "   int " + key + ";\n"
            elif type(value) == float:
                string += "   double " + key + ";\n"
            elif type(value) == list:
                datatype = type(value[0])
                if datatype == str:
                    string += "   List<String> " + key + ";\n"
                elif datatype == int:
                    string += "   List<int> " + key + ";\n"
                elif datatype == dict:
                    string += "   List<" + key.capitalize() + "> " + key + ";\n"
            elif type(value) == dict:
                string += "   " + key.capitalize() + " " + key + ";\n"
        return string

    def __create_constructor(self):
        string = "%s({" % self.name
        for key in self.fields.keys():
            string += "this." + key + ","
        string = string[:-1] + "});\n"
        return string

    def __create_from_json(self):
        string = self.name + ".fromJson(Map<String, dynamic> json) {\n"
        for key, value in self.fields.items():
            if type(value) == list:
                datatype = type(value[0])
                if datatype == str:
                    string += "      " + key + " = json['" + key + "'].cast<String>();\n"
                elif datatype == int:
                    string += "      " + key + " = json['" + key + "'].cast<int>();\n"
                elif datatype == dict:
                    string += "      if(json['" + key + "'] != null){\n         " + key + " = new List<" + key.capitalize() + ">();\n         json['" + key + "'].forEach((v) {\n            " + key + ".add(new " + key.capitalize() + ".fromJson(v));\n         });\n      }\n "
            elif type(value) == dict:
                string += "      " + key + " = json['" + key + "'] != null ? new " + key.capitalize() + ".fromJson(json['" + key + "']) : null;\n"
            else:
                string += "      " + key + " = json['" + key + "'];\n"
        string += "   }\n"
        return string

    def __create_to_json(self):
        string = "Map<String, dynamic> toJson() {\n      final Map<String, dynamic> data = new Map<String, dynamic>();\n"
        for key, value in self.fields.items():
            if type(value) == dict:
                string += "      if (this." + key + " != null){\n         data['" + key + "'] = this." + key + ".toJson();\n      }\n"
            elif type(value) == list:
                dtype = type(value[0])
                if dtype == dict:
                    string += "      if (this." + key + " != null) {\n         data['" + key + "'] = this." + key + ".map((v) => v.toJson()).toList();\n      }\n"
                else:
                    string += "      data['" + key + "'] = this." + key + ";\n"
            else:
                string += "      data['" + key + "'] = this." + key + ";\n"

        string += "      return data;\n   }"
        return string

    def create_class(self):
        fields_initial = self.__create_fields()
        constructor = self.__create_constructor()
        from_json = self.__create_from_json()
        to_json = self.__create_to_json()
        string = "class %s {\n%s\n   %s\n   %s\n   %s\n}" % (self.name, fields_initial, constructor, from_json, to_json)
        return string
