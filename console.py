#!/usr/bin/python3
"""AirBnB Console - project entry point """

import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class definition for HBNBCommand """

    prompt = '(hbnb) '
    class_list = {'BaseModel': BaseModel,
            #    'User': User, 'City': City,
            #    'Place': Place, 'Amenity': Amenity, 'Review': Review,
            #    'State': State
               }

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
        """  Prints the string representation of an instance based on the class name and id"""

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


    # def do_all(self, arg):
    #     """ Method to print all instances """
    #     if len(arg) == 0:
    #         print([str(a) for a in storage.all().values()])
    #     elif arg not in self.classes:
    #         print("** class doesn't exist **")
    #     else:
    #         print([str(a) for b, a in storage.all().items() if arg in b])

    # def do_update(self, arg):
    #     """ Method to update JSON file"""
    #     arg = arg.split()
    #     if len(arg) == 0:
    #         print('** class name missing **')
    #         return
    #     elif arg[0] not in self.classes:
    #         print("** class doesn't exist **")
    #         return
    #     elif len(arg) == 1:
    #         print('** instance id missing **')
    #         return
    #     else:
    #         key = arg[0] + '.' + arg[1]
    #         if key in storage.all():
    #             if len(arg) > 2:
    #                 if len(arg) == 3:
    #                     print('** value missing **')
    #                 else:
    #                     setattr(
    #                         storage.all()[key],
    #                         arg[2],
    #                         arg[3][1:-1])
    #                     storage.all()[key].save()
    #             else:
    #                 print('** attribute name missing **')
    #         else:
    #             print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
