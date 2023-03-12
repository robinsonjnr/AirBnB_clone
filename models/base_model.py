#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
#from models import storage

class BaseModel:
    """Class from which all other classes will inherit"""
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            *args: list of arguments
            **Kwargs: dict of key values arguments
        """

        if kwargs is not None and kwargs != {}:
            for keys in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%y-%m-%dt%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%y-%m-%dt%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".format (type(self).__name__, self.id, self.__dict__)
    def save(self):
        """updates the public instance attribute updated at"""
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict








