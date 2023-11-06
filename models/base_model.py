#!/usr/bin/python3
"""
This module has the Base Model class
"""
from datetime import datetime
import uuid


class BaseModel:
    """ Represents Base Model class. """
    def __int__(self):
        """
        Instance initialization
        """
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()
