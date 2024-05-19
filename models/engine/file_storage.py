#!/usr/bin/python3
"""The module for data storage, serialization ad deserialization"""


from models.base_model import BaseModel
import json

class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as json_file:
                obj_dict = json.load(json_file)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                cls = self.classes()[cls_name]
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
    
    @staticmethod
    def classes():
        """Returns a dictionary of valid classes that can be instantiated."""
        from models.base_model import BaseModel

        return {
                "BaseModel": BaseModel
                }
