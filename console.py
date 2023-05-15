#!/usr/bin/python3
""" The entry point of the command interpreter """

import sys
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
import shlex


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
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes_allowed:
            print("**classes doesn't exist**")
        else:
            new_obj = HBNBCommand.classes_allowed[line]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id

        """

        command = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif command[0] not in HBNBCommand.classes_allowed:
            print("** class doesn't exist **")
            return
        elif len(command) == 1:
            print("** instance id missing **")
            return
        else:
            inst_data = command[0] + "." + command[0]
            allowed_instances = storage.all()
            if inst_data not in allowed_instances:
                print("** no instance found **")
            else:
                obj = allowed_instances[inst_data]
                print(obj)

    def do_destroy(self, line):
        """
        command to delete an instance specified
        """

        command = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif command[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return
        elif len(command) < 2:
            print("** instance id missing **")
            return
        else:
            key = command[0] + "." + command[1]
            allowed_instances = storage.all()
            if key not in allowed_instances:
                print("** no instance found **")
            else:
                del (allowed_instances[key])
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """

        n_list = []
        all_inst = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in all_inst.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(all_inst[key])
                    n_list.append(val)
            else:
                val = str(all_inst[key])
                n_list.append(val)
                print(n_list)

    def do_update(self, line):
        """ Updates an instance based on the class
            name and id by adding or updating attribute
        """
        n_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif n_list[0] not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return
        elif len(n_list) == 1:
            print("** instance id missing **")
            return
        elif len(n_list) == 2:
            print("**attribute name missing**")
        elif len(n_list) == 3:
            print("**value missing**")
        else:
            key = n_list[0] + "." + n_list[1]
            allowed_instances = storage.all()
            if key not in allowed_instances:
                print("** no instance found **")
            else:
                obj = allowed_instances[key]
                setattr(obj, n_list[2], n_list[3])
                storage.save()

    def default(self, line):
        """
        When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
            "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.

        """
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]

            if class_name in self.classes_allowed:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
