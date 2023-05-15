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
        if len(line) == 0:
            return
        else:
            args = line.split('.')
            word_args = args[0]
            if word_args in HBNBCommand.allowed_classes:
                if len(args) == 2:
                    if args[1] == "all()":
                        HBNBCommand.do_all(self, word_args)
                    elif args[1] == "count()":
                        print((HBNBCommand.instance_count(self, word_args)))
                    elif str(args[1])[:4] == "show":
                        string = args[1]
                        c_id = string[6:-2]
                        l_ine = str(word_args) + " " + str(c_id)
                        HBNBCommand.do_show(self, l_ine)
                    elif str(args[1])[:7] == "destroy":
                        string = args[1]
                        c_id = string[9:-2]
                        l_ine = str(word_args) + " " + str(c_id)
                        HBNBCommand.do_destroy(self, l_ine)
                    elif str(args[1])[:6] == "update":
                        a_slc = args[1][7:-1]
                        my_list = a_slc.split(", ")
                        _id = my_list[0][1:-1]
                        if type(my_list[1]) == dict:
                            for att, val in my_list[1].items():
                                l_att = word_args + " " + _id + " " + att + val
                                HBNBCommand.do_update(self, l_att)
                        else:
                            if my_list[2][0] == '"' and my_list[2][-1] == '"':
                                val = my_list[2][1:-1]
                            else:
                                val = my_list[2]
                            if my_list[1][0] == '"' and my_list[1][-1] == '"':
                                attr = my_list[1][1:-1]
                            else:
                                attr = my_list[1]
                            l_att = str(word_args + " " + _id + " " + attr +
                                        " " + val)
                            HBNBCommand.do_update(self, l_att)
                    else:
                        pass
                else:
                    print("Try: {}.all() or all {}".format(args[0], args[0]))
            else:
                print("*** Unknown syntax: {}".format(line))
                return

    def do_count(self, line):
        """ counts and prints the instances of a class """

        counts = 0
        n_list = []
        all_list = []
        allowed_instances = storage.all()
        if line == "":
            for k, obj in allowed_instances.items():
                all_list.append(str(obj))
                counts = counts + 1
            return(counts)
        elif line in HBNBCommand.allowed_classes:
            for k, v in allowed_instances.items():
                if line == v.__class__.__name__:
                    keys = line + "." + str(v.id)
                    n_list.append(allowed_instances[keys])
                    counts = counts + 1
            return(counts)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
