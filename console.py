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
            # try:
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
            # except KeyError:
            #     print("** class doesn't exist **")


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            # try:
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
            # except KeyError:
            #     print("** class doesn't exist **")


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

    # def do_update(self, arg):
    #     """Updates an instance based on the class name and id"""
    #
    #     args = arg.split()
    #     if not args:
    #         print("** class name missing **")
    #     else:
    #         try:
    #             cls_name = args[0]
    #             if len(args) < 2:
    #                 print("** instance id missing **")
    #                 return
    #             instance_id = args[1]
    #             key = "{}.{}".format(cls_name, instance_id)
    #             all_objects = models.storage.all()
    #             if len(args) < 3:
    #                 print("** attribute name missing **")
    #                 return
    #             instance_name = args[2]
    #             key = "{}.{}".format(cls_name, instance_name)
    #             if len(args) < 4:
    #                 print("** value missing **")
    #                 return
    #             instance_value = args[3]
    #             key = "{}.{}".format(cls_name, instance_value)
    #                 models.storage.save()
    #             else:
    #                 print("** no instance found **")
    #         except KeyError:
    #             print("** class doesn't exist **")















        


    # def do_update(self, arg):
    #     """Updates an instance based on the class name and id"""
    #     args = arg.split()
    #     if not args:
    #         print("** class name missing **")
    #     else:
    #         try:
    #             cls_name = args[0]
    #             if len(args) < 2:
    #                 print("** instance id missing **")
    #                 return
    #             instance_id = args[1]
    #             key = "{}.{}".format(cls_name, instance_id)
    #             all_objects = models.storage.all()
    #             if key in all_objects:
    #                 if len(args) < 3:
    #                     print("** attribute name missing **")
    #                 elif len(args) < 4:
    #                     print("** value missing **")
    #                 else:
    #                     attr_name = args[2]
    #                     attr_value = args[3]
    #                     obj = all_objects[key]
    #                     if hasattr(obj, attr_name):
    #                         attr_type = type(getattr(obj, attr_name))
    #                         setattr(obj, attr_name, attr_type(attr_value))
    #                         models.storage.save()
    #                     else:
    #                         print("** attribute doesn't exist **")
    #             else:
    #                 print("** no instance found **")
    #         except KeyError:
    #             print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
