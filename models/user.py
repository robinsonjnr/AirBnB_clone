#!/usr/python3
"""this is a module that creates a user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """class for managing user objects"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
