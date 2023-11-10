#!/usr/bin/python3
"""unittest case"""

import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Test Case for testing Creation of a new instance."""

    def test_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_is_public(self):
        b1 = Base(10)
        b1.id = 8
        self.assertEqual(b1.id, 8)

    def test_nb_objects_is_private(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_objects)

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b3.id - 2)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(10, 8)

    def test_None_ID(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_objects(self):
        b1 = Base(None)
        b2 = Base(10)
        b3 = Base(None)
        b4 = Base(None)
        self.assertEqual(b1.id, b4.id - 2)

    def test_str_id(self):
        b1 = Base("laila")
        self.assertEqual(b1.id, "laila")

    def test_list_id(self):
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_tuple_id(self):
        b1 = Base((1, 2))
        self.assertEqual(b1.id, (1, 2))

    def test_dict_id(self):
        b1 = Base({"h": 1, "i": 2})
        self.assertEqual(b1.id, {"h": 1, "i": 2})

    def test_bool_id(self):
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_float_id(self):
        b1 = Base(10.8)
        self.assertEqual(b1.id, 10.8)

    def test_complex_id(self):
        b1 = Base(complex(5))
        self.assertEqual(b1.id, complex(5))

    def test_set_id(self):
        b1 = Base({1, 2, 3})
        self.assertEqual(b1.id, {1, 2, 3})

    def test_frozenset_id(self):
        b1 = Base(frozenset({1, 2, 3}))
        self.assertEqual(frozenset({1, 2, 3}), b1.id)

    def test_nan_id(self):
        b1 = Base(float('nan'))
        self.assertNotEquals(b1.id, float('nan'))

    def test_inf_id(self):
        b1 = Base(float('inf'))
        self.assertEqual(b1.id, float('inf'))

    def test_byte_id(self):
        b1 = Base(b'laila')
        self.assertEqual(b1.id, b'laila')

    def test_bytearray_id(self):
        b1 = Base(bytearray(b'laila'))
        self.assertEqual(bytearray(b'laila'), b1.id)

    def test_range_id(self):
        b1 = Base(range(2))
        self.assertEqual(b1.id, range(2))


if __name__ == "__main__":
    unittest.main()
