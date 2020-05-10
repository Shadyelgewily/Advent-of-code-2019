# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:05:45 2020

@author: quiet
"""

import unittest
import numpy as np
from Day8.class_image_decoder import image_decoder

class TestSuite(unittest.TestCase):
    def test_part1_example(self):
        image = image_decoder('Input/day8_part1_example.txt', 3, 2 )
        output = image.answer_part1
        expected_output = 1
        
        self.assertIs(output, expected_output)
        
    def test_part2_example(self):
        image = image_decoder('Input/day8_part2_example.txt', 2, 2 )
        image.decode_image()
        output = image.decoded_image
        expected_output = np.array([[0,1],[1,0]])
        self.assertEqual(output.tolist(), expected_output.tolist())

if( __name__ == "__main__" ):
    unittest.main()