#!/usr/bin/python3
"""Base Class Module"""
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Transfers serialized(csv) data into
        a file
        """
        with open(f"{cls.__name__}.csv", "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attrlist = ['id', 'width', 'height', 'x', 'y']
                else:
                    attrlist = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(file, attrlist)
                for ins in list_objs:
                    writer.writerow(ins.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns deserialized(csv) list of instances"""
        try:
            with open(f"{cls.__name__}.csv", "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    attrlist = ['id', 'width', 'height', 'x', 'y']
                else:
                    attrlist = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(file, attrlist)
                reader = [dict([i, int(j)] for i, j in elem.items())
                          for elem in reader]
                return [cls.create(**elem) for elem in reader]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the Rectangles and Squares"""
        t_obj = turtle.Turtle()
        t_obj.screen.bgcolor("#04bf1a")
        t_obj.pensize(3)
        t_obj.shape("turtle")

        t_obj.color("#fff600")
        for rec_obj in list_rectangles:
            t_obj.showturtle()
            t_obj.up()
            t_obj.goto(rec_obj.x, rec_obj.y)
            t_obj.down()
            for _ in range(2):
                t_obj.forward(rec_obj.width)
                t_obj.left(90)
                t_obj.forward(rec_obj.height)
                t_obj.left(90)
            t_obj.hideturtle()

        t_obj.color("#b5e3d8")
        for sq_obj in list_squares:
            t_obj.showturtle()
            t_obj.up()
            t_obj.goto(sq_obj.x, sq_obj.y)
            t_obj.down()
            for _ in range(2):
                t_obj.forward(sq_obj.width)
                t_obj.left(90)
                t_obj.forward(sq_obj.height)
                t_obj.left(90)
            t_obj.hideturtle()

        turtle.exitonclick()
