#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
            if cls_name != "BaseModel":
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
            if cls_name != "BaseModel":
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
        if not args or args[0] == "BaseModel":
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
            if cls_name != "BaseModel":
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(cls_name, instance_id)
            all_objects = models.storage.all()
            if not key in all_objects.keys():
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
           # attribute_value = args[3]
           #
           # if key in all_objects.keys():
           #     dict_attr = all_objects[key].__dict__.copy()
           #     dict_attr[args[2]] = args[3]
           #     all_objects[key].save()
###############
#
# 3an abi horayra radya laho 3anha
# had l code rah khdam mais manta3n
# t inspiray mno bash tl9ay solution 
# l code nta3dk
#            
###############
            if len(args) == 4:
                obj = all_objects["{}.{}".format(args[0], args[1])]
                if args[2] in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__[args[2]])
                    obj.__dict__[args[2]] = valtype(args[3])
                else:
                    obj.__dict__[args[2]] = args[3]
            elif type(eval(args[2])) == dict:
                obj = all_objects["{}.{}".format(args[0], args[1])]
                for k, v in eval(args[2]).items():
                    if (k in obj.__class__.__dict__.keys() and
                            type(obj.__class__.__dict__[k]) in {str, int, float}):
                        valtype = type(obj.__class__.__dict__[k])
                        obj.__dict__[k] = valtype(v)
                    else:
                        obj.__dict__[k] = v
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
