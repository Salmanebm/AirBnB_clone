#!/usr/bin/python3
"""
This module has the Base Model class
"""
from datetime import datetime
import uuid


class BaseModel:
    """ Represents Base Model class. """
    def __init__(self, *args, **kwargs):
        """
        Instance initialization
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Customized string representation of the class
        :return: None
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        :return: None
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        :returns: dictionary containing all keys/values of __dict__
        """
        self.__dict__["__class__"] = str(self.__class__.__name__)
        self.__dict__["created_at"] = str(self.created_at.isoformat())
        self.__dict__["updated_at"] = str(self.updated_at.isoformat())
        return self.__dict__


""" *********** TEST ************* """
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(f"line 1: {my_model.id}")
print(f"line 2: {my_model}")
print(f"line 3: {type(my_model.created_at)}")
print("--")
my_model_json = my_model.to_dict()
print(f"line 4: {my_model_json}")
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
