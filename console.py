#!/usr/bin/python3
"""
This module has the entry point to the command interpreter
"""
import cmd
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
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
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        arg_instance = globals()[arg]()
        arg_instance.save()
        print(arg_instance.id)

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
        elif len(args) in (1, 2):
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            if len(args) != 2:
                print("** instance id missing **")
                return

        object_key = f"{args[0]}.{args[1]}"
        if object_key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[object_key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances,
        based or not on the class name.
        """
        obj_list = []
        for value in storage.all().values():
            if not arg or arg == value.__class__.__name__:
                obj_list.append(str(value))

        print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
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
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        new_value = args[3]
        key_to_find = f"{class_name}.{instance_id}"
        all_objects = storage.all()

        if key_to_find not in all_objects:
            print("** no instance found **")

        obj_to_update = all_objects[key_to_find]

        for key, value in all_objects.items():
            if key in obj_to_update.__class__.__dict__.keys():
                value_type = type(obj_to_update.__class__.__dict__[key])
                obj_to_update.__class__.__dict__[key] = value_type(new_value)
            else:
                obj_to_update.__class__.__dict__[key] = new_value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
