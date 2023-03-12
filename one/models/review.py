#!/usr/python3
"""a module that creates the review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
def __init__(self, *args, **kwargs):
    """initializes the attributes of the review class"""
    super().__init__(*args, **kwargs)