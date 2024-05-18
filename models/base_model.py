#!/usr/bin/python3
"""The base model module"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methodes for other classes"""
    def __init__(self, *args, **kwargs):
        """Initiate the base model class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    
    def save(self):
        """
        Update the public instance attribute update_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dic__ 
        of the instance
        """
        # make a copy of the __dict__
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__

        return dict_copy
        
    def __str__(self):
        """Print the string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

