#!/usr/bin/python3
"""The base model module"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methodes for other classes"""
    def __init__(self, *args, **kwargs):
        """Initiate the base model class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if 'created_at' in key:
                        self.created_at = datetime.fromisoformat(value)
                    if 'updated_at' in key:
                        self.updated_at = datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            from models import storage
            storage.new(self)

    
    def save(self):
        """
        Update the public instance attribute update_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.save()

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

