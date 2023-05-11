#!/usr/bin/python3
""" The entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ A class that implements:
    quit and EOF to exit the program
    help (this action is provided by default by
    cmd but you should keep it updated and
    documented as you work through tasks)
    a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything

    """

    prompt = "(hbnb)"
    classes_allowed = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def emptyline(self):
        """ method to check when an empty line is parsed """
        pass

    def do_quit(self, line):
        """ command to quit the program from the prompt """
        print()
        return True

    def do_EOF(self, line):
        """ The method recognizes ctrl d to quit the program """
        print()
        return True

    def do_create(self, line):
        """ Create a new instance of BaseModel class """
        command = self.parseline(line)[0]
        if command is None or command = "":
            print("** class name missing **")
        elif command not in self.classes_allowed:
            print("**classes doesn't exist**")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id 

        """






if __name__ == '__main__':
    HBNBCommand().cmdloop()




















