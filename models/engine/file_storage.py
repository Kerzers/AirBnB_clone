#!/usr/bin/python3
""" module file_storage"""
import json
import models

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
    """    
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
        with open(self.__file_path, "a") as f:
            if len(self. __objects) != 0:
                for key, value in self.__objects.items():
                    print("key:{}  value: {}".format(key, self.__objects[key]))
                    print("+++++++")
                serial_obj = {k: v.to_dict() for k, v in self.__objects.items()}
                str_to_json = json.dumps(serial_obj)
                f.write(str_to_json)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                str_json = f.read()
        except FileNotFoundError:
            return

        if len(str_json) != 0:
            data = json.loads(str_json)
            for k, v in data.items():
                class_name, obj_id = k.split('.')
                print("classe name {}".format(class_name))
                class_ref = globals().get(class_name)
                self.__objects[k] = class_ref(**v)
