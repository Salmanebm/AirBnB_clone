#!/usr/bin/python3
"""
This module has the User class
"""
from datetime import datetime

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents the User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
