#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ A class to make a test suit for max_integer method."""
    def test_no_arg(self):
        """Method to Test for NO argument Case"""
        self.assertEqual(max_integer(), None)

    def test_one_el(self):
        """Method to Test for 1 element Case"""
        self.assertEqual(max_integer([21]), 21)

    def test_two_eq_el(self):
        """Method to Test for 1 element Case"""
        self.assertEqual(max_integer([21, 21]), 21)

    def test_ordered_list(self):
        """Method to Test for ordered list case"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_unordered_list(self):
        """Method to Test for unordered list case"""
        self.assertEqual(max_integer([3, 1, 2]), 3)

    def test_negative_list(self):
        """Method to Test for negative list case"""
        self.assertEqual(max_integer([-5, -10, -2, -8, -15, -3]), -2)

    def test_positive_negative_list(self):
        """Method to Test for positive and negative list"""
        self.assertEqual(max_integer([-5, -10, 2, 8, -15, -3, 0]), 8)

    def test_positive_negative_large(self):
        """Method to Test for positive and negative large numbers list"""
        self.assertEqual(
            max_integer(
                [-6351, 9735, -8649, 4405, 6261, -1907, -9443, -6308,
                    7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                    -6683, 715, -8738, 9678, -1081, 4730, -1376, 9126,
                    -8394, 9732, 1695, -4932, -2100, -6920, 2219, -7319,
                    -1193, -422, 9312, 9508, 9823, -2690, -9206, 4461,
                    2997, -6753, -7824, 3097, 1681,
                    3401, 7221, 1758, -1990, 4958, 4347,
                    7054, 545, 3492, -7285, -1672, 2230]), 9823)

    def test_int_float_list(self):
        """Method to Test for positive int and floats"""
        self.assertEqual(max_integer([2, 3.5, 1, 7.2, 5]), 7.2)

    def test_int_float_negative_list(self):
        """Method to Test for positive and negative int and floats"""
        self.assertEqual(max_integer([2, -3.5, 1, -7.2, 5]), 5)

    def test_int_float_negative_large_list(self):
        """Method to Test for positive and negative large int and floats"""
        self.assertEqual(max_integer([12345, -999.567, 98765, -123456,
                                        99999, -87654, 54321, -100000, 87654,
                                        -12345, 55555, -98765, 11111, -88888,
                                        22222]), 99999)

    def test_float_large_list(self):
        """Method to Test for large  floats"""
        self.assertEqual(max_integer([0.027891891117170508, 0.8464685760135892,
                                         4.506719557284897, 2.0258041087808,
                                         4.525163681550944, 1.3277284362225874,
                                         3.042753010712081, 2.4201460936424986,
                                         0.6254206993310946, 3.6037820704785766,
                                         0.5843942753272469, 2.994055932449279,
                                         0.5168645505697169, 0.014982685631661026,
                                         0.02477737364433171,
                                         0.47120480947220955, 2.5056796257122915,
                                         1.3349487122618868, 0.08451917751917885,
                                         1.0157082402123356, 29.496355326217376,
                                         10.171800729369348, 1.1263544935158727]),
                                         29.496355326217376)

    def test_str(self):
        """Method to Test for string argument"""
        self.assertEqual(max_integer("laila"), "l")

    def test_list_of_strings(self):
        """Method to Test for a list of strings argument"""
        self.assertEqual(max_integer(["laila", "hi", "ebrahim"]), "laila")

     def test_lists_of_ints(self):
        """Method to Test for  a list of int lists"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_lists_of_strings(self):
        """Method to Test for  a list of string lists"""
        self.assertEqual(max_integer([["aa"], ["hi"], ["abc"], ["hello"], ["zd"]]),
                             ["zd"])

    def test_nan(self):
        """Method to Test for a list contain nan"""
        self.assertEqual(max_integer([1, 55, float('nan')]), 55)

    def test_infinity(self):
        """Method to Test for a list contain infinity"""
        self.assertEqual(max_integer(float('inf'), 10000000, 0), float('inf'))

    def test_number_string(self):
        """Method to Test for a string conatin numbers"""
        self.assertEqual(max_integer("198762"), "9")

    def test_mixed_list(self):
        """Method to Test for a mixed list"""
        with self.assertRaises(TypeError):
            max_integer([[1, 2], 21, "laila"])

    def test_none(self):
        """Method to Test for a none argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dictionary(self):
        """Method to Test for a dictionary argument"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_float_arg(self):
        """Method to Test for a float argument"""
        with self.assertRaises(TypeError):
            max_integer(6.6)

    def test_int_arg(self):
        """Method to Test for a int argument"""
        with self.assertRaises(TypeError):
            max_integer(6)


if __name__ == '__main__':
    unittest.main()
                         
