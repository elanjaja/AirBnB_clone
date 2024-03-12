#!/usr/bin/python3
"""
defines a simple class
It handles how data is stored & persisted within our application
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """class for FileStorage
    The class tries to persist data through serialization and
    deserialization of Python
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns All instance objects saved
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        The method populates the __objects dictionary with objects
        where key is clase_name_of_instance.id
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """JSON SERIALIZATION
        This method serialies a Python instance to a JSON representation
        """

        obj_data = FileStorage.__objects
        file_path = FileStorage.__file_path
        obj_data_dict = {
                    key: obj_data[key].to_dict() for key in obj_data.keys()}
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(obj_data_dict, json_file)

    def reload(self):
        """JSON DESERIALIZATION
        This method deserializes a JSON string rep.
        """
        try:
            file_path = FileStorage.__file_path
            with open(file_path, "r", encoding="utf-8") as json_file:
                obj_data = json.load(json_file)
                for data in obj_data.values():
                    if data["__class__"]:
                        class_name = data["__class__"]
                        del data["__class__"]
                    self.new(eval(class_name)(**data))
        except FileNotFoundError:
            pass
