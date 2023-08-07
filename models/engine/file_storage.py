#!/usr/bin/python3
""" module file_storage"""
import json

class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
    
    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                from models.base_model import BaseModel
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
    """    
    def save(self):
        with open(self.__file_path, "w") as f:
            if len(self. __objects) != 0:
                str_to_json = json.dumps(self.__objects)
                f.write(str_to_json)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                str_json = f.read()
        except FileNotFoundError:
            return

        return json.loads(str_json)



    """
