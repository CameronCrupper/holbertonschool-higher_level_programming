#!/usr/bin/python3

import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """

        """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """

        """
        file = cls.__name__ + ".json"
        listobj = []
        if list_objs is not None:
            for i in list_objs:
                listobj.append(cls.to_dictionary(i))
        with open(file, 'w') as myFile:
            myFile.write(cls.to_json_string(listobj))

    @staticmethod
    def from_json_string(json_string):
        """

        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """

        """
        if cls.__name__ == "Rectangle":
            fake = cls(1, 1)
        elif cls.__name__ == "Square":
            fake = cls(1)
        fake.update(**dictionary)
        return fake

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        new = []
        with open(file, 'r') as myFile:
            new = cls.from_json_string(myFile.read())
            for i, j in enumerate(new):
                new[i] = cls.create(**new[i])
        return new
