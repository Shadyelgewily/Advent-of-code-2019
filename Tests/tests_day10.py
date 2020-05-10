# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:03:09 2020

@author: quiet
"""

import unittest
import numpy as np
from Day10.class_monotoring_station import monotoring_station

class TestSuite(unittest.TestCase):
 
    def test_best_location_example1(self):
        station_finder = monotoring_station('Input/day10_part1_example.txt' )
        station_finder.find_best_station_location()
        output = station_finder.best_location
        expected_output = (3, 4)
        self.assertSequenceEqual(output, expected_output)
        
    def test_N_asteroids_best_location_example1(self):
        station_finder = monotoring_station('Input/day10_part1_example.txt' )
        station_finder.find_best_station_location()
        output = station_finder.N_visible_at_best_location
        expected_output = 8
        self.assertEqual(output, expected_output)
        
    def test_best_location_example2(self):
        station_finder = monotoring_station('Input/day10_part1_example2.txt' )
        station_finder.find_best_station_location()
        output = station_finder.best_location
        expected_output = (5, 8)
        self.assertSequenceEqual(output, expected_output)
        
    def test_N_asteroids_best_location_example2(self):
        station_finder = monotoring_station('Input/day10_part1_example2.txt' )
        station_finder.find_best_station_location()
        output = station_finder.N_visible_at_best_location
        expected_output = 33
        self.assertEqual(output, expected_output)

    def test_best_location_example4(self):
        station_finder = monotoring_station('Input/day10_part1_example4.txt' )
        station_finder.find_best_station_location()
        output = station_finder.best_location
        expected_output = (11, 13)
        self.assertSequenceEqual(output, expected_output)
        
    def test_N_asteroids_best_location_example4(self):
        station_finder = monotoring_station('Input/day10_part1_example4.txt' )
        station_finder.find_best_station_location()
        output = station_finder.N_visible_at_best_location
        expected_output = 210
        self.assertEqual(output, expected_output)  

if( __name__ == "__main__" ):
    unittest.main()