#!/usr/bin/python3
# simple Python command-line interface
# loops terminal after processing a command

import sys
import cmd


class HelloWorld(cmd.Cmd):
    """
    Simple command
    """

    def do_greet(self, line):
        print("Hello")

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()

