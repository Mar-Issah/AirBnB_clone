#!/usr/bin/python3
""" Unittest for BaseModel Class """

import unittest
import models
import os
from datetime import datetime
import time
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
  """Unittests for testing prompting of the HBNB command interpreter."""

  def setUp(self):
    """setup method"""
    self.console = HBNBCommand()

  def tearDown(self):
    """tearDown method"""
    pass

  def test_prompt_string(self):
    """test prompt output"""
    self.assertEqual("(hbnb) ", HBNBCommand.prompt)

  @patch('sys.stdout', new_callable=StringIO)
  def test_quit_command(self, mock_stdout):
        self.console.do_quit("")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

  @patch('sys.stdout', new_callable=StringIO)
  def test_eof_command(self, mock_stdout):
        self.assertTrue(self.console.do_EOF(""))
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

  @patch('sys.stdout', new_callable=StringIO)
  def test_emptyline_command(self, mock_stdout):
        self.console.emptyline()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages."""

    def test_help(self):
        help = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  create  help  quit")
            #  "EOF  all  count    destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, output.getvalue().strip())

    def test_help_quit(self):
        help = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help, output.getvalue().strip())

    def test_help_EOF(self):
        help = "Signal to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help, output.getvalue().strip())

    def test_help_create(self):
        help = ("Create a new class instance and print its id")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help, output.getvalue().strip())

    # def test_help_show(self):
    #     help = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
    #          "Display the string representation of a class instance of"
    #          " a given id.")
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         self.assertFalse(HBNBCommand().onecmd("help show"))
    #         self.assertEqual(help, output.getvalue().strip())

    # def test_help_destroy(self):
    #     help = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
    #          "Delete a class instance of a given id.")
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         self.assertFalse(HBNBCommand().onecmd("help destroy"))
    #         self.assertEqual(help, output.getvalue().strip())

    # def test_help_all(self):
    #     help = ("Usage: all or all <class> or <class>.all()\n        "
    #          "Display string representations of all instances of a given class"
    #          ".\n        If no class is specified, displays all instantiated "
    #          "objects.")
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         self.assertFalse(HBNBCommand().onecmd("help all"))
    #         self.assertEqual(help, output.getvalue().strip())

    # def test_help_count(self):
    #     help = ("Usage: count <class> or <class>.count()\n        "
    #          "Retrieve the number of instances of a given class.")
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         self.assertFalse(HBNBCommand().onecmd("help count"))
    #         self.assertEqual(help, output.getvalue().strip())

    # def test_help_update(self):
    #     help = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
    #          "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
    #          ">) or\n       <class>.update(<id>, <dictionary>)\n        "
    #          "Update a class instance of a given id by adding or updating\n   "
    #          "     a given attribute key/value pair or dictionary.")
    #     with patch("sys.stdout", new=StringIO()) as output:
    #         self.assertFalse(HBNBCommand().onecmd("help update"))
    #         self.assertEqual(help, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()