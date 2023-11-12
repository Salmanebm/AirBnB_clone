#!/usr/bin/python3
"""
This module has the entry point to the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel


class HBBNCommand(cmd.Cmd):
    """
    Represents command interpreter class
    """
    prompt = '(hbnb) '
    misc_header = 'This is misc_header test'

    def do_quit(self, arg):
        """
        Quit command to quit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF to exit the program
        """
        sys.exit()

    def emptyline(self):
        """
        Handles empty line + ENTER to not print anything
        """
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if arg:
            if arg == "BaseModel":
                base_model_instance = BaseModel()
                base_model_instance.save()
                print(base_model_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBBNCommand().cmdloop()
