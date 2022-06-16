class Generator:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def __create_fields(self):
        string = ""
        for key, value in self.fields.items():
            print(type(value))
            if type(value) == str:
                string += "\tString " + key + ";\n"
            elif type(value) == int:
                string += "\tint " + key + ";\n"
            elif type(value) == list:
                datatype = type(value[0])
                if datatype == str:
                    string += "\tList<String> " + key + ";\n"
                elif datatype == int:
                    string += "\tList<int> " + key + ";\n"
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
                    string += "\t\t" + key + " = json['" + key + "'].cast<String>();\n"
                elif datatype == int:
                    string += "\t\t" + key + " = json['" + key + "'].cast<int>();\n"
            else:
                string += "\t\t" + key + " = json['" + key + "'];\n"
        string += "\t}\n"
        return string

    def __create_to_json(self):
        string = "Map<String, dynamic> toJson() {\n\t\tfinal Map<String, dynamic> data = new Map<String, dynamic>();\n"
        for key in self.fields.keys():
            string += "\t\tdata['" + key + "'] = this." + key + ";\n"
        string += "\t\treturn data;\n\t}"
        return string

    def create_class(self):
        fields_initial = self.__create_fields()
        constructor = self.__create_constructor()
        from_json = self.__create_from_json()
        to_json = self.__create_to_json()
        string = "class %s {\n%s\n\t%s\n\t%s\n\t%s\n}" % (self.name, fields_initial, constructor, from_json, to_json)
        return string
