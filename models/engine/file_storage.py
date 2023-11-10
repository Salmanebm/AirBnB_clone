#!/usr/bin/python3
"""
This module has FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Represents FileStorage class.
        ATTRIBUTES:
         * __file_path: string - path to the JSON file
         * __objects: dictionary - empty but will store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_obj = {}
        for key in self.__objects:
            serialized_obj[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                all_objects = json.load(file)
                for obj_dict in all_objects:
                    class_name = eval(all_objects[obj_dict]["__class__"])
                    self.new(class_name(**all_objects[obj_dict]))
        except FileNotFoundError:
            pass
