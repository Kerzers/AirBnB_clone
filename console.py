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
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

