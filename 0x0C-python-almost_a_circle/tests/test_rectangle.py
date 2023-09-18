import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io

class TestRectangleMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_01_class_type(self):
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_02_inherits_base(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_03_constructor_no_args(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_04_constructor_many_args(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(e.exception), s)

    def test_05_constructor_one_args(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

 

if __name__ == "__main__":
    unittest.main()
