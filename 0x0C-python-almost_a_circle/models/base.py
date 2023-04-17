#!/usr/bin/python3
"""Base Class Module"""
import json


class Base:
    """Definition of Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """inputs a JSON string representation ,of a list
        of instances, into a file"""
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(Base.to_json_string([
                    i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes
        already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                ins = cls(1, 1)
            elif cls.__name__ == "Square":
                ins = cls(1)
            ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(f"{cls.__name__}.json") as file:
                ins_list = cls.from_json_string(file.read())
            return [cls.create(**attr) for attr in ins_list]
        except IOError:
            return []
