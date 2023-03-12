#!/usr/bin/python3
"""this module creates a user class"""

from models.base_model import BaseModel

class City (BaseModel):
    """class for managing city objects"""

    state_id = ""
    name = ""

def __init__(self, *args, **kwargs):
    """ initializes the attributes for the city class"""
    super().__init__(*args, **kwargs)