#!/usr/bin/python3
"""
This module has the entry point to the command interpreter
"""
import cmd


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

    def emptyline(self):
        """
        Handles empty line + ENTER to not print anything
        """
        return False


if __name__ == "__main__":
    HBBNCommand().cmdloop()
