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
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

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
obj1 = BaseModel(name="Alice", age=25, __class_="Adel")
print("Attributes from kwargs:")
print(obj1.__dict__)  # Print the object's attributes

# Create an instance without any kwargs (default attributes will be used)
obj2 = BaseModel()
print("\nDefault attributes:")
print(obj2.__dict__)  # Print the object's attributes

# Access specific attributes
print(f"\nName: {obj1.name}")
print(f"Age: {obj1.age}")

# Access default attributes
print(f"\nID: {obj2.id}")
print(f"Created At: {obj2.created_at}")
print(f"Updated At: {obj2.updated_at}")

