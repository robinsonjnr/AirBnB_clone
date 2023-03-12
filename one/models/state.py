#!/usr/bin/python3
"""this is the module that creates a state class"""

from models.base_model import BaseModel

class State(BaseModel):
    name = ""
def __init__(self, *args, **kwargs):
    """initializes the attributes of the state class"""
    super().__init__(*args, **kwargs)