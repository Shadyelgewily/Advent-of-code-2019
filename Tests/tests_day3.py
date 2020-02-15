# -*- coding: utf-8 -*-

#To do: Find out best practice with imports (probably use Day2. instead of enumerating)
import unittest
from Day3.class_wirepath import wirepath
from Day3.class_fuel_management_circuit import fuel_management_circuit
from Day3.load_input import load_wires

class TestSuite(unittest.TestCase):
    
    def setUp(self):
        self.test_circuit1 = fuel_management_circuit()
        test_wire1 = wirepath(['R990','U796','R784'])
        test_wire2 = wirepath(['R1000','U850','L1000'])
        self.test_circuit1.add_wire(test_wire1)
        self.test_circuit1.add_wire(test_wire2)
    
    def test_wirepath(self):
        result = self.test_circuit1.wires[0].get_wire_position_sequence()
        expected_result = [(0,0), (990, 0), (990, 796), (1774, 796)]
    
    def test_is_move_horizontal_false_positive(self):
        result = self.test_circuit1.is_move_horizontal((0,5))
        expected_result = False
        
        self.assertIs(result, expected_result)
        
    def test_is_move_horizontal_true_positive(self):
        result = self.test_circuit1.is_move_horizontal((5,0))
        expected_result = True
        
        self.assertIs(result, expected_result)
        
    def test_is_move_vertical_false_positive(self):
        result = self.test_circuit1.is_move_vertical((5,0))
        expected_result = False
        
        self.assertIs(result, expected_result)
        
    def test_is_move_vertical_true_positive(self):
        result = self.test_circuit1.is_move_vertical((0,5))
        expected_result = True
        
        self.assertIs(result, expected_result)
        
    def test_are_moves_perpendicular_true_positive1(self):
        result = self.test_circuit1.are_moves_perpendicular((0,5),(3,0))
        expected_result = True
        
        self.assertIs(result, expected_result)
        
    def test_are_moves_perpendicular_true_positive2(self):
        result = self.test_circuit1.are_moves_perpendicular((5,0),(0,3))
        expected_result = True
        
        self.assertIs(result, expected_result)
        
    def test_are_moves_perpendicular_false_positive1(self):
        result = self.test_circuit1.are_moves_perpendicular((0,5),(0,3))
        expected_result = False
        
        self.assertIs(result, expected_result)
    
    def test_are_moves_perpendicular_false_positive2(self):
        result = self.test_circuit1.are_moves_perpendicular((5,0),(3,0))
        expected_result = False
        
        self.assertIs(result, expected_result)
    
    def test_find_direction_between_positions(self):
        result = self.test_circuit1.find_direction_between_positions((1,1), (3,6))
        expected_result = (2,5)
        
        self.assertEqual(result, expected_result)
        
    def test_find_intersection_if_perpendicular_directions(self):
        start_position_vertical_wire = (1000,850)
        start_position_horizontal_wire = (990, 796)
        
        result = self.test_circuit1.find_intersection_if_perpendicular_directions(start_position_vertical_wire,
                                                                                  start_position_horizontal_wire)
        expected_result = (1000,796)
        
        self.assertEqual(result, expected_result)
    
    def test_is_coordinate_on_horizontal_wirepiece_true_positive(self):
        start_position_horizontal_wire = (500, 796)
        end_position_horizontal_wire = (990, 796)
        test_coordinate = (550, 796)
        
        result = self.test_circuit1.is_coordinate_on_horizontal_wirepiece(test_coordinate,
                                                                           start_position_horizontal_wire,
                                                                           end_position_horizontal_wire)
        expected_result = True
        
        self.assertIs(result, expected_result)
    
    def test_is_coordinate_on_horizontal_wirepiece_false_positive(self):
        start_position_horizontal_wire = (500, 796)
        end_position_horizontal_wire = (990, 796)
        test_coordinate = (499, 796)
        
        result = self.test_circuit1.is_coordinate_on_horizontal_wirepiece(test_coordinate,
                                                                           start_position_horizontal_wire,
                                                                           end_position_horizontal_wire)
        expected_result = False
        
        self.assertIs(result, expected_result)
     
    def test_is_coordinate_on_horizontal_wirepiece_wrong_y(self):
        start_position_horizontal_wire = (500, 796)
        end_position_horizontal_wire = (990, 796)
        test_coordinate = (500, 800)
        
        result = self.test_circuit1.is_coordinate_on_horizontal_wirepiece(test_coordinate,
                                                                           start_position_horizontal_wire,
                                                                           end_position_horizontal_wire)
        expected_result = False
        
        self.assertIs(result, expected_result)
        
    def test_is_coordinate_on_wirepiece_horizontal(self):
        start_position_wirepiece = (500, 796)
        end_position_wirepiece = (990, 796)
        test_coordinate = (600, 796)
    
        result = self.test_circuit1.is_coordinate_on_wirepiece(test_coordinate,
                                                               start_position_wirepiece,
                                                               end_position_wirepiece)
        expected_result = True
        
        self.assertIs(result, expected_result)
    
    def test_is_coordinate_on_wirepiece_vertical(self):
        start_position_wirepiece = (500, 800)
        end_position_wirepiece = (500, 0)
        test_coordinate = (500, 750)
    
        result = self.test_circuit1.is_coordinate_on_wirepiece(test_coordinate,
                                                               start_position_wirepiece,
                                                               end_position_wirepiece)
        expected_result = True
        
        self.assertIs(result, expected_result)
    
    def test_is_valid_perpendicular_intersection_true_positive(self):
        start_position_vertical_wirepiece = (1000, 0)
        end_position_vertical_wirepiece = (1000,850)
        start_position_horizontal_wirepiece = (990, 796)
        end_position_horizontal_wirepiece = (1200, 796)
        intersection = (1000,796)
        
        result = self.test_circuit1.is_valid_perpendicular_intersection(intersection,
                                                                        start_position_vertical_wirepiece,
                                                                        end_position_vertical_wirepiece,
                                                                        start_position_horizontal_wirepiece,
                                                                        end_position_horizontal_wirepiece
                                                                        )
        expected_result = True
        
        self.assertIs(result, expected_result)

    def test_is_valid_perpendicular_intersection_false_positive(self):
        start_position_vertical_wirepiece = (1000, 0)
        end_position_vertical_wirepiece = (1000,850)
        start_position_horizontal_wirepiece = (990, 796)
        end_position_horizontal_wirepiece = (999, 796)
        intersection = (1000,796)
        
        result = self.test_circuit1.is_valid_perpendicular_intersection(intersection,
                                                                        start_position_vertical_wirepiece,
                                                                        end_position_vertical_wirepiece,
                                                                        start_position_horizontal_wirepiece,
                                                                        end_position_horizontal_wirepiece
                                                                        )
        expected_result = False
        
        self.assertIs(result, expected_result)
              
    def test_find_intersection_if_parallel_directions(self):
        result =  self.test_circuit1.find_intersection_if_parallel_directions()
        
        self.assertEqual(result, None)
        
    def test_get_overlapping_part_wirepieces_vertical(self):
        start_position_wirepiece1 = (1000, 0)
        end_position_wirepiece1 = (1000,850)
        start_position_wirepiece2 = (1000, 5)
        end_position_wirepiece2 = (1000, 750)
        
        result = self.test_circuit1.get_overlapping_part_wirepieces(start_position_wirepiece1,
                                                                    end_position_wirepiece1,
                                                                    start_position_wirepiece2,
                                                                    end_position_wirepiece2)
        expected_result = [(1000,5), (1000,750)]
        
        self.assertEqual(result, expected_result)
        
    def test_get_overlapping_part_wirepieces_horizontal(self):
        start_position_wirepiece1 = (500, 850)
        end_position_wirepiece1 = (600,850)
        start_position_wirepiece2 = (502, 850)
        end_position_wirepiece2 = (608, 850)
        
        result = self.test_circuit1.get_overlapping_part_wirepieces(start_position_wirepiece1,
                                                                    end_position_wirepiece1,
                                                                    start_position_wirepiece2,
                                                                    end_position_wirepiece2)
        expected_result = [(502,850), (600,850)]
        
        self.assertEqual(result, expected_result)
    
    def test_find_intersections_if_overlapping_directions_horizontal(self):
        start_position_wirepiece1 = (500, 850)
        end_position_wirepiece1 = (505,850)
        start_position_wirepiece2 = (501, 850)
        end_position_wirepiece2 = (504, 850)
        
        result = self.test_circuit1.find_intersections_if_overlapping_directions(start_position_wirepiece1,
                                                                                end_position_wirepiece1,
                                                                                start_position_wirepiece2,
                                                                                end_position_wirepiece2)
        expected_result = [(501,850), (502,850), (503,850), (504, 850)]
        
        self.assertEqual(result, expected_result)
    
    def test_find_intersections_if_overlapping_directions_vertical(self):
        start_position_wirepiece1 = (500, 850)
        end_position_wirepiece1 = (500,840)
        start_position_wirepiece2 = (500, 840)
        end_position_wirepiece2 = (500, 843)
        
        result = self.test_circuit1.find_intersections_if_overlapping_directions(start_position_wirepiece1,
                                                                                end_position_wirepiece1,
                                                                                start_position_wirepiece2,
                                                                                end_position_wirepiece2)
        expected_result = [(500,840), (500,841), (500,842), (500, 843)]
        
        self.assertEqual(result, expected_result)
        
    def test_manhattan_distance(self):
        
        result = self.test_circuit1.calc_manhattan_distance((0,0), (5,3))
        expected_result = 8
        
        self.assertEqual(result, expected_result)

if( __name__ == "__main__" ):
    unittest.main()