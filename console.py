#!/usr/bin/python3
""" Module for the custom interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage

class Console(cmd.Cmd):
    """A bass class that inherite from the base class Cmd"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """This handle the End Of File condition"""
        print()
        return True

    def default(self, line):
        """Provide the default value for an unknown input"""
        exec(line)

    def do_quit(self, line):
        """Exit the interpreter"""
        return True
    
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
        """
        Create a new instance of BaseModel, saves it and prints the id
        """
        if not line:
            print("** class name missing **")
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Show an instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """"
        Delete an instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Print all string representation of all instances
        """
        args = line.split()
        obj_list = []
        if not line:
            obj_list = [str(obj) for obj in storage.all().values()]
        elif args[0] in sorage.classes():
            obj_list = [str(obj) for key, obj in storage.all().items() if key.startswith(args[0])]
        else:
            print("** class doesn't exit **")
            return
        print(obj_list)

    def do_update(self, line):
        """
        Update an instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class Name missing **")
            return
        if args[0] not in storage.classes():
            print(" ** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            obj = storage.all()[key]
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        except KeyError:
            print("** no instance found **")

if __name__ == "__main__":
    Console().cmdloop()
