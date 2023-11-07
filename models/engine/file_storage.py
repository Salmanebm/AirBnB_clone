#!/usr/bin/python3
"""
This module has FileStorage class
"""
import json


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
        new_obj = obj.__class__.__name
        FileStorage.__objects[f"{new_obj}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
