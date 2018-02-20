#!/usr/bin/env python3

import unittest
import gs
 
class my_unit_test_class(unittest.TestCase):
 
    def test_numbers_3_4(self):
        self.assertEqual(len(gs.suitors), 10)
 
#     def test_strings_a_3(self):
#         self.assertEqual(methods.multiply('a',3), 'aaa')
# 
#     def test_check_even(self):
#         self.assertEqual(methods.check_even(4), True)
 
if __name__ == '__main__':
    unittest.main()
