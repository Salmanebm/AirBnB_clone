#!/usr/bin/python3
"""
This module has the Base Model class
"""
from datetime import datetime
import uuid

import models


class BaseModel:
    """ Represents Base Model class. """
    def __init__(self, *args, **kwargs):
        """
        Instance initialization
        - If the instance is new: it creates new instance with its new attrs
        - If the instance has previously created data in the database,
            it's restored again.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Customized string representation of the class
        :return: None
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the datetime during any change
        :return: None
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        converts all attributes to a dictionary to be converted to JSON
        representation.
        :returns: dictionary containing all keys/values of __dict__
        """
        dict_copy = self.__dict__
        dict_copy["__class__"] = str(self.__class__.__name__)
        # if isinstance(dict_copy["created_at"], datetime):
        dict_copy["created_at"] = str(self.created_at.isoformat())
        # if isinstance(dict_copy["updated_at"], datetime):
        dict_copy["updated_at"] = str(self.updated_at.isoformat())
        return dict_copy
