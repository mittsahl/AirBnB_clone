#!/usr/bin/python3
"""File Storage engine"""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """File storage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dict __objects"""
        return self.__objects

    def new(self, obj):
        """adds object to object dict with id key"""
        self.__objects[str(type(obj).__name__) + "." + obj.id] = obj

    def save(self):
        """Serializes objects to json file"""
        thangs = []
        for key, value in self.__objects.items():
            thangs.append(value.to_dict())
        with open(self.__file_path, "w+") as f:
            f.write(json.dumps(thangs))

    def reload(self):
        """Deserializes json file back into objects {} dict"""
        try:
            with open(self.__file_path, "r") as f:
                leest = json.loads(f.read())
            for obj in leest:
                if obj['__class__'] == "BaseModel":
                    self.new(BaseModel(**obj))
                if obj['__class__'] == "User":
                    self.new(User(**obj))
        except Exception:
            pass
