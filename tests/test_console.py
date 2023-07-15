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
        """Setup method"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Teardown method"""
        pass

    def test_prompt_string(self):
        """Test prompt output"""
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

    def test_create_missing_class(self):
        """Test when class is missing"""
        error_msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(error_msg, output.getvalue().strip())

    def test_create_invalid_class(self):
        """Test when class name is not in the list."""
        error_msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(error_msg, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        """Test wrong syntax."""
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_class(self):
        """Test show with missing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **", output.getvalue().strip())

    def test_show_invalid_class(self):
        """Test show with invalid class"""
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        """Test destroy with missing id"""
        correct = "** instance id missing **"
        classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
        for class_name in classes:
            with patch("sys.stdout", new_callable=StringIO) as output:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {class_name}"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_all_invalid_class(self):
        """Test all with invalid class"""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_class(self):
        """Test update with missing class"""
        correct = "** class name missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(correct, output.getvalue().strip())

        correct2 = "** instance id missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("update ."))
            self.assertEqual(correct2, output.getvalue().strip())

    def test_update_invalid_class(self):
        """Test update with invalid class"""
        correct = "** instance id missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id(self):
        """Test update with missing id"""
        correct = "** instance id missing **"
        classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
        for class_name in classes:
            with patch("sys.stdout", new_callable=StringIO) as output:
                self.assertFalse(HBNBCommand().onecmd(f"update {class_name}"))
                self.assertEqual(correct, output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages."""

    def test_help(self):
        help_text = (
            "Documented commands (type help <topic>):\n"
            "========================================\n"
            "EOF  all  create  destroy  help  quit  show  update"
        )
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_quit(self):
        help_text = "Quit command to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_EOF(self):
        help_text = "Signal to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_create(self):
        help_text = "Create a new class instance and print its id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_show(self):
        help_text = "Prints the string rep of an inst based on class name and id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_destroy(self):
        help_text = "Method to delete instance with class and id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_all(self):
        help_text = "Prints all string representation of all instances"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_update(self):
        help_text = "Updates an instance based on the class name and id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(help_text, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
