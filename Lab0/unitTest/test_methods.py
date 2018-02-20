#!/usr/bin/env python3

import unittest
import methods
 
class my_unit_test_class(unittest.TestCase):
 
    def test_numbers_3_4(self):
        self.assertEqual(methods.multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual(methods.multiply('a',3), 'aaa')

    def test_check_even(self):
        self.assertEqual(methods.check_even(4), True)
 
if __name__ == '__main__':
    unittest.main()
