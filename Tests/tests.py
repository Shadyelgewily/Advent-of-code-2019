# -*- coding: utf-8 -*-

#To do: Find out best practice with imports (probably use Day2. instead of enumerating)
import unittest
from Day1 import calculate_fuel, calculate_fuel_partb, make_list_if_single_number
from Day2.intcode_program import intcode_program
from Day2.read_gravity_assist_program import read_gravity_assist_program

#To do: add test with input to Day 2 Advent of code challenge
class TestSuite(unittest.TestCase):
    def test_calculate_fuel_single_number(self):
        self.assertEqual(calculate_fuel(12), 2 )
        
    def test_calculate_fuel_list_single_item(self):
        self.assertEqual(calculate_fuel([14]), 2 )
    
    def test_calculate_fuel_list_multiples_items(self):
        self.assertEqual(calculate_fuel([12,14]), 4 )
        
    def test_calculate_fuel_partb_single_number(self):
        self.assertEqual(calculate_fuel_partb(14), 2 )
        
    def test_calculate_fuel_partb_list_single_item(self):
        self.assertEqual(calculate_fuel_partb([1969]), 966 )
    
    def test_calculate_fuel_partb_list_multiples_items(self):
        self.assertEqual(calculate_fuel_partb([100756, 0]), 50346 )
        
    def test_make_list_if_single_number(self):
        self.assertEqual(make_list_if_single_number(0), [0])
        
    def test_make_list_if_single_number_list(self):
        self.assertEqual(make_list_if_single_number([0,2]), [0,2])
    
    def test_invalid_initial_opcode(self):
        with self.assertRaises(ValueError): 
            intcode_program([7,3,7])
        
    def test_replace_value_at_memory_address(self):
        intcode_program_instance = intcode_program([2,3,7])
        
        intcode_program_instance.replace_value_at_memory_address(0,1)
        result = intcode_program_instance.get_current_memory_state()
        
        self.assertEqual(result, [1,3,7] )
        
    def test_replace_value_at_memory_address_error(self):
        intcode_program_instance = intcode_program([1,3,7])
        
        with self.assertRaises(IndexError):
            intcode_program_instance.replace_value_at_memory_address(7,1)
    
    def test_get_initial_opcode(self):
        intcode_program_instance = intcode_program([1,3,6])
        
        result = intcode_program_instance.get_opcode()
        
        self.assertEqual(result, 1)
    
    def test_valid_next_opcode(self):
        intcode_program_instance = intcode_program([1,3,6,7,99])
        
        intcode_program_instance.set_next_instruction_pointer_and_opcode_value()
        result = intcode_program_instance.get_opcode()
        
        self.assertEqual(result, 99)
    def test_invalid_next_opcode(self):
        intcode_program_instance = intcode_program([1,3,6,7,3])
        
        with self.assertRaises(ValueError):
            intcode_program_instance.set_next_instruction_pointer_and_opcode_value()
        
    def test_next_opcode_index_error(self):
        intcode_program_instance = intcode_program([1,3,6])
        
        with self.assertRaises(IndexError):
            intcode_program_instance.set_next_instruction_pointer_and_opcode_value()

    def test_get_parameters_for_next_instruction(self):
        intcode_program_instance = intcode_program([1,0,0,0,99])
        
        result = intcode_program_instance.get_parameters_for_next_instruction()
        
        self.assertEqual(result, (1,1))
    
    def test_get_address_to_store_next_instruction_result(self):
        intcode_program_instance = intcode_program([1,0,0,0,99])
        
        result = intcode_program_instance.get_address_to_store_next_instruction_result()
        
        self.assertEqual(result, 0)
        
    def test_intcode_program1(self):
        intcode_program_instance = intcode_program([1,0,0,0,99])
        intcode_program_instance.execute_intcode_program()
        
        result = intcode_program_instance.get_current_memory_state()
        
        self.assertEqual(result, [2,0,0,0,99])
    
    def test_intcode_program2(self):
        intcode_program_instance = intcode_program([2,3,0,3,99])
        intcode_program_instance.execute_intcode_program()
        
        result = intcode_program_instance.get_current_memory_state()
        
        self.assertEqual(result, [2,3,0,6,99])
        
    def test_intcode_program3(self):
        intcode_program_instance = intcode_program([2,4,4,5,99,0])
        intcode_program_instance.execute_intcode_program()
        
        result = intcode_program_instance.get_current_memory_state()
        
        self.assertEqual(result, [2,4,4,5,99,9801])
        
    def test_intcode_program4(self):
        intcode_program_instance = intcode_program([1,1,1,4,99,5,6,0,99])
        intcode_program_instance.execute_intcode_program()
        
        result = intcode_program_instance.get_current_memory_state()
        
        self.assertEqual(result, [30,1,1,4,2,5,6,0,99])
        
    def test_intcode_program5(self):
        intcode_program_instance = intcode_program([1,9,10,3,2,3,11,0,99,30,40,50])
        intcode_program_instance.execute_intcode_program()
        
        result = intcode_program_instance.get_current_memory_state()
        
        self.assertEqual(result, [3500,9,10,70,2,3,11,0,99,30,40,50])
        
    def test_gravity_assist_program(self):
        intcode_program_input = read_gravity_assist_program("Input/day2.txt")
        intcode_program_instance = intcode_program(intcode_program_input)
        intcode_program_instance.restore_gravity_assist_program()
        intcode_program_instance.execute_intcode_program()
        
        result = intcode_program_instance.get_current_memory_state()[0]
        
        self.assertEqual(result, 2782414)
        
    def test_find_noun_and_verb_that_produces_output_1(self):
        intcode_program_input = read_gravity_assist_program("Input/day2.txt")
        intcode_program_instance = intcode_program(intcode_program_input)
        
        result = intcode_program_instance.find_noun_and_verb_that_produces_output(2782414)
        
        self.assertEqual(result, 1202)
    
    def test_find_noun_and_verb_that_produces_output_2(self):
        intcode_program_input = read_gravity_assist_program("Input/day2.txt")
        intcode_program_instance = intcode_program(intcode_program_input)
        
        result = intcode_program_instance.find_noun_and_verb_that_produces_output(19690720)
        
        self.assertEqual(result, 9820)

if( __name__ == "__main__" ):
    unittest.main()