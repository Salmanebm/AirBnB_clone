#!/usr/bin/python3
"""
This module has the entry point to the command interpreter
"""
import cmd
import json
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Represents command interpreter class
    """
    prompt = '(hbnb) '
    misc_header = 'This is misc_header test'

    __classes = {
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
    }

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

    def do_show(self, line):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return

        object_key = f"{args[0]}.{args[1]}"

        if object_key not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[object_key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id,
        (save the change into the JSON file).
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return

        object_key = f"{args[0]}.{args[1]}"
        if object_key not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[object_key]
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
