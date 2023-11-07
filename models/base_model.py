#!/usr/bin/python3
"""
This module has the Base Model class
"""
from datetime import datetime
import uuid


class BaseModel:
    """ Represents Base Model class. """
    def __init__(self):
        """
        Instance initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Customized string representaion of the class
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
        return self.__dict_
