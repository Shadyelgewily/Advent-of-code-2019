# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:52:18 2020

@author: quiet
"""

import unittest

from Day6.class_orbits import orbits

class TestSuite(unittest.TestCase):
    
    def test_example_input_part1(self):
        example_orbits = orbits("Input/day6_part1_example.txt")
        output = example_orbits.count_all_orbits()
        expected_output = 42
        
        self.assertIs(output, expected_output)
        
    def test_example_input_part2(self):
        example_orbits = orbits("Input/day6_part2_example.txt")
        example_orbits.find_shortest_path_part2()
        output = example_orbits.N_shortest_path
        expected_output = 4
        
        self.assertIs(output, expected_output)

if( __name__ == "__main__" ):
    unittest.main()