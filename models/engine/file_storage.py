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
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    # def save(self):
    #     """
    #     Serializes __objects to the JSON file (path: __file_path).
    #     """
    #     with open(FileStorage.__file_path, 'w') as file:
    #         json.dump(FileStorage.__objects, file)

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path) as file:
                all_objects = json.load(file)
                for object_dict in all_objects.values():
                    class_name = object_dict["__class__"]
                    del object_dict["__class__"]
                    new_object = eval(class_name)(**object_dict)
                    self.new(new_object)
        except FileNotFoundError:
            pass
