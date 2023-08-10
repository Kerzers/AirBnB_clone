#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def extract_strings(lst):
    result = []
    quoted_section = 0
    current_string = ""

    for item in lst:
        if item.startswith('"') and item.endswith('"'):
            current_string = item[1:-1]   # Remove the opening & closing quote
            result.append(current_string)
        if item.startswith('"'):
            quoted_section = 1
            current_string = item[1:]  # Remove the opening quote
        elif item.endswith('"') and quoted_section:
            quoted_section = 0
            current_string += " " + item[:-1]  # Remove the closing quote
            result.append(current_string)
            current_string = ""
        elif quoted_section:
            current_string += " " + item
        else:
            pass
    return result


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    class_list = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name not in self.class_list:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(cls_name, instance_id)
            all_objects = models.storage.all()
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name not in self.class_list:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(cls_name, instance_id)
            all_objects = models.storage.all()
            if key in all_objects:
                del all_objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name. """
        args = arg.split()
        if not args or args[0] in self.class_list:
            if not args:
                cls_name = "BaseModel"
            else:
                cls_name = args[0]
            key = "{}".format(cls_name)
            all_objects = models.storage.all()
            for key in all_objects:
                if key in all_objects:
                    print(all_objects[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name not in self.class_list:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(cls_name, instance_id)
            all_objects = models.storage.all()
            if key not in all_objects.keys():
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return

            if args[3].startswith('"'):
                string_list = extract_strings(args)
                attribute_value = string_list[0]
            else:
                attribute_value = args[3]
            list_type_attr = [str, int, float]
            if key in all_objects.keys():
                if hasattr(all_objects[key], args[2]):
                    type_attr = type(getattr(all_objects[key], args[2]))
                    if type_attr in list_type_attr:
                        setattr(all_objects[key], args[2],
                                type_attr(attribute_value))
                else:
                    setattr(all_objects[key], args[2], attribute_value)
                all_objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
