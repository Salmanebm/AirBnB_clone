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

    def do_help(self, arg):
        """
        Represents the help command
        """
        commands = {
            "EOF": "end of file",
            "help": "help command to show description of each command",
            "quit": "Quit command to exit the program"
        }

        if arg:
            print(f"{commands[arg]}\n")
        else:
            print("\n" + "Documented commands (type help <topic>):")
            print("========================================")
            for command in commands.keys():
                print(f"{command}", end="  ")
            print("\n")

    def emptyline(self):
        """
        Handles empty line + ENTER to not print anything
        """
        return False


if __name__ == "__main__":
    HBBNCommand().cmdloop()
