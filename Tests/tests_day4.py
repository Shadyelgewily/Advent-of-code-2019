# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:16:08 2020

@author: quiet
"""

import unittest
from Day4.class_password_generator import password_generator

class TestSuite(unittest.TestCase):
    
        def setUp(self):
            self.test_password1 = password_generator('111111-222222')
            
        def test_password_in_range_true(self):
            result = self.test_password1.is_password_in_range(111222)
            expected_result = True
            
            self.assertIs(result, expected_result)
        
        def test_password_in_range_false(self):
            result = self.test_password1.is_password_in_range(333333)
            expected_result = False
            
            self.assertIs(result, expected_result)
        
        def test_atleast_two_adjacent_digits_same_false(self):
            result = self.test_password1.is_atleast_two_adjacent_digits_same(137683)
            expected_result = False
            
            self.assertIs(result, expected_result)
        
        def test_atleast_two_adjacent_digits_same_true(self):
            result = self.test_password1.is_atleast_two_adjacent_digits_same(222222)
            expected_result = True
            
            self.assertIs(result, expected_result)
            
        def test_exactly_two_adjacent_digits_same_false(self):
            result = self.test_password1.is_exactly_two_adjacent_digits_same(222222)
            expected_result = False
            
            self.assertIs(result, expected_result)
        
        def test_exactly_two_adjacent_digits_same_true(self):
            result = self.test_password1.is_exactly_two_adjacent_digits_same(223445)
            expected_result = True
            
            self.assertIs(result, expected_result)
            
        def test_nondecreasing_left_to_right_true(self):
            result = self.test_password1.is_nondecreasing_left_to_right(111123)
            expected_result = True
            
            self.assertIs(result, expected_result)
        
        def test_nondecreasing_left_to_right_false(self):
            result = self.test_password1.is_nondecreasing_left_to_right(223450)
            expected_result = False
            
            self.assertIs(result, expected_result)
    
if( __name__ == "__main__" ):
    unittest.main()