#!/usr/bin/python3
"""AirBnB Console - project entry point """

import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Class definition for HBNBCommand """

    prompt = '(hbnb) '
    class_list = {'BaseModel': BaseModel, 'User': User,
                  'City': City, 'Place':
                      Place, 'Amenity': Amenity,
                      'Review': Review, 'State': State}

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Signal to exit the program """
        print('')
        return True

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """ Create a new class instance and print its id """
        if not arg:
            print('** class name missing **')
            return

        class_name = arg.strip()
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        new_instance = self.class_list[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """  Prints the str rep of an inst based on class name and id"""

        args_list = arg.split()
        if not args_list:
            print('** class name missing **')
            return
        class_name = args_list[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print('** instance id missing **')
            return
        instance_id = args_list[1]
        key = f'{class_name}.{instance_id}'
        if key in storage.all():
            instance = storage.all()[key]
            print(instance)
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return

        arg_list = arg.split()

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        class_name = arg_list[0]
        instance_id = arg_list[1]

        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances"""
        if not arg:
            print([str(instance) for instance in storage.all().values()])
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        else:
            print([str(instance) for key, instance
                   in storage.all().items() if arg in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print('** class name missing **')
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return

        class_name = arg_list[0]
        instance_id = arg_list[1]

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print('** no instance found **')
            return
        if len(arg_list) < 3:
            print('** attribute name missing **')
            return
        if len(arg_list) < 4:
            print('** value missing **')
            return
        attribute_name = arg_list[2]
        attribute_value = arg_list[3][1:-1]
        setattr(storage.all()[key], attribute_name, attribute_value)
        storage.all()[key].save()

    def precmd(self, argument):
        """ executed just before the command line is interpreted """
        args = argument.split('.', 1)
        if len(args) == 2:
            class_name = args[0]
            args = args[1].split('(', 1)
            class_name_strip = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = class_name_strip + " " + class_name + " "\
                + _id + " " + other_arguments
            print(line)
            return line
        else:
            return argument

    def do_count(self, argument):
        """  Retrieve the number of instances of a class """
        token_list = shlex.split(argument)
        dict = storage.all()
        num_instances = 0
        if token_list[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        else:
            for key in dict:
                class_name = key.split('.')
                if class_name[0] == token_list[0]:
                    num_instances += 1

            print(num_instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
