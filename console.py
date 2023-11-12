#!/usr/bin/python3
"""
This module has the entry point to the command interpreter
"""
import cmd
import sys


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


if __name__ == "__main__":
    HBBNCommand().cmdloop()
