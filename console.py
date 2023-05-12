#!/usr/bin/python3
""" The entry point of the command interpreter """

import cmd
import models
from datetime import datetime


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
        if command is None or command == "":
            print("** class name missing **")
        elif command not in self.classes_allowed:
            print("**classes doesn't exist**")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id

        """

        command = self.parseline(line)[0]
        phrase = self.parseline(line)[1]

        if command == "" or command is None:
            print("** class name missing **")
        elif command not in self.classes_allowed:
            print("** class doesn't exist **")
        elif phrase == '':
            print("** instance id missing **")
        else:
            inst_data = storage.all().get(command + '.' + phrase)
            if inst_data is None:
                print("** no instance found **")
            else:
                print(inst_data)

    def do_destroy(self, line):
        """
        command to delete an instance specified
        """

        if line == "" or line is None:
            print("** class name missing **")
        else:
            phrase = line.split('')
            if phrase[0] not in storage.all():
                print("** class doesn't exist **")
            elif len(phrase) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(phrase[0], phrase[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if line != "":
            phrase = line.split('')
            if phrase[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                n_list = [str(obj) for key, obj in storage.all()
                          if type(obj).__name__ == phrase[0]]
                print(n_list)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """ Updates an instance based on the class
            name and id by adding or updating attribute
        """
        phrase = shlex.split(line)
        phrase_size = len(phrase)
        if phrase_size == 0:
            print("** class name missing **")
        elif phrase[0] not in self.classes_allowed:
            print("** class doesn't exist **")
        elif phrase_size == 1:
            print("** instance id missing **")
        else:
            key = phrase[0] + '-' + phrase[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print("** no instance found **")
            elif phrase_size == 2:
                print("** attribute name missing **")
            elif phrase_size == 3:
                print("** value missing **")
            else:
                phrase[3] = self.analy_parameter_value(phrase[3])
                setattr(inst_data, phrase[2], phrase[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()

    def analy_parameter_value(self, value):
        """Check a parameter value for an update
            Analyze if a parameter is a string that needs
            to be converted to a float or an integer number.

            Args:
                value: The value to analze
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
