import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_01_nb_objects_private(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_02_nb_objects_initialized(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_03_instantiation(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_04_constructor(self):
        with self.assertRaisesRegex(TypeError, "__init__() missing 1 required positional argument: 'self'"):
            Base.__init__()

    def test_05_consecutive_ids(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_06_id_synced(self):
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_07_custom_id_int(self):
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_08_custom_id_str(self):
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_09_id_keyword(self):
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_10_to_json_string(self):
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument: 'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")

        d = [{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.to_json_string(d), s)

    def test_11_from_json_string(self):
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument: 'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(Base.from_json_string(s), d)

    def test_12_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

    def test_13_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_14_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))

if __name__ == "__main__":
    unittest.main()
