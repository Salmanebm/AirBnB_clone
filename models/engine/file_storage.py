#!/usr/bin/python3

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split(".")
                        class_obj = globals()[class_name]
                        new_instance = class_obj(**value)
                        self.__objects[key] = new_instance
                except json.JSONDecodeError:
                    pass
